
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://icarro-v1.netlify.app/search?page=0&size=10")
    subtitle = driver.find_element(By.CSS_SELECTOR, "[class*="Type your data and hit Yalla!"]")
    start_sub = driver.find_element(By.CSS_SELECTOR, "[Type your data]")
finally:
    driver.quit()