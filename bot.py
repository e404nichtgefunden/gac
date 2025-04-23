from pyrogram import Client

api_id = 24366117
api_hash = "99aa6457d4734bbf0d86c92b5dcbf0c9"
bot_token = "7970941805:AAGvOT_-D2veOwDe8nqyxb_771sDaL425q8"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

app.run()