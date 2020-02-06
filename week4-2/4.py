from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.google.com/search?q='

word = input('Search: ')

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get(url+word)

search_box = driver.find_element_by_id('fakebox-input')
search_box.submit()