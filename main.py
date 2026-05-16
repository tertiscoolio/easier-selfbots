#example self bot
import easier_selfbot
from easier_selfbot import send_message, read_last_message, spam_message
easier_selfbot.token = "discord_token"
easier_selfbot.channel_id = "channel_id"


while True:
    last_mess = read_last_message()

    if last_mess == ".ping":
        send_message("pong")
    elif ".spam" in last_mess:
        spam_message("message", 10)


