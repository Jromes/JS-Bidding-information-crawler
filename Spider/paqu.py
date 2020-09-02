#!/usr/bin/env Python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import os
import time
import re

weblist_chd_list = []
result_list = []
#chrome_options = Options()
#chrome_options.add_argument("--headless")
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome()
driver.get("http://njggzy.nanjing.gov.cn/njweb/fjsz/068002/buildService2.html")


#above = driver.find_element_by_xpath('//*[@id="dummybodyid"]/div[2]/div[2]/div/div[2]/div/div[1]/span[1]')
#above = driver.find_elements_by_class_name('ewb-comp-tt l')
#ActionChains(driver).move_to_element(above).perform()
#print(driver.find_element_by_xpath("//div[@class='ewb-comp-hd clearfix']"))


#print(driver.find_element_by_xpath('//*[@id="dummybodyid"]/div[2]/div[2]/div/div[2]/div/div[1]/span[1]').text)
#print(driver.find_elements_by_class_name('ewb-comp-tt l'))

#print(find_element(By.XPATH,".//*[@id='Title"))
#bnge1 = driver.find_elements_by_class_name('ewb-comp-tt l')
#print(driver.find_elements_by_css_selector('#iframe068002002 > ul'))
#bnge = (driver.find_elements_by_css_selector('#iframe068002002 > ul'))
#print(driver.page_source)

bnge=driver.find_element_by_xpath("//span[@data-target='tab-bb']")
ActionChains(driver).move_to_element(bnge).perform()
driver.find_element_by_xpath("//input[@id='keyword']").send_keys("监理")
click_point=driver.find_element_by_xpath("//button[@onclick='searchlistfjsz();']")
ActionChains(driver).click(click_point).perform()
# =============================================================================
# js_1 = "document.getElementById(\"showList\").style.display='block';"
# driver.execute_script(js_1)
# js_1 = "document.getElementById(\"showList\").style.display='block';"
# driver.execute_script(js_1)
# =============================================================================

website_list_1=driver.find_elements_by_xpath('//li[@class="ewb-info-item2 clearfix yclist"]')

# =============================================================================
# for i in range(1,2):
#     board_en=pa.findall(board[i].text)
#     result.append([str(board_en[-1]),int(ol_num[i].text)])
# =============================================================================
#time.sleep(3) 
#print(len(website_list_1))
# =============================================================================
# link = driver.find_element_by_xpath('//*[@id="showList"]').is_displayed()
# print(link)
# =============================================================================
# =============================================================================
# print("---------------")
# print(website_list_1[0].get_attribute('onclick'))
# print("---------------")
# # print(website_list_2.get_attribute('onclick'))
# print(website_list_2.get_attribute('innerText'))
# print("---------------")
# print(website_list_2.get_attribute('textContent'))
# print("---------------")
# print(website_list_2.get_attribute('innerHTML'))
# print("---------------")
# print(driver.page_source)
# drivepagesource=driver.page_source
# pattern = re.compile(r'onclick=\"window.open(\'[.+?]\');', re.I)
# m = pattern.match(driver.page_source)
# =============================================================================
#print(m.group(1))
#ActionChains(driver).click(website_list_2).perform()
time.sleep(3)
with open("test.txt","w",encoding='utf-8') as f:
        f.write(driver.page_source) 

with open("test.txt", "r",encoding='utf-8') as f:  # 打开文件
    drivepagesource_1 = f.read()  # 读取文件
    # print(drivepagesource_1)


drivepagesource=driver.page_source
weblist_1 = re.findall(r'onclick=\"window.open\(\'(.+?)\'\);', drivepagesource)

next_page_click_point=driver.find_element_by_xpath("//a[@class='next ewb-fan']")
ActionChains(driver).click(next_page_click_point).perform()


#with open("test.txt","w",encoding='utf-8') as f:
#        f.write(driver.page_source) 
time.sleep(3)                                          
driver.close()

