from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    required_input1 = browser.find_element_by_css_selector("[placeholder = 'Input your first name']")
    required_input1.send_keys("Ivan")
    required_input2 = browser.find_element_by_css_selector("[placeholder = 'Input your last name']")
    required_input2.send_keys("Petrov")
    required_input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
    required_input3.send_keys("1@gmail.com")

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    time.sleep(2)

    actual_text = browser.find_element_by_tag_name('h1').text
    expected_title = 'Congratulations! You have successfully registered!1'
    if actual_text == expected_title:
        print('все ок')
        assert True
    else:
        print('проблемы')
        assert False
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
