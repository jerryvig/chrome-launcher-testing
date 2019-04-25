from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome-unstable'
options.add_argument('headless')

driver = webdriver.Chrome(options=options)

driver.get('https://facebook.com/')

driver.implicitly_wait(10)

email = driver.find_element_by_css_selector('input[type=email]')
password = driver.find_element_by_css_selector('input[type=password]')
login = driver.find_element_by_css_selector('input[value="Log In"]')

email.send_keys('jjvigil@ucdavis.edu')

driver.get_screenshot_as_file('main-page.png')
