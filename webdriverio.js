const webdriverio = require('webdriverio');
const chromedriver = require('chromedriver');

const PORT = 9515;

chromedriver.start([
    '--url-base=wd/hub',
    `--port=${PORT}`,
    '--verbose'
]);

(async() => {
    const opts = {
        host: 'localhost',
        port: PORT,
        logLevel: 'error',
        path: '/',
        capabilities: {
            browserName: 'chrome',
            //chromeOptions: {args: ['--headless']}
        }
    };

   const browser = await webdriverio.remote(opts);

    //console.log( 'keys = ' + JSON.stringify(Object.keys(browser)) );

    // await browser.url('https://www.chromestatus.com/features');

    //const title = await browser.getTitle();
    //console.log(`Title: ${title}`);

   /*  await browser.waitForText('.num-features', 3000);
    let numFeatures = await browser.getText('.num-features');
    console.log(`Chrome has ${numFeatures} total features`);

    await browser.setValue('input[type="search"]', 'CSS');
    console.log('Filtering features....');
    await browser.pause(1000);

    numFeatures = await browser.getText('.num-features');
    console.log(`Chrome has ${numFeatures} CSS features`);

    const buffer = await browser.saveScreenshot('screenshot.png');
    console.log('Saved screenshot...'); */

    chromedriver.stop();
    //browser.end();
})();
