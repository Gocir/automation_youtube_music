from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://music.youtube.com/")
print("Successfully open YouTube Music")
driver.find_element(By.XPATH, '//*[@id="layout"]/ytmusic-nav-bar/div[2]/ytmusic-pivot-bar-renderer/ytmusic-pivot-bar-item-renderer[2]').click()
print("Successfully open the Explore page")
driver.find_element(By.TAG_NAME, 'ytmusic-carousel')
driver.find_element(By.XPATH, '//*[@id="items"]/ytmusic-two-row-item-renderer[1]')
driver.find_element(By.ID, 'play-button').click()
print("Successfully play album")
