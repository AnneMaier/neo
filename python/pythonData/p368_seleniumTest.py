from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

print(type(driver))

print("-"  * 50)
print("Go Google~!")

url = "https://www.google.com"
driver.get(url)

search_textbook = driver.find_element(By.NAME, "q")

word = 'selenium'

search_textbook.send_keys(word)
search_textbook.submit()

wait = 30
print(str(wait) + ' seconds later...')
time.sleep(wait)

imagefile = 'p368_seleniumTest.png'
driver.save_screenshot(imagefile)
print(imagefile + ' saved')

wait = 3
driver.implicitly_wait(wait)

driver.quit()
print('Browser closed')