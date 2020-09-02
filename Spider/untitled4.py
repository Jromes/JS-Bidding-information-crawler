
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
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("http://njggzy.nanjing.gov.cn/njweb/fjsz/068002/buildService2.html")


bnge=driver.find_element_by_xpath("//span[@data-target='tab-bb']")
ActionChains(driver).move_to_element(bnge).perform()
driver.find_element_by_xpath("//input[@id='keyword']").send_keys("监理")
click_point=driver.find_element_by_xpath("//button[@onclick='searchlistfjsz();']")
ActionChains(driver).click(click_point).perform()

for j in range(10):
    if j==0:
        ange=driver.find_element_by_xpath("//span[@data-target='tab-aa']")
        ActionChains(driver).move_to_element(ange).perform()
    
        ActionChains(driver).move_to_element(bnge).perform()
        time.sleep(1)    


    website_list_1=driver.find_elements_by_xpath('//li[@class="ewb-info-item2 clearfix yclist"]')
    

    
    # print('=============================================================1:')
    # print(driver.current_window_handle)        # 用于获取当前窗口句柄
    drivepagesource=driver.page_source
    weblist_1 = re.findall(r'onclick=\"window.open\(\'(.+?)\'\);', drivepagesource)
    now_window=driver.current_window_handle
    # for i in range(len(weblist_1)):
    for i in range(len(weblist_1)):
        webadd = "http://njggzy.nanjing.gov.cn/"+weblist_1[i]
        shuju=[]
        suoyou = driver.window_handles
        driver.switch_to_window(suoyou[0])
        js = "window.open('"+webadd+"')"
        driver.execute_script(js)

    
        drivepagesource_chd=driver.page_source
    
        suoyou = driver.window_handles
        driver.switch_to_window(suoyou[len(suoyou)-1])   
        project_name=driver.find_element_by_xpath('//div[@class="article-info"]/h1')
# =============================================================================
#         print(project_name.text)
#         print("===================================")
# =============================================================================
        
        lblBiaoDuanNo=driver.find_element_by_xpath('//span[@id="lblBiaoDuanNo"]')
        # print(lblBiaoDuanNo,type(lblBiaoDuanNo))
        lblBiaoDuanNo
        try:
            biaoduan_price=driver.find_element_by_xpath('//span[@id="Hx_BaoJia1"]')

        except:
            biaoduan_price=driver.find_element_by_xpath('//span[@id="lblZhongBiaoPrice"]')

        finally:
            print("===================================")
    
            
        pingbian_way=driver.find_element_by_xpath('//span[@id="lblPingBiaoBanFa"]')

        
        shuju=[lblBiaoDuanNo.text,project_name.text,pingbian_way.text,biaoduan_price.text]
        # result_list.append(shuju)
# =============================================================================
#         print('=============================================================:')
#         print(driver.current_window_handle)        # 用于获取当前窗口句柄
# =============================================================================
        
        # time.sleep(2) 
        suoyou = driver.window_handles
        driver.switch_to_window(suoyou[len(suoyou)-1])    
# =============================================================================
#         print(suoyou)
#         print('=============================================================:')
#         print(driver.current_window_handle)        # 用于获取当前窗口句柄       
# =============================================================================
        driver.close()
        # time.sleep(2)
        driver.switch_to_window(suoyou[0])


        js = "window.open('http://njggzy.nanjing.gov.cn/njweb/fjsz/buildService1.html')"
        
        driver.execute_script(js)
        suoyou = driver.window_handles
        driver.switch_to_window(suoyou[len(suoyou)-1])  
        cnge=driver.find_element_by_xpath("//span[@data-target='tab-bb']")
        dnge=driver.find_element_by_xpath("//span[@data-target='tab-aa']")
        # time.sleep(2)
        ActionChains(driver).move_to_element(cnge).perform()
        # time.sleep(2)
        ActionChains(driver).move_to_element(dnge).perform()
        # time.sleep(2)
        driver.find_element_by_xpath("//input[@id='keyword']").send_keys(shuju[0])
        click_point=driver.find_element_by_xpath("//button[@onclick='searchlistfjsz();']")
        ActionChains(driver).click(click_point).perform()

        ActionChains(driver).move_to_element(cnge).perform()
        ActionChains(driver).move_to_element(dnge).perform()
        time.sleep(1)
        website_list_1=driver.find_element_by_xpath('//li[@class="ewb-info-item2 clearfix yclist"]')
        ActionChains(driver).click(driver.find_element_by_xpath('//li[@class="ewb-info-item2 clearfix yclist"]')).perform()
        suoyou = driver.window_handles
        driver.switch_to_window(suoyou[len(suoyou)-1])  
        drivepagesource_chd_2 = driver.page_source
        # weblist_1 = re.findall(r'onclick=\"window.open\(\'(.+?)\'\);', drivepagesource_chd_2)
        gusuan_price = re.findall(r'监理合同估算价：<span>(.+?)</span>', drivepagesource_chd_2)
        # print(gusuan_price[0])
        shuju.append(gusuan_price[0])
        result_list.append(shuju)
        suoyou = driver.window_handles
        for k in range(len(suoyou)-1):
            # print("123=============================")
            # print(k)
            # print(len(suoyou)-k)
            driver.switch_to_window(suoyou[len(suoyou)-k-1])
            driver.close()
        
# =============================================================================
#         with open("test.txt","w",encoding='utf-8') as f:
#             f.write(drivepagesource_chd_2) 
# =============================================================================
    suoyou = driver.window_handles
    driver.switch_to_window(suoyou[0])
    next_page_click_point=driver.find_element_by_xpath("//a[@class='next ewb-fan']")
    ActionChains(driver).click(next_page_click_point).perform()
    
    
    time.sleep(1)                                          
driver.quit()