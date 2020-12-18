from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


link = 'http://suninjuly.github.io/math.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element_by_id('robotsRule')

    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked == 'true', "People radio is not selected by default"

except NoSuchElementException as e:
    print(f'Test failed - {e.msg}')
    assert False
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
