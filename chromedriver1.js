const fs = require('fs');
const webdriver = require('selenium-webdriver');
const chromedriver = require('chromedriver');

const chromeCapabilities = webdriver.Capabilities.chrome();
chromeCapabilities.set('chromeOptions', {args: ['--headless']});

const driver = new webdriver.Builder()
    .forBrowser('chrome')
    .withCapabilities(chromeCapabilities)
    .build();

(async function() {
    await driver.get('https://www.linkedin.com/');

    await driver.takeScreenshot().then(base64png => {
       fs.writeFileSync('screenshot.png', new Buffer(base64png, 'base64'));
    });

    driver.quit();
})();
