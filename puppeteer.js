const puppeteer = require('puppeteer');

(async () => {
    console.info("start");
    console.info(`puppeteer`, puppeteer)

    const browser = await puppeteer.launch({
        headless: false,
        args: [`--window-size=1920,1080`],
        slowMo: 30,
    });

    const page = await browser.newPage();

    await page.setViewport({
        width:1920,
        height:1080,
    })
    
    await Promise.all([
        page.goto(`https://www.google.co.kr/`),
        page.waitForNavigation()
    ])
    
    await page.waitForTimeout(3000);
    
    await browser.close();
    
}) ();