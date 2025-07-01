import sys
import asyncio

sys.path.append("C:\\Users\\prana\\OneDrive\\Documents\\pyApps\\Web-Scrapper-Organised\\Website-Scrapped")
sys.path.append("C:\\Users\\prana\\OneDrive\\Documents\\pyApps\\Web-Scrapper-Organised\\Notification")

from Telegram_Bot import compose_msg
from GS_main import SearchJobGS

positionName = input("Enter Job Title: ")


JOBS = SearchJobGS(positionName)


async def send_all_jobs(jobs):
    try:
        for job in jobs:
            await compose_msg(job)
            await asyncio.sleep(1)
    except:
        print("Something went wrong!!")
asyncio.run(send_all_jobs(JOBS))






