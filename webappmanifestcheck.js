const chromeLauncher = require('chrome-launcher');
const CDP = require('chrome-remote-interface');

function launchChrome(headless=true) {
    return chromeLauncher.launch({
        // port: 9222, // Uncomment to force a specific port of your choice.
        chromeFlags: [
            '--window-size=412,732',
            '--disable-gpu',
            headless ? '--headless' : ''
        ]
    });
}

(async function() {
   const chrome = await launchChrome();
   const protocol = await CDP({port: chrome.port});

   const {Page} = protocol;
   await Page.enable();

   Page.navigate({url: 'https://www.chromestatus.com/'});

   Page.loadEventFired(async() => {
        const manifest = await Page.getAppManifest();

        if (manifest.url) {
            console.log('Manifest: ' + manifest.url);
            console.log(manifest.data);
        } else {
            console.log('Site has no app manifest');
        }

        protocol.close();
        chrome.kill();
   });
})();
