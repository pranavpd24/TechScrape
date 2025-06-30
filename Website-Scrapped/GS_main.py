from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys


#Local file import
sys.path.append("C:\\Users\\prana\\OneDrive\\Documents\\pyApps\\Web-Scrapper-Organised\\Class_files")
from JobClass import Job
PATH = 'C:\\Users\\prana\\OneDrive\\Documents\\pyApps\\Web-Scrapper-Organised\\Website-Scrapped\\chromedriver.exe'

service = Service(executable_path= PATH)



def PositionStringMakerGS(positionList):
    if (len(positionList)<=1):
        PositionString = positionList[0]
        
    elif len(positionList)>1:    
        PositionString = "%20".join(positionList)
    return PositionString


def DispJobInfo(JOBS):
    count = 1
    for job in JOBS:
        print(f"JOB NUMBER {count}")
        job.DispInfoCorrectly()
        count+=1
    

def RenderPageGS(CUSTOM_PATH):
    driver = webdriver.Chrome(service= service)

    driver.get(CUSTOM_PATH)
    try:
        all_jobs = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "text-decoration-none")))
        JOBS = []
        locations = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'[data-testid="location"]')))
        for job in all_jobs:
            # JOBS.append(job.text)
            # print(job.text)
            job_element = job.text.split('\n')
            job_object = Job(name=job_element[0],location=job_element[1]+job_element[2], href=job.get_attribute('href'))
            # print(job.get_attribute('href'))
            JOBS.append(job_object)
        driver.quit()
        return JOBS
    except:
        print("Someting went wrong! Pls check position name")
    # for location in locations:
    #     print(location.text)
    
    # DispJobInfo(JOBS)
    
    

    # return JOBS



def LastPageFinderGS(PositionString):
    PAGE_PATH_BASE = f"https://higher.gs.com/results?&page=1&search={PositionString}&sort=RELEVANCE"
    driver = webdriver.Chrome(service= service)


    driver.get(PAGE_PATH_BASE)
    try:
        page_diversion = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-cy="gs-uitk-pagination__item"]')))
        page_content=[]
        for page in page_diversion:
            print(page_content.append(page.text))
    
        driver.quit()
        return int(page_content[len(page_content)-1])
    except:
        print("Error in Rendering in Last Page")
    
    




def SearchJobGS(positionName):
    # PositionString = PostionStringMakerGS(position_list)
    position_list = list(positionName.split(" "))
    PositionString = PositionStringMakerGS(position_list)
    try:
        length_of_pages = LastPageFinderGS(PositionString)
        ALL_JOBS=[]
        for i in range(1,min(length_of_pages,2)):
            CUSTOM_PATH = f"https://higher.gs.com/results?&page={i}&search={PositionString}&sort=RELEVANCE"
            Job_list = RenderPageGS(CUSTOM_PATH)
            ALL_JOBS.extend(Job_list)
        return ALL_JOBS
    except:
        print("I think position not exist here")


# positionName = input("Enter position name: ")

# skills = input("Enter you have to search job(Add comma for smooth operation): ")

# position_list = list(positionName.split(" "))

# PostionString = PostionStringMakerGS(position_list)


# Jobs = SearchJobGS(PostionStringMakerGS(list(positionName.split(" "))))4
# SearchJobGS(positionName)

#print(Jobs)

# skills_set = set(skill.strip() for skill in skills.split(','))




    

