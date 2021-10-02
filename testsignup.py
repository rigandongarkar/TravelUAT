
from selenium import webdriver
driver = webdriver.Chrome(executable_path="E:\\python selenium\\chromedriver_win32\\chromedriver")
driver.get("https://www.phptravels.net/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_link_text("Signup").click()
driver.find_element_by_name("first_name").send_keys("firstname")
driver.find_element_by_name("last_name").send_keys("lastname")
driver.find_element_by_name("phone").send_keys("9988778855")
driver.find_element_by_name("email").send_keys("asssmm@mail.com")
driver.find_element_by_name("password").send_keys("wwda121")
# driver.find_element_by_xpath("//span[@title='Customer']").click()
driver.find_element_by_xpath("//button[@type='submit']").click()
successtext = driver.find_element_by_xpath("//div[contains(@class,'alert-success signup')]").text
print(successtext)
driver.find_element_by_link_text("Home").click()