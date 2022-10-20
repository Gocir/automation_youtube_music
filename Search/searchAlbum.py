from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://music.youtube.com/")
print("Successfully Open Youtube Music")
driver.find_element(By.TAG_NAME, 'ytmusic-search-box').click()
driver.find_element(By.TAG_NAME, 'input').send_keys("Dunia Batas")
driver.find_element(By.TAG_NAME, 'input').send_keys(Keys.ENTER)
print("Successfully Search Album")
