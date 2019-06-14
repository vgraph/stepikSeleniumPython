from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/huge_form.html")

elements = driver.find_elements_by_css_selector("[type=text]")

for element in elements:
    element.send_keys("Мой ответ")

button = driver.find_element_by_css_selector("button").click()
