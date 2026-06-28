#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8


# In[90]:

# In[ ]:


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, ActionChains
import os
from fake_useragent import UserAgent

useragent = UserAgent()

# In[ ]:


chrome_option = webdriver.ChromeOptions()
dir_path = os.getcwd()
chrome_option.add_argument(f'user-data-dir={dir_path}/selenium')
chrome_option.add_argument(f'user-agent={useragent.random}')
chrome_option.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_option)


# In[91]:

# In[ ]:


browser.get('https://www.aviasales.ru/?params=MOWALA1')


# In[92]:

# city_from = browser.find_element(By.ID, 'avia_form_origin-input')<br>
# print(city_from)

# In[93]:

# city_from.clear()<br>
# city_from.clear()

# In[94]:

# city_from.send_keys('Москва')

# In[95]:

# city_to = browser.find_element(By.ID, 'avia_form_destination-input')<br>
# city_to.clear()<br>
# city_to.send_keys('Казахстан')

# In[96]:

# calendar = browser.find_element(By.CSS_SELECTOR,'body > div.header.--blue > div.selene-form > div > div > div > div > form > div.s__EV1p5ZE5yZ7zL3O7li9n.s__mtImpdxqmb3FtpyrTsgk.s__kGy7Tb3xVjEevcmv8PDu > div > button.s__iUCZVK_7pftNPmX5zeoS.s__IwBVpRef_1GpuUeZuKUL.s__QOH8_RMDyCm4BxeyrqOt.s__OIqaFwbhkZg2cIA5d0zJ > svg > path')

# In[ ]:


calendar = browser.find_element(By.XPATH,'//*[@class="s__iUCZVK_7pftNPmX5zeoS s__IwBVpRef_1GpuUeZuKUL s__QOH8_RMDyCm4BxeyrqOt s__OIqaFwbhkZg2cIA5d0zJ"]')
print(calendar)
calendar.click()
sleep(1)
calendar.click()


# In[97]:

# In[ ]:


dates = []
for i in range(3):
    sleep(1)
    Xpath ='//*[@class="s__NhCGXhDOELgUyu3f7gUv "]'
    data = browser.find_elements(By.XPATH,Xpath)
    for element in data:
        date = element.get_attribute('aria-label')
        price = element.find_element(By.CLASS_NAME,'s__wRhMOEwg2Ub7G1CotYcY').text
        dates.append([date,price])
    sleep(5)
    next_button = browser.find_element(By.XPATH,'//*[@class="s__iAbNIgMSL5KhwplFwsCo"]')
    next_button.click()


# In[98]:

# In[ ]:


new_dates = []
for date in dates:
    price = ''.join(date[1].split())
    price = int(price)
    if price < 11000:
        new_dates.append([date[0],price])


# In[ ]:


for date in new_dates:
    print(date)


# In[ ]:
