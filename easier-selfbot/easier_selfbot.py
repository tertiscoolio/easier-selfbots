import requests
import time

channel_id = ''
token = ''


def read_last_message():
    time.sleep(3)
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=1'

    headers = {
        'authorization': token
    }
    readmessage = requests.get(url, headers=headers)
    result = readmessage.json()
    if result:
        message_content = result[0]['content']
        print(message_content)
        return message_content
    else:
        print("No messages found")
        return None

def send_message(message):
    nonce = str(int(time.time() * 1000))

    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    headers = {
        'authorization': token,
        'content-type': 'application/json'
    }

    data = {
        'mobile_network_type': 'unknown',
        'content': message,
        'nonce': nonce,
        'tts': False,
        'flags': 0
    }

    sendrequest = requests.post(url, json=data, headers=headers)
    result = sendrequest.json()
    if (result.get('content') == message and
            result.get('tts') == False and
            result.get('flags') == 0 and
            result.get('nonce') == nonce):
        print("✓ Message sent")

    else:
        print("✗ Something went wrong! if u think this is the frameworks problem go to https://discord.gg/bSmDBSFG")


    return result

def spam_message(message, times):
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    headers = {
        'authorization': token,
        'content-type': 'application/json'
    }
    if times <= 0:
        print("use is spam_message(message, number of times) do not use 0 or less")
    elif times is None:
        print("use is spam_message(message, number of times)")
    else:
        time1= 0
        while time1 < times:
            time.sleep(0.5)
            time1 += 1
            nonce = str(int(time.time() * 1000))

            data = {
                'mobile_network_type': 'unknown',
                'content': message,
                'nonce': nonce,
                'tts': False,
                'flags': 0
            }

            sendrequest = requests.post(url, json=data, headers=headers)
            result = sendrequest.json()
            if (result.get('content') == message and
                    result.get('tts') == False and
                    result.get('flags') == 0 and
                    result.get('nonce') == nonce):
                print("✓ Message sent")

            else:
                print("✗ Something went wrong! if u think this is the frameworks problem go to https://discord.gg/bSmDBSFG")


    return result