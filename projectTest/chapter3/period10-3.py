# coding=utf-8

from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('http://localhost:63342/projectAutoTest/projectHtml/chapter3/period10-2.html')
driver.implicitly_wait(10)

# 切换进 iframe 结构
driver.switch_to.frame('iframeContainer')
time.sleep(1)
driver.find_element_by_id('noWindows').find_element_by_tag_name('input').click()
time.sleep(3)

driver.quit()


