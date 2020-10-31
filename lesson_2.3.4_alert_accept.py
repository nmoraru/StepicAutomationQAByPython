from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    button = browser.find_element_by_tag_name("button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()
    
    x_element1 = browser.find_element_by_css_selector("#input_value")
    x = x_element1.text
    
    y = calc(x)

    inputAnswer = browser.find_element_by_css_selector("#answer")
    inputAnswer.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()