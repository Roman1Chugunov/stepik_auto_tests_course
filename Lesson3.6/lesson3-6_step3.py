import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope="module")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
class TestLesson36:
    def test_step2(self, browser, link):
        answer = math.log(int(time.time()))
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Type your answer here...']").send_keys(answer)
        browser.find_element(By.CLASS_NAME , 'submit-submission').click()
        hint_text = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
        assert hint_text == "Correct!"
