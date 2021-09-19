from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.info import *


@Client.on_callback_query()
async def callback(bot, update):
    data = update.data
    if data == "close":
        update.message.delete()
