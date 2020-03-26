from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com")
driver.maximize_window()

print(driver.find_element(By.PARTIAL_LINK_TEXT, "California Real Estate").click())
print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))
assert "California Real Estate" in driver.title
print(driver.title)
driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]")
driver.find_element(By.NAME, "g2-name").send_keys("abc")
driver.find_element(By.NAME, "g2-email").send_keys("1@r.com")
driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "go back").click()
assert "California Real Estate" in driver.title
print(driver.title)




driver.close()