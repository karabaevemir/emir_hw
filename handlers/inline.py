from aiogram import types, Dispatcher
from youtube_searcher import  as YT
import hashlib


def finder(text):
    return YT(text, max_results=5).to_dict()


async def inline_youtube_handler(query: types.InlineQuery):
    text = query.query or "echo"
    links = finder(text)
    articles = []
    for link in links:
        article = types.InlineQueryResultArticle(
            id=hashlib.md5(f"{link['id']}".encode()).hexdigest(),
            title=link['title'],
            url=f"https://www.youtube.com{link['url_suffix']}",
            thumb_url=f"{link['thumbnails'][0]}",
            input_message_content=types.InputMessageContent(
                message_text=f"Вот ссылка\nhttps://www.youtube.com{link['url_suffix']}"
            )
        )
        articles.append(article)

    await query.answer(articles, cache_time=20)


def register_inline(dp: Dispatcher):
    dp.register_handler(inline_youtube_handler)