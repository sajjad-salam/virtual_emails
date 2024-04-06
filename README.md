 # Temporary Email Bot

This bot creates a temporary email address for users and forwards any emails received to their Telegram chat. It also periodically checks for new emails and sends notifications to users when new emails arrive.

## Code Explanation

### 1. Importing Libraries

```python
import telebot
import random
import string
import requests
from telebot import types
import time
```

- `telebot`: This library is used to create a Telegram bot.
- `random` and `string`: These libraries are used to generate random usernames for temporary email addresses.
- `requests`: This library is used to make HTTP requests to the 1secmail API.
- `time`: This library is used to keep track of the time of the last email check.

### 2. Defining Constants

```python
API = 'https://www.1secmail.com/api/v1/'
domain_list = ["1secmail.com", "1secmail.org", "1secmail.net"]
```

- `API`: This is the base URL for the 1secmail API.
- `domain_list`: This is a list of the available 1secmail domains.

### 3. Defining the Bot Token

```python
TOKEN =input(F+'::token')
bot = telebot.TeleBot(TOKEN)
```

- `TOKEN`: This is the Telegram bot token. You can obtain this token by creating a bot on the Telegram BotFather.
- `bot`: This is the Telegram bot object.

### 4. Defining User Emails Dictionary

```python
user_emails = {}
```

- `user_emails`: This dictionary stores the temporary email addresses for each user. The keys are the user IDs, and the values are dictionaries containing the email address, the last check time, and the chat ID.

### 5. Start Command Handler

```python
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "مرحبًا بك في بوت البريد المؤقت! أرسل لي أي رسالة للبدء.")
```

- This function handles the `/start` command. It sends a welcome message to the user and prompts them to send any message to start using the bot.

### 6. Generating a Random Username

```python
def generate_username():
```


```markdown
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


```



<img src="https://img.shields.io/badge/PYTHON-black?style=for-the-badge&logo=python&logoColor=gold"/>
