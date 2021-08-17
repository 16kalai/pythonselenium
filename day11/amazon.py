# launching browser
#print screen shot, image, url, html
#


from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#launch
import time
driver = Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.com/")
#print (driver.title)        #print title
time.sleep(5)
#maximize
driver.maximize_window()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']").send_keys("lenovo thinkpad e14")
time.sleep(5)
#search button
driver.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()
#selecting
driver.find_element_by_xpath("//*[@id='p_n_cpf_eligible/21512497011']/span/a/div/label/i").click()
driver.save_screenshot("Amazon.png")
#close
driver.quit()