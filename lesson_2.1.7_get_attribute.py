from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element1 = browser.find_element_by_css_selector("#treasure")
    x = x_element1.get_attribute("valuex")
    
    y = calc(x)

    input2 = browser.find_element_by_css_selector("#answer")
    input2.send_keys(y)
    
    # Кликаем чекбокс
    checkBox = browser.find_element_by_css_selector("#robotCheckbox")
    checkBox.click()

    # Кликаем радиобаттон
    radioButton = browser.find_element_by_css_selector("#robotsRule")
    radioButton.click()

    # Кликаем Submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()