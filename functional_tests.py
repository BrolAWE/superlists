from selenium import webdriver

browser = webdriver.Chrome("C:/Users/aleks/Downloads/chromedriver_win32/chromedriver.exe")
browser.get('http://localhost:8000')
assert 'Django' in browser.title
