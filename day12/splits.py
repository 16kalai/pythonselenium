

from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#launch
import time
driver = Chrome(ChromeDriverManager().install())
driver.get("https://www.Amazon.in/")
time.sleep(5)
#maximize
driver.maximize_window()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']").send_keys("lenovo thinkpad e14",Keys.ENTER)
time.sleep(5)
driver.find_element_by_xpath("//*[@id='search']/div[1]/div/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/div[2]/div[2]/div/div/div[1]/h2/a/span").click()
time.sleep(5)
driver.find_element_by_id("//*[@id='add-to-cart-button']").click()
time.sleep(5)