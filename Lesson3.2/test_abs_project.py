import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    def test_registration_form1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        correct_welcome_text = "Congratulations! You have successfully registered!"

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
        first_name.send_keys("Ivan")
        last_name = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
        last_name.send_keys("Ivanov")
        email = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
        email.send_keys("a@a.a")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual (correct_welcome_text, welcome_text,
        f"Welcome text should be 'Congratulations! You have successfully registered!', not '{welcome_text}'")

    def test_registration_form2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        correct_welcome_text = "Congratulations! You have successfully registered!"


        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector('input[placeholder="Input your name"]')
        first_name.send_keys("Ivan")
        last_name = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
        last_name.send_keys("Ivanov")
        email = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
        email.send_keys("a@a.a")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual (correct_welcome_text, welcome_text,
        f"Welcome text should be 'Congratulations! You have successfully registered!', not '{welcome_text}'")

if __name__ == "__main__":
    unittest.main()
