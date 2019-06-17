"""
1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
2. Дождаться, когда цена дома уменьшится до 10000 RUR (ожидание нужно установить не меньше 12 секунд)
3. Нажать на кнопку "Забронировать"
4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    """
    Функция возращает результат формулы ln(abs(12*sin(x)))
    :param x:
    :return str:
    """
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get(link)

# Ожидаем когда текст внутри элемента == '10000 RUR'
# Время ожидания 12 секунд
WebDriverWait(driver, 12).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '10000 RUR')
)

# Нажимаем кнопку "Забронировать"
driver.find_element_by_css_selector('#book').click()

# Получаем строковое значение x
x = driver.find_element_by_css_selector('#input_value').text

# Получаем результат формулы
result = calc(x)

# Передаем результат в поле ввода
driver.find_element_by_css_selector('#answer').send_keys(result)

# Нажимаем кнопку "Отправить"
driver.find_element_by_css_selector('#solve').click()
