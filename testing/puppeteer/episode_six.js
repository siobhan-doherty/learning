const puppeteer = require("puppeteer");
const fs = require("fs");

async function run() {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();

    // navigate to page
    await page.goto("http://bbc.com");

    // SEO related data 
    const title = await page.title();
    const metaDescription = await page.$eval("meta[name='description']", (element) => element.textContent);
    const metaKeywords = await page.$eval("meta[name='keywords']", (element) => element.textContent);

    // extract links
    const links = await page.$$eval("a", (elements) =>
        elements.map((element) => ({ 
            src: element.href, 
            text: element.textContent
        }))
    )

    // extract images 
    const images = await page.$$eval("img", (elements) => 
        elements.map((element) => ({
            src: element.src, 
            alt: element.alt
        }))
    )

    // take counts of the images and links
    const imageCount = images.length;
    const linkCount = links.length;

    // prepare output format 
    const outputData = {
        title,
        metaDescription, 
        metaKeywords, 
        images, 
        links, 
        imageCount, 
        linkCount
    };

    // convert JSON into a string 
    const outputJSON = JSON.stringify(outputData);

    // write to file 
    fs.writeFileSync("output", outputJSON);

    await browser.close();
}

run();
