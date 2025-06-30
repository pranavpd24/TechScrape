from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

#Importing the Local Files
sys.path.append("C:\\Users\\prana\\OneDrive\\Documents\\pyApps\\Web-Scrapper-Organised\\Class_files")
from JobClass import Job
PATH = 'C:\\Users\\prana\\OneDrive\\Documents\\pyApps\\Web-Scrapper-Organised\\Website-Scrapped\\chromedriver.exe'






service = Service(executable_path=PATH)

driver = webdriver.Chrome(service=service)

driver.get('https://careers.oracle.com/en/sites/jobsearch/jobs')

positonName = input("Enter the position name: ")
try: 
    SearchBox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'keyword')))
    SearchBox.send_keys(positonName)
except:
    print("No Results Found")
    driver.quit()
try:    
    FindBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div > div > div > div:nth-child(1) > div > div:nth-child(1) > div > div > div > div.component-styling-wrapper-124055 > div > button')))
    FindBox.click()
except:
    print("No FindBox Found. PLS Try Again!!")
    driver.quit()

try:
    NoSearchResult = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'search-no-results__header')))
    driver.quit()
except:
    # if NoSearchResult:
    pass
    
# search-no-results__header #no search result classs
time.sleep(5)

for i in range(3):
    try:
        MoreResultbutton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div > div > div.search-pagination > button')))
        MoreResultbutton.click()
        time.sleep(3)
    except:
        driver.quit()

try:
    JobCard = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'[data-qa="searchResultItem"]')))
except:
    print("No Job Card found on Oracle Careers")
    driver.quit()
# print(JobCard)

JOBS = []

for job in JobCard:
    try:
        # JobLocations = job.find_elements(By.CSS_SELECTOR, '.job-list-item__job-info-value')
        Joblocation = WebDriverWait(job, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'job-list-item__job-info-value')))

        # JobTitles = job.find_elements(By.CLASS_NAME, 'job-tile__title')
        JobTitle = WebDriverWait(job, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'job-tile__title')))
        # print(len(JobTitles)==len(jobLocations))
        # JobDescription = job.find_elements(By.CLASS_NAME,'job-grid-item__description')
        JobDescription = WebDriverWait(job, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'job-grid-item__description')))
        # JobLinks = job.find_elements(By.CSS_SELECTOR, '.job-grid-item__link')
        JobLink = WebDriverWait(job, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'job-grid-item__link'))).get_attribute('href')
    except:
        print("Something Went Wrong!!!!!")
        driver.quit()


    
    JOBS.append(Job(name=JobTitle.text, location=Joblocation.text, href=JobLink, description=JobDescription.text))
    # print()
    # print()
    # print('#####################')
    # print()
    # print("Position Name: "+JobTitle.text)
    # print("Job Location: "+Joblocation.text)
    # print('Job Description: ')
    # print(JobDescription.text)
    # print("href: "+JobLink)
    # print()
    # print('#####################')
    # print()
    # print()

# for job in JobCard:
#     print(job.text)


for job in JOBS:
    job.DispInfoCorrectly()



input("Press ENTER to Exit")

driver.quit()



