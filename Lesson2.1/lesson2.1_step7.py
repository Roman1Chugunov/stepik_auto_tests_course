from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_id("treasure")
    input = browser.find_element_by_id("answer")
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robots_rule_radiobutton = browser.find_element_by_id("robotsRule")
    people_rule_radiobutton = browser.find_element_by_id("peopleRule")

    x = treasure.get_attribute("valuex")
    y = calc(x)
    input.send_keys(y)
    robot_checkbox.click()
    robots_rule_radiobutton.click()


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()