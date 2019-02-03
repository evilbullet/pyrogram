"""This example shows how to retrieve the full message history of a chat"""

import time

from pyrogram import Client
from pyrogram import Message
from pyrogram.api.errors import FloodWait

from PIL import Image
import webbrowser

app = Client(
"my_account", api_id=668604, api_hash="691dfb6e3825de315413c995ee3dd558"
)
target = "memlrd"  # "me" refers to your own chat (Saved Messages)
messages = []  # List that will contain all the messages of the target chat
offset_id = 10  # ID of the last message of the chunk

with app:
    while True:
        try:
            m = app.get_history(target, offset_id=offset_id)
        except FloodWait as e:  # For very large chats the method call can raise a FloodWait
            print("waiting {}".format(e.x))
            time.sleep(e.x)  # Sleep X seconds before continuing
            continue

        if not m.messages:
            break

        messages += m.messages
        offset_id = m.messages[-1].message_id

        bot_t = app.session_name
        fi = ''
        for i in range(len(messages)):
            try:
                print(messages[i].views)
                try:
                    print(messages[i].photo.sizes[0]['file_id'])#, app.get_me())
                    # fi = messages[i].photo.sizes[0]['file_id']
                except:
                    print('no photo')
            except:
                print('no view')
            i += 1
        fi = 'AgADAgADT6gxG8Fv8UiY5yi_xaWKGjoySw0ABPWaLPUe4QABCPVkDgABAg'
        bt = '275227150'
        print('https://api.telegram.org/file/bot{}/{}'.
                          format(bt, fi))
        print('https://api.telegram.org/file/{}/{}'.
                          format(bt, fi))
        app.send_photo('memlrd', 'AgADAgADT6gxG8Fv8UiY5yi_xaWKGjoySw0ABPWaLPUe4QABCPVkDgABAg')
        print('https://api.telegram.org/file/bot{}/{}'.
                          format(app.bot_token, fi))
        print('https://api.telegram.org/file/bot{}/{}'.
                          format(app.bot_token, fi))
        # print('https://api.telegram.org/file/bot{}/{}'.
        #                  format(app.api_hash,fi))
        # print('https://api.telegram.org/file/bot{}/{}'.
        #                  format(app.api_id,fi))

        # webbrowser.open('https://api.telegram.org/file/bot{}/{}'.
        #                  format(app.bot_token,fi))

# Now the "messages" list contains all the messages sorted by date in
# descending order (from the most recent to the oldest one)
