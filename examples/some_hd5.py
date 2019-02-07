
import time
from pyrogram import Client
from pyrogram import Message
from pyrogram.api.errors import FloodWait
from PIL import Image
import h5py
import json
# from tables import *

import numpy as np

def dataset_maker(ff, sf):
    channels_name = 'name1'
    date = 'date'
    with h5py.File('dataset_1.hdf5', 'w') as f:
        d = f.create_dataset('channels_dataset',
                             (channels_name, date, 1), maxshape=(1024, 1024, None))
        d[:, :, 0] = ff
        d.resize((1024, 1024, 2))
        d[:, :, 1] = sf

def send_photo_to_channel(chs):
    '''   '''
    channels = ['memes', 'laughingC']
    app = Client("memlrd", api_id=668604, api_hash="691dfb6e3825de315413c995ee3dd558")

    target = chs  # "me" refers to your own chat (Saved Messages)
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
                    print(type(messages[i].views))
                    try:
                        print(type(messages[i].photo.sizes[0]['file_id']))  # , app.get_me())
                        print(messages[i])  # fi = messages[i].photo.sizes[0]['file_id']
                    except:
                        print('no photo')
                except:
                    print('no view')
                i += 1
            fi = 'AgADAgADT6gxG8Fv8UiY5yi_xaWKGjoySw0ABPWaLPUe4QABCPVkDgABAg'
            # app.send_photo('me', fi)

# Now the "messages" list contains all the messages sorted by date in  # descending order (from the most recent to the oldest one)
def top_3posts():
    channels = ['memes', 'laughingC']
    app = Client("memlrd", api_id=668604, api_hash="691dfb6e3825de315413c995ee3dd558")
    target = 'memlrd'  # "me" refers to your own chat (Saved Messages)
    messages = []  # List that will contain all the messages of the target chat
    offset_id = 90  # ID of the last message of the chunk

    no_photo, no_view = 0, 0
    image_ids = []
    with app:
        while True:
            try:
                m = app.get_history(target, offset_id=offset_id)
                messages += m.messages
                print(len(messages))
                # offset_id = m.messages[-1].message_id
            except FloodWait as e:  # For very large chats the method call can raise a FloodWait
                print("waiting {}".format(e.x))
                time.sleep(e.x)  # Sleep X seconds before continuing
                continue
            if not m.messages:
                break

    print(len(messages))
    for i in range(len(messages)):
        try:
            if messages[i].photo.sizes[0]['file_id']:
                image_ids.append(messages[i].photo.sizes[0]['file_id'])
        except:
            no_view += 1
        i += 1
    print(no_view, image_ids)