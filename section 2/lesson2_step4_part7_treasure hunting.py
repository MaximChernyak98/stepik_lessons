from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import math

link = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_image = browser.find_element_by_id('treasure')
    x_value = treasure_image.get_attribute("valuex")
    result = calc(x_value)

    answer_field = browser.find_element_by_css_selector('#answer')
    answer_field.send_keys(result)

    robot_checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    robot_checkbox.click()

    robots_rule_radiobutton = browser.find_element_by_id('robotsRule')
    robots_rule_radiobutton.click()

    submit_button = browser.find_element_by_css_selector('button.btn.btn-default')
    submit_button.click()

    time.sleep(5)

except NoSuchElementException as e:
    print(f'Test failed - {e.msg}')
    assert False
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
