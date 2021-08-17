import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Ie(executable_path="E:\Python\IEDriverServer_Win32_3.150.1\IEDriverServer")

driver.get("https://www.airtel.com/")

driver.close()
driver.quit()
# time.sleep(5)
# driver.find_element_by_name("q").send_keys("ball")
