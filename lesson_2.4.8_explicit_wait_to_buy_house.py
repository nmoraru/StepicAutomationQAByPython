from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button1 = browser.find_element_by_css_selector("#book")
    
    button3 = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1.click()

    x_element1 = browser.find_element_by_css_selector("#input_value")
    x = x_element1.text
    
    y = calc(x)

    inputAnswer = browser.find_element_by_css_selector("#answer")
    inputAnswer.send_keys(y)

    button2 = browser.find_element_by_css_selector("#solve")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()