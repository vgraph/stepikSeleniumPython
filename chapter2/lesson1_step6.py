from selenium import webdriver
import math

link = 'http://suninjuly.github.io/math.html'


def calc(x):
    '''
    Функция возращает результат формулы
    :param x:
    :return:
    '''
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

# Кликаем radio "Роботы рулят"
driver.find_element_by_css_selector('[for="robotsRule"]').click()

# Нажимаем кнопку "Отправить"
driver.find_element_by_css_selector('button.btn').click()
