from selenium import webdriver

link = 'http://suninjuly.github.io/cats.html'

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get(link)

driver.find_element_by_css_selector('#button')
