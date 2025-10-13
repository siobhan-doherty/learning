const puppeteer = require("puppeteer");

async function run() {
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();
    await page.goto("https://yahoo.com");
    const title = await page.title(); 
    console.log(title);
    const heading = await page.$eval("h1", (element) => element.textContent);
    console.log(heading);
    await page.screenshot({ path: "episode_four.png" });
    await page.pdf({ path: "example.pdf", format: "A4" });
    await browser.close();
}

run();
