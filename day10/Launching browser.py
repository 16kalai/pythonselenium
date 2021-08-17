###
# Browser = chrome, firefox, ie, safari
# selenium is a bridge b/w python and browser
# every browser has separate driver
# chromedriver, gekodriver, Iedriver, safari
#

from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#launch
import time
driver = Chrome(ChromeDriverManager().install())
driver.get("https://www.redbus.in/")
time.sleep(5)
#maximize
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.page_source)
print(driver.)
time.sleep(5)
#driver.find_element_by_name("q").send_keys("python jobs in india",Keys.ENTER)
#close
driver.quit()

