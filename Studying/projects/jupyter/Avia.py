#!/usr/bin/env python
# coding: utf-8

# In[20]:


from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = webdriver.FirefoxOptions()
options.page_load_strategy = 'eager'
browser = Firefox(options=options)


# In[ ]:





# In[21]:


browser.get('https://www.aviasales.ru')
sleep(5)
try:
    cookies = browser.find_element(By.XPATH,'//*[@data-test-id="accept-cookies-button"]')
    cookies.click()
except:
    print('Cookies не найдены')
    


# In[22]:


city_from = browser.find_element(By.ID,'avia_form_origin-input')
city_from.clear()
city_from.send_keys('Москва')


# In[23]:


city_to = browser.find_element(By.ID,'avia_form_destination-input')
city_to.clear()
city_to.send_keys('Казахстан')


# In[24]:


browser.find_element(By.XPATH,'//*[@data-test-id="start-date-field"]').click()


# In[25]:


# date = browser.find_element(By.CLASS_NAME,'s__NhCGXhDOELgUyu3f7gUv').find_element(By.XPATH,'//*[@aria-disabled="false"]')


# In[26]:


# date.find_element(By.CLASS_NAME,'s__ta_SSbfNo_PsQ7Rdf70_').text


# In[27]:


# try:
#     date.find_element(By.CLASS_NAME,'s__lY97GtsPAyCOrUnAm4_M')
    
# except:
#     print('Информация не найдена')


# In[2]:


# Xpath_today = '//*[@class = "s__NhCGXhDOELgUyu3f7gUv boundedFrom selected today"]'
# today = browser.find_element(By.CLASS_NAME,'s__NhCGXhDOELgUyu3f7gUv ')
Xpath ='//*[@class="s__NhCGXhDOELgUyu3f7gUv "]'
data = browser.find_elements(By.XPATH,Xpath)
dates = []
for element in data:
    date = element.get_attribute('aria-label')
    price = element.find_element(By.CLASS_NAME,'s__wRhMOEwg2Ub7G1CotYcY').text
    dates.append([date,price])
    # print(date,price.decode()+'RUB')
# a='13\u202f687'
# print(type(a))
# print(a)
# lst = ['10']
# lst.append(a)

# print(lst)


new_dates = []
for date in dates:
    price = ''.join(date[1].split())
    price = int(price)
    if price < 10000:
        new_dates.append([date[0],price])


for date in new_dates:
    print(date)


# In[ ]:


# dates = [date.find_element(By.XPATH,'//*[@aria-disabled="false"]')]
# dates


# In[ ]:


# try:
#     for date in dates:
#         data_day = date.find_element(By.CLASS_NAME,'s__ta_SSbfNo_PsQ7Rdf70_').get_attribute("data-test-id")
#         data_pay = date.find_element(By.CLASS_NAME,'s__wRhMOEwg2Ub7G1CotYcY').text
#         # data_pay = int(data_pay)
#         print(data_day,data_pay,' RUB')
# except:
#     print('Информация не найдена')


# In[ ]:


# dates


# In[ ]:




