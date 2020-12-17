from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import math

link = 'http://suninjuly.github.io/math.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#input_value')
    x_value = x_element.text
    result = calc(x_value)

    answer_field = browser.find_element_by_css_selector('#answer')
    answer_field.send_keys(result)

    robot_checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    robot_checkbox.click()

    robots_rule_radiobutton = browser.find_element_by_css_selector('[for="robotsRule"]')
    robots_rule_radiobutton.click()

    submit_button = browser.find_element_by_css_selector('button.btn.btn-default')
    submit_button.click()

    time.sleep(4)

except NoSuchElementException as e:
    print(f'Test failed - {e.msg}')
    assert False
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
