from selenium import webdriver
import time
option=webdriver.ChromeOptions()
option.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(chrome_options=option)
driver.get("https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html")
# page=driver.find_element_by_xpath("//div[@class='btn-to-get-doc stop-propagation']")
# js="window.scrollTo(100,1200);"
# driver.execute_script(js)
# time.sleep(3)
read=driver.find_element_by_xpath("//div[@class='foldpagewg-text']")
# driver.execute_script('arguments[0].scrollIntoView();',read[-1])
js="window.scrollTo(100,1200);"
driver.execute_script(js)
read.click()
time.sleep(3)
# driver.execute_script('arguments[0].scrollIntoView();', page)
# read.click()
