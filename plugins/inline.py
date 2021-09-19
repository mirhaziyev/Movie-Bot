import requests
from requests.utils import requote_uri
from pyrogram import Client, filters 
from pyrogram.types import *
from .commands import BUTTONS
from .info import API, thumb, description, info


@Client.on_inline_query()
async def inline_info(bot, update):
    query = update.query
    num = None
    if "+" in query:
        movie_name, num = query.split("+", -1)
    else:
        movie_name = query
    r = requests.get(API + requote_uri(movie_name))
    movies = [r.json()[int(num) - 1]] if num else r.json()
    results = []
    for movie in movies:
        try:
            results.append(
                InlineQueryResultArticle(
                    title=movie['title'],
                    thumb_url=thumb(movie),
                    description=description(movie),
                    input_message_content=InputTextMessageContent(
                        message_text=info(movie),
                        disable_web_page_preview=True
                    ),
                    reply_markup=BUTTONS
                )
            )
        except:
            pass
    await update.answer(results)
