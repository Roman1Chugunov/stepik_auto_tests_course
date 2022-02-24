import os
import time
from selenium import webdriver

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'upload.txt')
    first_name = browser.find_element_by_css_selector("[name='firstname']")
    last_name = browser.find_element_by_css_selector("[name='lastname']")
    email = browser.find_element_by_css_selector("[name='email']")
    submit_button = browser.find_element_by_css_selector("[type='submit']")
    input_file = browser.find_element_by_id("file")

    first_name.send_keys("Ivan")
    last_name.send_keys("Ivanov")
    email.send_keys("a@a.a")
    input_file.send_keys(file_path)
    submit_button.click()

finally:
    time.sleep(1)
    browser.quit()