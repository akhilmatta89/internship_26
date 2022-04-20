import selenium
import pandas as pd
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.naukri.com/')
role_search = driver.find_element_by_class_name('suggestor-input ')
role_search.send_keys('Data Analyst')
location_search = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[3]/div/div/div/input')
location_search.send_keys('Bangalore')
serach_path = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[6]')
serach_path.click()
title = []
company = []
experience = []
location = []

title_tag = driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")[0:10]
for ttl in title_tag:
    title.append(ttl.text)
company_tag = driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")[0:10]
for cmpny in company_tag:
    company.append(cmpny.text)
exp_tag = driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']/span[1]")[0:10]
for exp in exp_tag:
    experience.append(exp.text)
location_tag = driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span[1]")[0:10]
for lctn in location_tag:
    location.append(lctn.text)
# print(len(title))
# print(len(company))
# print(len(experience))
# print(len(location))
df = pd.DataFrame({'Title':title,'Company':company,'Experience':experience,'Location':location})
df