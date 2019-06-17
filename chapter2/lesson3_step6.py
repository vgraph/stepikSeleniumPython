"""Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
2. Нажать на кнопку
3. Переключиться на новую вкладку
4. Пройти капчу для робота и получить число-ответ
"""

from selenium import webdriver
import math

link = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x):
    """
    Функция возращает результат формулы ln(abs(12*sin(x)))
    :param x:
    :return str:
    """
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
# Открываем страницу
driver.get(link)

# Нажимаем кнопку "Хочу отправиться в волшебное путешествие"
driver.find_element_by_css_selector('button.trollface').click()

# Переключаемся на вторую вкладку
new_window = driver.window_handles[1]  # Из списка имен вкладок выбираем вторую
driver.switch_to.window(new_window)  # Переключаемся на новую вкладку

# Получаем строковое значение x
x = driver.find_element_by_css_selector('#input_value').text

# Получаем результат формулы
calculation_result = calc(x)

# Передаем результат в поле ввода
driver.find_element_by_css_selector('#answer').send_keys(calculation_result)

# Нажимаем кнопку "Отправить"
driver.find_element_by_css_selector('button.btn').click()