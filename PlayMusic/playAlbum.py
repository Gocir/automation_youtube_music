from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://music.youtube.com/")
print("Successfully Open Youtube Music")
driver.find_element(By.XPATH, '//*[@id="layout"]/ytmusic-nav-bar/div[2]/ytmusic-pivot-bar-renderer/ytmusic-pivot-bar-item-renderer[2]').click()
print("Successfully Open Explore page")
driver.find_element(By.XPATH, '//*[@id="items"]/ytmusic-two-row-item-renderer[1]')
driver.find_element(By.ID, 'play-button').click()
print("Successfully Play Album on the First List Item")
