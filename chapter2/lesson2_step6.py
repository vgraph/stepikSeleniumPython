from selenium import webdriver
import math

'''
1. Открыть страницу http://SunInJuly.github.io/execute_script.html.
2. Считать значение для переменной x.
3. Посчитать математическую функцию от x.
4. Проскроллить страницу вниз.
5. Ввести ответ в текстовое поле.
6. Выбрать checkbox "Подтверждаю, что являюсь роботом".
7. Переключить radiobutton "Роботы рулят!".
8. Нажать на кнопку "Отправить".
'''

link = 'https://suninjuly.github.io/execute_script.html'


def calc(x):
    """
    Функция возращает результат формулы
    :param x:
    :return:
    """
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get(link)

# Находим элемент, содержащий значение x
x_element = driver.find_element_by_css_selector('#input_value')

# Получаем текст внутри этого элемента
x = x_element.text

# Считаем функцию со значением х
y = calc(x)

# Передаем в поле ввода результат вычисления функции
driver.find_element_by_css_selector('#answer').send_keys(y)

# Кликаем чекбокс "Подтверждаю, что являюсь роботом"
driver.find_element_by_css_selector('#robotCheckbox').click()

# Скроллим до кнопки "Отправить"
button = driver.find_element_by_css_selector("button.btn")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)

# Кликаем radio "Роботы рулят"
driver.find_element_by_css_selector('[for="robotsRule"]').click()

# Нажимаем кнопку "Отправить"
driver.find_element_by_css_selector('button.btn').click()
