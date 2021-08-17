import time
from webbrowser import Chrome

from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = Chrome(ChromeDriverManager().install())
driver.get("https://support.industry.siemens.com/tf/ww/en/posts/software-libraries-sistema/184830/?page=0&pageSize=10")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='onetrust-accept-btn-handler']").click()
driver.find_element_by_xpath("//*[@id='header_loginLink']").click()
user_ele =driver.find_element_by_name("ctl00$ContentPlaceHolder1$TextSiemensLogin")
print(user_ele.is_displayed())

pass_ele =driver.find_element_by_xpath("//*[@id='ContentPlaceHolder1_TextPassword']")
print(pass_ele.is_displayed())

user_ele.send_keys("16kalai")
pass_ele.send_keys("Kalaikan1623$")
driver.find_element_by_name("ctl00$ContentPlaceHolder1$LoginUserNamePasswordButton").click()
time.sleep(3)
print(driver.title)
print(driver.current_url)
driver.close()

