const chromeLauncher = require('chrome-launcher');
const CDP = require('chrome-remote-interface');

const launchChrome = (headless=true) => {
    return chromeLauncher.launch({
        // port: 9222, // Uncomment to force a specific port of your choice.
        chromeFlags: [
            '--window-size=412,732',
            '--disable-gpu',
            headless ? '--headless' : ''
        ]
    });
};

(async function() {
    const chrome = await launchChrome();
    const protocol = await CDP({port: chrome.port});

    const {Page, Runtime} = protocol;
    await Promise.all([Page.enable(), Runtime.enable()]);

    Page.navigate({url: 'https://www.indeed.com/'});

    Page.loadEventFired(async() => {
       const js = 'document.querySelector("title").textContent';
       const result = await Runtime.evaluate({expression: js});
       console.log('Title of page: ' + result.result.value);
       protocol.close();
       chrome.kill();
    });
})();
