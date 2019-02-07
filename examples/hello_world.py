"""This example demonstrates a basic API usage"""

from pyrogram import Client

# Create a new Client instance
app = Client(
             "my_account", api_id=668604, api_hash="691dfb6e3825de315413c995ee3dd558"
             )
# api_id = 668604
# api_hash = 691dfb6e3825de315413c995ee3dd558

# Start the Client before calling any API method
app.start()

# Send a message to yourself, Markdown is enabled by default
app.send_message("me", "Hi there! I'm using **Pyrogram** {}".format(app.get_me()))
#id 275227150
m = app.get_history('me', 20)
for mm in m:
    print(mm.messages)
# print(m.messages[0].photo.sizes[0]['file_id'])
# Send a location to yourself
# app.send_location("me", 51.500729, -0.124583)

# app.send_photo("me",
#                'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')


# Stop the client when you're done
app.stop()
