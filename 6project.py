#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from urllib.request import urlopen
from selenium import webdriver
import time
import bs4 as bs

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver .chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 

url = "https://yoshops.com/products/reliance-jio-phone1"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()

#review button
time.sleep(10)
button = driver.find_elements(By.CSS_SELECTOR, "div.yotpo-default-button[role='button']")
button[1].click()

#ratings
time.sleep(10)
rating = driver.find_element(By.CSS_SELECTOR, "span[data-score='5'][role='radio']")
rating.click()

#title
time.sleep(10)
title = driver.find_element(By.CSS_SELECTOR, "input[name = 'review_title']")
title.send_keys('Thankyou')

#review
time.sleep(10)
review = driver.find_element(By.CSS_SELECTOR, "textarea[name = 'review_content']")
review.send_keys('Thankyou for your feedback')

#name
time.sleep(10)
review = driver.find_element(By.CSS_SELECTOR, "input[name = 'display_name']")
review.send_keys('Khushi')

#email
time.sleep(10)
review = driver.find_element(By.CSS_SELECTOR, "input[name = 'email']")
review.send_keys('khushishukla898@gmail.com')

#post button
time.sleep(10)
post = driver.find_element(By.CSS_SELECTOR, "input[data-button-type='submit']")
post.click()

print("Reviewed the product Succesfully!")

#product detail
details=driver.find_elements(By.XPATH,"//div[@class='peekaboo-inner clearfix']")
product_details=[]
for p in details:
    product_details.append(p.text)


#customer review
cus = driver.find_elements(By.XPATH,"//*[@class='content-review']")
review=[]
for r in cus:
    review.append(r.text)
while '' in review:
    review.remove('')

#customer name
cus_name = driver.find_elements(By.XPATH,"//span[contains(@class,'y-label yotpo-user-name yotpo-font-bold pull-left')]")
name=[] # contains - all such web elements whose value can change
for n in cus_name:
    name.append(n.text)
while '' in name:
    name.remove('')
    
names = driver.find_elements(By.XPATH,"//*[@id='product-name']")
product_name=[]
for n in names:
    product_name.append(n.text)
    
df1=pd.DataFrame()
df2=pd.DataFrame()
df3=pd.DataFrame()
df4=pd.DataFrame()

df1['product_name']=product_name
df2['product_details']=product_details
df3['customer_name']=name
df4['customer_review']=review

file_name = pd.ExcelWriter("product.xlsx", engine='xlsxwriter')
df1.to_excel(file_name,sheet_name='sheet1',index=False)
df2.to_excel(file_name,sheet_name='sheet1',index=False,startcol=1)
df3.to_excel(file_name,sheet_name='sheet1',index=False,startcol=2)
df4.to_excel(file_name,sheet_name='sheet1',index=False,startcol=3)
file_name.save()
time.sleep(10)


# In[ ]:




