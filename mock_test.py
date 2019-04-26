from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome-unstable'
options.add_argument('headless')
options.add_argument("user-data-dir=/home/jerry/.config/google-chrome-unstable/Default")

driver = webdriver.Chrome(options=options)

driver.get('https://www.linkedin.com/feed/')

driver.implicitly_wait(10)

##sign_in_buttons = driver.find_elements_by_css_selector('a[class=nav__button-secondary]')
##for button in sign_in_buttons:
#    button.click()
# password = driver.find_element_by_css_selector('input[type=password]')
# login = driver.find_element_by_css_selector('input[value="Log In"]')

# email.send_keys('jjvigil@ucdavis.edu')

driver.implicitly_wait(4)

#id = driver.find_element_by_id('username')
#password = driver.find_element_by_id('password')
#sign_in_button = driver.find_element_by_css_selector('button[type=submit]')

#id.send_keys('jerry.vigil@mktneutral.com')
#password.send_keys('XXXXXXX')
#sign_in_button.click()

driver.implicitly_wait(4)

driver.get_screenshot_as_file('linkedin.png')

##pin_input = driver.find_element_by_css_selector('#input__phone_verification_pin')
# two_step_submit = driver.find_element_by_css_selector('#two-step-submit-button')

# import code
# code.interact(local=locals())

