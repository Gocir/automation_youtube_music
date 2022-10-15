from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://music.youtube.com/")
print("Successfully Open Youtube Music")
driver.find_element(By.XPATH, '//*[@id="layout"]/ytmusic-nav-bar/div[2]/ytmusic-search-box').click()
driver.find_element(By.ID, 'input').send_keys("Tolong")
driver.find_element(By.ID, 'input').send_keys(Keys.Enter)
print("Successfully Search Music")
