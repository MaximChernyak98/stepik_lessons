from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    required_input1 = browser.find_element_by_css_selector(".form-control.first[required]")
    required_input1.send_keys("Ivan")
    required_input2 = browser.find_element_by_css_selector(".form-control.second[required]")
    required_input2.send_keys("Petrov")
    required_input3 = browser.find_element_by_css_selector(".form-control.third[required]")
    required_input3.send_keys("1@gmail.com")

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    time.sleep(4)

    actual_text = browser.find_element_by_tag_name('h1').text
    expected_title = 'Congratulations! You have successfully registered!'

    if actual_text == expected_title:
        print('Test passed')
        assert True
    else:
        print('Test failed - headers do not match')
        assert False

except NoSuchElementException as e:
    print(f'Test failed - {e.msg}')
    assert False
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
