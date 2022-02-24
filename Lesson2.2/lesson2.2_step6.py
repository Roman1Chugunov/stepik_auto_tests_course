from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    input = browser.find_element_by_id("answer")
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robots_rule_radiobutton = browser.find_element_by_id("robotsRule")
    people_rule_radiobutton = browser.find_element_by_id("peopleRule")

    x = x_element.text
    y = calc(x)
    input.send_keys(y)
    robot_checkbox.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule_radiobutton)
    robots_rule_radiobutton.click()


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()