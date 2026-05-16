# easier self bot

I made this just for fun but you can use it for your own projects

# what does it do?
its made for self bots that are used in discord and highly customizable 

# how do i use it?
this is an example its not the best because it was made in under an hour 


read_last_message() is a function that reads the last message that was sent in a channel id 

send_message('example text') its a function that sends text into the channel u set it to

spam_message('message thats spammed', number of times) this function is pretty self explationory it spams the channel u set it to with a custom set of times

```py
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



```

# how to install it?

its pretty easy just install the file named easier_selfbot.py and put it in the project that u want to use it 

add this to ur main python file or the one handling the self bot
```py
import easier_selfbot
from easier_selfbot import send_message, read_last_message, spam_message
easier_selfbot.token = "discord_token"
easier_selfbot.channel_id = "channel_id"
```
