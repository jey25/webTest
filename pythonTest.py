from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
url = 'https://google.com'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

driver.find_element_by_css_selector('.gb_1 gb_2 gb_9d gb_9c').click()
