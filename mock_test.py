import random
import time

from selenium import webdriver
from selenium.webdriver.firefox import options

SLEEP_BASE = 180
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
        driver.get_screenshot_as_file(linkedin_routes_map[route][1])

    driver.quit()

def main():
    random.seed()
    profile = webdriver.FirefoxProfile('/home/jerry/.mozilla/firefox/huqgok2n.default')
    opts = options.Options()
    opts.headless = True

    # run indefinitely
    while True:
        run_routes(profile, opts)
        sleep_range = random.randint(-60, 60)
        time.sleep(SLEEP_BASE + sleep_range)

if __name__ == '__main__':
    main()
