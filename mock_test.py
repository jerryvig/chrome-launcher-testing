from selenium import webdriver

profile = webdriver.FirefoxProfile('/home/jerry/.mozilla/firefox/huqgok2n.default')
driver = webdriver.Firefox(profile)

driver.get('https://www.linkedin.com/feed/')

driver.implicitly_wait(15)

driver.get_screenshot_as_file('linkedin.png')

driver.quit()
