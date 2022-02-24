from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    url = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(url)
    trollface = browser.find_element(By.CLASS_NAME, "trollface")
    trollface.click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    presented_integer = browser.find_element_by_id("input_value")
    x = presented_integer.text
    y = calc(x)
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(y)
    submit_button = browser.find_element_by_css_selector("[type = 'submit']")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
