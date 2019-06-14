from selenium import webdriver
import math

link = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
    '''
    Функция возращает результат формулы
    :param x:
    :return:
    '''
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get(link)

# Находим значение аттрибута valuex элемента "сундук"
x = driver.find_element_by_css_selector('#treasure').get_attribute('valuex')

y = calc(x)

# Передаем в поле ввода результат вычисления функции
driver.find_element_by_css_selector('#answer').send_keys(y)

# Кликаем чекбокс "Подтверждаю, что являюсь роботом"
driver.find_element_by_css_selector('#robotCheckbox').click()

# Кликаем radio "Роботы рулят"
driver.find_element_by_css_selector('#robotsRule').click()

# Нажимаем кнопку "Отправить"
driver.find_element_by_css_selector('button.btn').click()
