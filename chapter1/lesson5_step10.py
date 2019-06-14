# -*- coding: utf-8 -*-
from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
# Для поиска элементов использованы CSS локаторы

# Находим первое поле ввода первого блока, передаем в него имя
browser.find_element_by_css_selector(".first_block .first").send_keys("Ivan")

# Находим второе поле ввода первого блока, передаем в него фамилию
# Тест падает здесь. На странице registration2.html убрали поле ввода
# с классом .second
browser.find_element_by_css_selector(".first_block .second").send_keys("Petrov")

# Находим третье поле ввода первого блока, передаем в него город
browser.find_element_by_css_selector(".first_block .third").send_keys("Smolensk")

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
