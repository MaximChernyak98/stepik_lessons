from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import math

link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element_by_id("peopleRule")
    is_people_checked = people_radio.get_attribute('checked')
    print('value of people radio: ', is_people_checked)
    assert is_people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element_by_id("robotsRule")
    is_robots_checked = robots_radio.get_attribute('checked')
    assert is_robots_checked is None

    time.sleep(2)

except NoSuchElementException as e:
    print(f'Test failed - {e.msg}')
    assert False
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
