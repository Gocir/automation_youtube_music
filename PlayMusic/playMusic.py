from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://music.youtube.com/")
print("Successfully Open Youtube Music")
driver.find_element(By.XPATH, '//*[@id="items"]/ytmusic-responsive-list-item-renderer[1]')
driver.find_element(By.ID, 'play-button').click()
print("Successfully Play Music on the First List Item")
