from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x, y):
      return str(int(x) + int(y))

    x_element1 = browser.find_element_by_css_selector("#num1")
    x = x_element1.text

    y_element1 = browser.find_element_by_css_selector("#num2")
    y = y_element1.text
    
    z = calc(x, y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)

    # Кликаем Submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()