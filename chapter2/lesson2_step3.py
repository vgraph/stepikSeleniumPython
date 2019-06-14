from selenium import webdriver
from selenium.webdriver.support.ui import Select

'''
1. Открыть страницу http://suninjuly.github.io/selects1.html
2. Посчитать сумму заданных чисел
3. Выбрать в выпадающем списке значение равное расчитанной сумме
4. Нажать кнопку "Отправить"
'''

link = 'http://suninjuly.github.io/selects1.html'

driver = webdriver.Chrome()
driver.get(link)

# Получаем со траницы первое число
num1 = driver.find_element_by_css_selector('#num1').text

# Получаем со траницы второе число
num2 = driver.find_element_by_css_selector('#num2').text

# Считаем сумму чисел
sum_of_nums = int(num1) + int(num2)

# Находим элемент dropdown
select = Select(driver.find_element_by_css_selector('#dropdown'))

# Выбираем пункт dropdown'а, свойтво value, которого соответствует сумме
select.select_by_value(str(sum_of_nums))

# Можно было бы выбрать нужный элемент так:
# select = Select(driver.find_element_by_css_selector('#dropdown'))
# select.select_by_visible_text(str(sum_of_nums))

# Нажимаем кнопку "Отправить"
driver.find_element_by_css_selector('button.btn').click()
