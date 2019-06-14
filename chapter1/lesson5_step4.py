from selenium import webdriver
import math

link = str(math.ceil(math.pow(math.pi, math.e)*10000))

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/find_link_text")
driver.find_element_by_link_text(link).click()

value1 = 'input'
value2 = 'last_name'
value3 = 'city'
value4 = 'country'

input1 = driver.find_element_by_tag_name(value1)
input1.send_keys("Ivan")
input2 = driver.find_element_by_name(value2)
input2.send_keys("Petrov")
input3 = driver.find_element_by_class_name(value3)
input3.send_keys("Smolensk")
input4 = driver.find_element_by_id(value4)
input4.send_keys("Russia")
button = driver.find_element_by_css_selector("button.btn")
button.click()