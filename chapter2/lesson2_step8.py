from selenium import webdriver
import os

'''
1. Открыть страницу http://suninjuly.github.io/file_input.html
2. Заполнить текстовые поля: имя, фамилия, email
3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
4. Нажать кнопку "Отправить"
'''

link = 'http://suninjuly.github.io/file_input.html'

driver = webdriver.Chrome()
driver.get(link)

# Заполняем поля формы
driver.find_element_by_css_selector('[name="firstname"]').send_keys('Ivan')
driver.find_element_by_css_selector('[name="lastname"]').send_keys('Petrov')
driver.find_element_by_css_selector('[name="email"]').send_keys('email@email.com')

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))

# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'file.txt')

# Находим кнопку загрузки файла
upload_element = driver.find_element_by_css_selector('#file')

# Передаем путь к файлу в элемент input type=file
upload_element.send_keys(file_path)

# Нажимаем кнопку "Отправить"
driver.find_element_by_css_selector('button.btn').click()
