from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    # Arrange
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/selects1.html"

    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    select = Select(browser.find_element_by_id("dropdown"))
    submitBtn = browser.find_element_by_css_selector("button.btn")

    # Act
    
    a = int(num1.text)
    b = int(num2.text)
    c = str(a + b)
    select.select_by_value(c)
    submitBtn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
