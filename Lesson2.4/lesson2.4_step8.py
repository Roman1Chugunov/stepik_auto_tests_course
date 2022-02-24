from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 12 секунд
    browser.implicitly_wait(13)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    wait_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    book = browser.find_element(By.ID, "book")
    book.click()
    # решаем задачку
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
