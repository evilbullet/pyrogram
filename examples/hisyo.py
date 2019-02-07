"""This example shows how to get the full message history of a chat, starting from the latest message"""

from pyrogram import Client

app = Client("my_account")
target = "memlrd"  # "me" refers to your own chat (Saved Messages)
x = []
image_ids = []
with app:
    while True:
        x = app.get_history(target, limit=10)
        image_ids+=x.messages
        if not x.messages:
            break

for post in image_ids:
    print(post[0].sizes)
    # if post.photo.sizes[0]['file_id'] and post.photo.sizes[3]['file_id']:
    #     print (image_ids.append(post.photo.sizes[0]['file_id']))
    # # print(x)
# with app:
#     for message in app.get_history(chat_id=target, limit=10):
#         print(message.text)