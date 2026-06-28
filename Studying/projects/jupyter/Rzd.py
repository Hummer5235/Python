#!/usr/bin/env python
# coding: utf-8

# In[202]:


from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep


# date = int(input('Введите дату: ')) 
# month = int(input('Введите месяц: '))
date = 12
month = 2
# city_from = input('Введите город отправления: ').capitalize()
# city_to = input('Введите город прибытия: ').capitalize()
city_from = 'Краснодар'
city_to = 'Москва'
trains = []


# In[203]:


browser = Firefox()
browser.implicitly_wait(5)


# In[204]:


browser.get('https://www.rzd.ru/')


# In[205]:


coockie_button = browser.find_element(By.CLASS_NAME,'cookie-alert__btn')


# In[206]:


if coockie_button:
    coockie_button.click()


# In[207]:


browser.find_element(By.XPATH,'//input[@id="direction-from"]').send_keys(f'{city_from}')


# In[208]:


browser.find_element(By.XPATH,f'//li[@aria-label="{city_from}"]').click()


# In[209]:


browser.find_element(By.XPATH,'//input[@id="direction-to"]').send_keys(f'{city_to}')


# In[210]:


browser.find_element(By.XPATH,f'//li[@aria-label="{city_to}"]').click()


# In[211]:


browser.find_element(By.XPATH,f'//*[@id="datepicker-from"]').click()


# In[212]:


browser.find_element(By.XPATH,f'//td[@data-day="{date}"][@data-month="{month-1}"]').click()
browser.find_element(By.XPATH,'//a[@aria-label="Найти маршруты"]').click()


# In[213]:


# browser.find_element(By.CLASS_NAME,"icon-only--md").click()
# browser.find_element(By.CLASS_NAME,'header__label').click()


# In[214]:


# browser.find_element(By.XPATH,f'//input[@aria-label="Изменить дату отправления."]').clear()
# browser.find_element(By.XPATH,f'//input[@aria-label="Изменить дату отправления."]').send_keys(f'{date}.0{month}.2024')

# browser.find_element(By.XPATH,'//*[@aria-label="Найти новый маршрут, при условии изменения поиска."]').click()
# sleep(3)
# soup = BeautifulSoup(browser.page_source,'lxml')
# card_list = soup.find('Tavriya_poezda-search-results-card-list',class_='ng-star-inserted').find_all('div',class_='container')


# In[ ]:





# In[ ]:





# In[215]:


for i in range(10):
    sleep(3)
    browser.find_element(By.CLASS_NAME,"icon-only--md").click()
    browser.find_element(By.XPATH,f'//input[@aria-label="Изменить дату отправления."]').clear()
    browser.find_element(By.XPATH,f'//input[@aria-label="Изменить дату отправления."]').send_keys(f'{date}.0{month}.2024')
    browser.find_element(By.CLASS_NAME,'header__label').click()
    browser.find_element(By.XPATH,'//*[@aria-label="Найти новый маршрут, при условии изменения поиска."]').click()
    sleep(3)
    soup = BeautifulSoup(browser.page_source,'lxml')
    card_list = soup.find('Tavriya_poezda-search-results-card-list',class_='ng-star-inserted').find_all('div',class_='container')
    for number,value in enumerate(card_list):
        title = card_list[number].find('div',class_='fade-out__content').text
        dates = card_list[number].find_all('div',class_='card-route__date')
        dates  = [date.text for date in dates]
        start_date, end_date = dates
        times = card_list[number].find_all('div',class_='card-route__time')
        times = [element.text.strip() for element in times]
        start_time,end_time = times
        trains.append([title,start_date+start_time,end_date+end_time])
    date+=1


# In[216]:


for train in trains:
    print(train)


# In[ ]:




