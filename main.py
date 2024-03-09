import telebot
import random
import string
import requests
from telebot import types
import time

API = 'https://www.1secmail.com/api/v1/'
domain_list = ["1secmail.com", "1secmail.org", "1secmail.net"]

TOKEN =input(F+'::token')
bot = telebot.TeleBot(TOKEN)

user_emails = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "مرحبًا بك في بوت البريد المؤقت! أرسل لي أي رسالة للبدء.")

def generate_username():
    name = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(name) for i in range(10))
    return username

def check_mail(mail='', chat_id=None):
    req_link = f'{API}?action=getMessages&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
    r = requests.get(req_link).json()
    length = len(r)

    if length == 0:
        bot.send_message(chat_id, 'لا توجد رسائل في الوقت الحالي سوف تصلك الرسائل فور وصولها')
    else:
        id_list = []

        for i in r:
            for k, v in i.items():
                if k == 'id':
                    id_list.append(v)

        bot.send_message(chat_id, f'لديك {length} رسائل في بريدك الإلكتروني الوهمي')

        for i in id_list:
            read_msg = f'{API}?action=readMessage&login={mail.split("@")[0]}&domain={mail.split("@")[1]}&id={i}'
            r = requests.get(read_msg).json()

            sender = r.get('from')
            subject = r.get('subject')
            date = r.get('date')
            content = r.get('textBody')

            mail_info = f'Sender: {sender}\nTo: {mail}\nSubject: {subject}\nDate: {date}\nContent: {content}'
            bot.send_message(chat_id, mail_info)

def delete_mail(mail='', chat_id=None):
    url = 'https://www.1secmail.com/mailbox'

    data = {
        'action': 'deleteMailbox',
        'login': mail.split('@')[0],
        'domain': mail.split('@')[1]
    }

    r = requests.post(url, data=data)
    bot.send_message(chat_id, f'[X] Email {mail} - Deleted!\n')

def send_new_messages_periodically():
    while True:
        time.sleep(5)
        for user_id, user_data in user_emails.items():
            mail = user_data['email']
            length = get_email_length(mail)
            if 'last_email_length' not in user_data or length != user_data['last_email_length']:
                check_mail(mail=mail, chat_id=user_data['chat_id'])
                user_data['last_email_length'] = length

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        user_id = message.from_user.id
        username = generate_username()
        mail = f'{username}@{random.choice(domain_list)}'
        user_emails[user_id] = {'email': mail, 'last_check_time': time.time(), 'chat_id': message.chat.id}

        bot.send_message(message.chat.id, f'[+] ايميلك الوهمي هو : {mail}')

    except KeyboardInterrupt:
        delete_mail(mail=mail, chat_id=message.chat.id)
        bot.send_message(message.chat.id, 'اكو مشكلة بل بوت حبيبي!')

def get_email_length(mail=''):
    req_link = f'{API}?action=getMessages&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
    r = requests.get(req_link).json()
    return len(r)

# Start the thread to periodically check for new messages
import threading
threading.Thread(target=send_new_messages_periodically).start()

if __name__ == '__main__':
    bot.polling()
