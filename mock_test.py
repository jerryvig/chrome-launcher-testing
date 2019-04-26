import time

from selenium import webdriver
from selenium.webdriver.firefox import options

DEFAULT_WAIT = 8

profile = webdriver.FirefoxProfile('/home/jerry/.mozilla/firefox/huqgok2n.default')
options = options.Options()
options.headless = True
driver = webdriver.Firefox(profile, options=options)
driver.implicitly_wait(DEFAULT_WAIT)

driver.get('https://www.linkedin.com/feed/')
time.sleep(DEFAULT_WAIT + 5)
driver.get_screenshot_as_file('linkedin-feed.png')


driver.get('https://www.linkedin.com/mynetwork/')
time.sleep(DEFAULT_WAIT)
driver.get_screenshot_as_file('linkedin-mynetwork.png')

driver.get('https://www.linkedin.com/jobs/')
time.sleep(DEFAULT_WAIT)
driver.get_screenshot_as_file('linkedin-jobs.png')

driver.get('https://www.linkedin.com/jobs/')
time.sleep(DEFAULT_WAIT)
driver.get_screenshot_as_file('linkedin-jobs.png')

driver.get('https://www.linkedin.com/notifications/')
time.sleep(DEFAULT_WAIT)
driver.get_screenshot_as_file('linkedin-notifications.png')

driver.quit()
