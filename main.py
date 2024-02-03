from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print("Web Scrapping Assignment")

driver = webdriver.Chrome()

driver.get("https://news.ycombinator.com/")

print(driver.title)


search_input = driver.find_element(By.NAME, "q")

search_input.send_keys("sql")

search_input.send_keys(Keys.RETURN)

time.sleep(2)

search_results = driver.find_elements(By.CSS_SELECTOR, "a.Story_link")

for result in search_results:
    print(result.text)

driver.quit()