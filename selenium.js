// const {Builder, By, Key, util} = require(`selenium-webdriver`);

// async function test() {
//     const driver = await new Builder().forBrowser(`chrome`).build();
//     await driver.get(`http://studio.zepeto.me/kr`);
//     await driver.findElement(By.name("q")).sendKeys(`sleenium`, Key.RETURN);    
// }

// test();

const webdriver = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const chromedriver = require('chromedriver');

chrome.setDefaultService(new chrome.ServiceBuilder(chromedriver.path).build());

const {Builder, Browser, By, Key, until} = require('selenium-webdriver');

(async function example() {
  let driver = await new Builder().forBrowser(Browser.CHROME).build();
  try {
    await driver.get('http://www.google.com/ncr');
    await driver.findElement(By.name('q')).sendKeys('webdriver', Key.RETURN);
    await driver.wait(until.titleIs('webdriver - Google Search'), 1000);
  } finally {
    await driver.quit();
  }
})();