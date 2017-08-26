from selenium import webdriver
from lib.pom.Home import Home

driver = webdriver.Chrome(executable_path='/Users/ikuma/Downloads/chromedriver')
driver.get('https://www.google.co.jp/imghp?hl=ja')

home = Home(driver)
home.search_with_string('test')

driver.quit()
