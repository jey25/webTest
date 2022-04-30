const {Builder, By, Key, until} = require("selenium-webdriver");

async function test() {
    let driver = await new Builder().forBrowser("chrome").build();
    await driver.get("http://google.com");
    await driver.findElement(By.name("q")).sendKeys("Selenium", Key.RETURN);    
    await driver.quit();
}

test();