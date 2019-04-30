import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox import options

SLEEP_BASE = 300
DEFAULT_WAIT = 8

linkedin_routes_map = {
    'feed': ['https://www.linkedin.com/feed/', 'linkedin-feed.png'],
    'mynetwork': ['https://www.linkedin.com/mynetwork/', 'linkedin-mynetwork.png'],
    'jobs': ['https://www.linkedin.com/jobs/', 'linkedin-jobs.png'],
    'notifications': ['https://www.linkedin.com/notifications/', 'linkedin-notifications.png'],
    'premium': ['https://www.linkedin.com/premium/my-premium/', 'linkedin-premium.png'],
    'jobs-search': ['https://www.linkedin.com/jobs/search/', 'linkedin-jobs-search.png'],
}

def run_routes(profile, opts):
    driver = webdriver.Firefox(profile, options=opts)
    driver.implicitly_wait(DEFAULT_WAIT)

    for route in linkedin_routes_map:
        driver.get(linkedin_routes_map[route][0])
        time.sleep(DEFAULT_WAIT)
        if route == 'jobs-search':
            job_search_input = driver.find_element_by_id('jobs-search-box-keyword-id-ember93')
            job_search_input.send_keys('python javascript')
            location_search_input = driver.find_element_by_id('jobs-search-box-location-id-ember93')
            location_search_input.send_keys(Keys.BACKSPACE * 13)
            location_search_input.send_keys('Austin, Texas')
            search_button = driver.find_element_by_css_selector('button[data-ember-action-99="99"]')
            search_button.click()
            time.sleep(DEFAULT_WAIT)

            job_search_input.send_keys(Keys.BACKSPACE * 17)
            job_search_input.send_keys('c++ python')
            search_button.click()
            time.sleep(DEFAULT_WAIT)

            job_search_input.send_keys(Keys.BACKSPACE * 10)
            job_search_input.send_keys('python docker')
            search_button.click()
            time.sleep(DEFAULT_WAIT)
        driver.get_screenshot_as_file(linkedin_routes_map[route][1])

    driver.close()

def main():
    random.seed()
    profile = webdriver.FirefoxProfile('/home/jerry/.mozilla/firefox/huqgok2n.default')
    opts = options.Options()
    opts.headless = True

    # run indefinitely
    while True:
        run_routes(profile, opts)
        sleep_range = random.randint(-60, 60)
        print('Sleeping %d s.' % (SLEEP_BASE + sleep_range))
        time.sleep(SLEEP_BASE + sleep_range)

    # driver.quit()

if __name__ == '__main__':
    main()
