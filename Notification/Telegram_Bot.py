from telegram import Bot
import sys
from dotenv import load_dotenv
import os
sys.path.append("C:\\Users\\prana\\OneDrive\\Documents\\pyApps\\Web-Scrapper-Organised\\Class_files")
from JobClass import Job
import asyncio

load_dotenv()

async def compose_msg(Job):
    bot_token = os.getenv('Telegram_Bot_Key') 
    chat_id = os.getenv("Chat_ID")
    message = f"""Job Name: {Job.name}
Location: {Job.location}
Description: {Job.description}

Link to Apply: {Job.href}"""

    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)


# async def send_msg(Job):
#     asyncio.run(compose_msg(Job))