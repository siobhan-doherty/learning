const puppeteer = require("puppeteer");

async function run() {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();

    // navigate to page 
    await page.goto("https://google.com");

    // extract images 
    const images = await page.$$eval("img", (elements) =>
        elements.map((element) => ({
            src: element.src, 
            alt: element.alt,
        }))
    );

    // extract links 
    const links = await page.$$eval("a", (elements) => 
        elements.map((element) => ({
            href: element.href, 
            text: element.textContent,
        }))
    );

    const imageCount = images.length;
    const linkCount = links.length;

    // output of the above 
    const output = JSON.stringify({ images, links, imageCount, linkCount });
    console.log(output);

    // close the browser 
    await browser.close();
}

run();
