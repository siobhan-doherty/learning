const puppeteer = require("puppeteer");

async function run() {
    const browser = await puppeteer.launch(
        { 
            headless: false, 
            defaultViewport: { width: 980, height: 600 }
        }
    );

    const page = await browser.newPage();
    await page.goto("https://yahoo.com");
    const title = await page.title(); 
    console.log(title);
    const heading = await page.$eval("h1", (element) => element.textContent);
    console.log(heading);
    await page.screenshot({ path: "episode_four_part_two.png" });
    await page.pdf({ path: "another_example.pdf", format: "A4" });
    await browser.close();
}

run();
