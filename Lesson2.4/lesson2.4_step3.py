from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    url = "http://suninjuly.github.io/wait1.html"
    browser.get(url)
    verify_button = browser.find_element(By.ID, "verify")
    verify_button.click()
    verify_message = browser.find_element(By.ID, "verify_message")
    message_text = verify_message.text
    assert "successful" in verify_message.text

finally:
    time.sleep(1)
    browser.quit()
