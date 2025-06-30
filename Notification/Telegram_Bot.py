from telegram import Bot
import sys
sys.path.append("C:\\Users\\prana\\OneDrive\\Documents\\pyApps\\Web-Scrapper-Organised\\Class_files")
from JobClass import Job
import asyncio

async def compose_msg(Job):
    bot_token = "8125656504:AAFRi-A_RUEzGWE-YOwHuA1EUyXHXpLlj6U"
    chat_id = "978476978"
    message = f"""Job Name: {Job.name}
Location: {Job.location}
Description: {Job.description}

Link to Apply: {Job.href}"""

    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)


# async def send_msg(Job):
#     asyncio.run(compose_msg(Job))