import telebot
import random
import string
import requests
from telebot import types
import time

API = 'https://www.1secmail.com/api/v1/'
domain_list = ["1secmail.com", "1secmail.org", "1secmail.net"]
print("\033[97;1m[\033[92;1m+\033[97;1m] \x1b[1;38;5;121m MY INFO https://t.me/KING_OF_ENG")
import os
import requests
import time
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
#-------------------#
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33'
#-----------------------------------------------------#
bRIMON="\033[1;30m" 
M="\033[1;31m"       
H="\033[1;33m"               
byellow="\033[1;33m"     
bblue="\033[1;34m"        
P="\033[1;35m"               
C="\033[1;36m"          
B="\033[1;37m"       
G="\033[1;32m"              
R="\033[1;31m"
AA="\033[1;32m"
BB="\033[1;31m"
CC="\033[1;36m"
X='\033[1;30m'
XX="\x1b[38;5;196m"
GGG="\x1b[38;5;214m"
print(f"""\x1b[1;38;5;121m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢀⠀⠀⠀⣰⡇⢀⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⣿⣰⡀⢠⣿⣇⣾⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣰⣿⣿⢇⣾⣿⣼⣿⢃⡞⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⢋⣾⣿⣿⣿⣯⣿⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢟⣵⣿⣿⣿⣿⣿⣿⣯⡞⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣵⣿⣿⣿⣿⣿⣿⣿⣿⡿⡁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣦⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡡⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⠀⢀⣀⣄⣀⡀⡀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡥⠀⠀⠀⠀⠀⠀
⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠘⣿⠋⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀ENG-SAJJAD
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡛⠃⠀⠀
⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀
⠀⠀⠀⠀⠀⢰⣾⣿⣿⣿⣿⣿⠟⠁⠉⠙⠻⠯⡛⠿⠛⠻⠿⠟⠛⠓⠀⠀
⠀⠜⡿⠳⡶⠻⣿⣿⣿⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣽⣧⣾⠛⠉⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠟⠁⠘⠃
  
{G}⋆{GGG}\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;46m AUTHOR    \x1b[1;97m ● \x1b[1;92m ENG.SAJJAD
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47mUESER  \x1b[1;97m    ● \x1b[1;92m@S_J_O_D
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}]\x1b[38;5;48m INFO   \x1b[1;97m    ● \x1b[1;92m BOT_YOUTOBE_DOWNLOADER
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47mTOOLS     \x1b[1;97m ● \x1b[1;92mNO
\x1b[1;92m {XX}[\x1b[1;92m⍣{XX}] \x1b[38;5;47mVERSION   \x1b[1;97m ● \x1b[1;92mV.1                 
{G}⋆{GGG}\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆""")
import os
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
try:
	import requests
except ImportError:
    Z = '''[1;31m'''
R = '''[1;31m'''
X = '''[1;33m'''
F = '''[2;32m'''
C = '''[1;97m'''
B = '''[2;36m'''
Y = '''[1;34m'''
E = '''[1;31m'''
B = '''[2;36m'''
G = '''[1;32m'''
S = '''[1;33m'''
ses = requests.Session()
F = '''[2;32m'''
Z = '''[1;31m'''
L = '''[1;95m'''
E = '''[1;31m'''
G = '''[1;32m'''
S = '''[1;33m'''
Z = '''[1;31m'''
X = '''[1;33m'''
Z1 = '''[2;31m'''
F = '''[2;32m'''
A = '''[2;39m'''
C = '''[2;35m'''
B = '''[2;36m'''
Y = '''[1;34m'''
xxh = '\x1b[38;5;208m'#برتقالي
r1='\x1b[38;5;8m'#رمادي
e1='\x1b[38;5;196m'#احمر
w1='\x1b[38;5;225m'#وردي فاتح جدا
t1='\x1b[38;5;92m'#بنفسجي غامق
y1='\x1b[1;93m'#اصفر نيون
u1='\x1b[1;38;5;203m'#وردي لطيف
i1='\x1b[1;38;5;121m'#اخضر نيون
o1='\x1b[1;96m'#ازرق سماوي
p1='\x1b[38;5;205m'#وردي فاتح
a1='\x1b[38;5;161m'#وردي جميل جدا
S0='\x1b[1;93m'  
S9='\x1b[1;38;5;121m'
S8='\x1b[1;93m'
S7='\x1b[38;5;92m' 
S6='\x1b[1;38;5;121m' 
S5='\x1b[1;38;5;121m'
S4='\x1b[1;96m'
S3='\x1b[1;38;5;121m'
S2='\x1b[38;5;92m' 
S1='\x1b[1;38;5;121m' 
S00='\x1b[1;38;5;121m' 
S99='\x1b[1;96m'
S88='\x1b[1;38;5;121m'
S77='\x1b[38;5;117m'
S66='\x1b[1;32m'
S55='\x1b[38;5;117m'
S44='\x1b[38;5;180m'
S33='\x1b[1;38;5;121m'
S22='\x1b[38;5;117m'
S11='\033[2;35m'
S000='\x1b[38;5;117m'
S999='\x1b[1;32m'
S888='\x1b[38;5;117m'
S777='\x1b[1;38;5;121m'
time1 = time.localtime()
time2 = time.strftime('''%d/%m/%Y''')
print('')
time3 = time.strftime('''%H:%M:%S''')
print('')
print('')
print(f'''{C} \x1b[38;5;208m 𝕋ℍ𝔼 𝔻𝔸𝕋𝔼 \x1b[1;38;5;121m ♥   \x1b[1;38;5;121m   ♣ \x1b[1;96m{time2} \x1b[1;38;5;121m ♣''')
print('')
print(f'''{C} \x1b[38;5;208m 𝕋ℍ𝔼 𝕋𝕀𝕄𝔼 \x1b[1;38;5;121m ♥   \x1b[1;38;5;121m    ♣	\x1b[1;96m{time3} \x1b[1;38;5;121m ♣''')
print()
print(' ✖✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖  ')
print()
TOKEN=input('  \x1b[38;5;117m{\x1b[1;32m•\x1b[38;5;117m}  \x1b[38;5;180m𝐓𝐎𝐊𝐄𝐍  \x1b[1;38;5;121m ๛   \x1b[38;5;117m')
bot = telebot.TeleBot(TOKEN)
print('\033[2;35m')
print(' ✖✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖  ')
print()
print()
print(' ✖✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖  ')
print("the bot is ready to work by @S_J_O_D ")			

# TOKEN =input(F+'::token')
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
