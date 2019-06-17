from selenium import webdriver
import math

'''
1. Открыть страницу http://suninjuly.github.io/alert_accept.html
2. Нажать на кнопку
3. Принять confirm
4. На новой странице решить капчу для роботов, чтобы получить число с ответом
'''

link = 'http://suninjuly.github.io/alert_accept.html'


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
driver.find_element_by_css_selector('button.btn').click()

# Переключаемся на модальное окно
confirm = driver.switch_to.alert

# Принимаем confirm
confirm.accept()

# Получаем строковое значение x
x = driver.find_element_by_css_selector('#input_value').text

# Получаем результат формулы
calculation_result = calc(x)

# Передаем результат в поле ввода
driver.find_element_by_css_selector('#answer').send_keys(calculation_result)

# Нажимаем кнопку "Отправить"
driver.find_element_by_css_selector('button.btn').click()
