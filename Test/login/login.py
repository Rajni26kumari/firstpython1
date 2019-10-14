import requests
from selenium import webdriver
import urllib.request
import time
from bs4 import BeautifulSoup
url = 'https://devicemon.azurewebsites.net'
driver = webdriver.Chrome("E:/chromedriver/chromedriver.exe")
driver.implicitly_wait(10)
driver.get(url)
driver.find_element_by_xpath("//*[@id='i0116']").send_keys("test.ncadminuser@ha-efbops.com")
driver.find_element_by_id("idSIButton9").click()
driver.find_element_by_xpath("//*[@id='i0118']").send_keys("nathcorp!1")
time.sleep(4)
driver.find_element_by_id("idSIButton9").click()
driver.find_element_by_id("idSIButton9").click()
driver.find_element_by_id("TableSearch").send_keys("014269671953")
soup = BeautifulSoup(driver.page_source,'html.parser')
#print(soup.extract())
#to find the title value
title_element= driver.find_elements_by_xpath("//th[@class='col-xs-1 small text-center bold sorting_asc' or @aria-controls= 'PIDTable']")
title = [x.text for x in title_element]

print('title:')
print(title)
#find the lower value
value_element= driver.find_elements_by_xpath("//*[@id='PidDetail']/tr/td")
value= [x.text for x in value_element]
print('value:')
print(value,'\n')

for title,value in zip(title,value):
    print(title+':'+value)
'''
for values in soup.findAll("tr"):
    for data in values.findAll("th",{'aria-controls': 'PIDTable'}):
        print(data.text)
'''





#driver.close()