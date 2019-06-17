"""
https://stepik.org/lesson/36285/step/13?unit=162401
Задание: оформляем тесты в стиле unittest
Попробуйте оформить тесты из первого модуля в стиле unittest.

Возьмите тесты из шага 10 - https://stepik.org/lesson/138920/step/10?unit=196194
Создайте новый файл
Создайте в нем класс тестов unittest
Добавьте тест для страницы http://suninjuly.github.io/registration1.html﻿
Добавьте второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
Отправьте эту строчку в качестве ответа на это задание
"""
import pytest
import unittest
from selenium import webdriver


def check_page(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    
    # Находим первое поле ввода первого блока, передаем в него имя
    browser.find_element_by_css_selector(".first_block .first").send_keys("Ivan")
    # Находим второе поле ввода первого блока, передаем в него фамилию
    browser.find_element_by_css_selector(".first_block .second").send_keys("Petrov")
    # Находим третье поле ввода первого блока, передаем в него город
    browser.find_element_by_css_selector(".first_block .third").send_keys("Smolensk")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    return welcome_text


class TestRegistration(unittest.TestCase):
    
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = check_page(link)
        # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = check_page(link)
        # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)
