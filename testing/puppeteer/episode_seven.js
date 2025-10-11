const puppeteer = require("puppeteer");

async function generatePDF(url, outputFile) {
    try {
        // launch the browser 
        const browser = await puppeteer.launch({ headless: false });
        const page = await browser.newPage();

        // navigate to the page 
        await page.goto("http://google.com");

        // generate a PDF 
        await page.pdf({ path: outputFile, format: "A4" });

        // close the browser
        await browser.close();
    } catch (err) {
        console.log(err);
    }
}

const url = "http://google.com";
const outputFile = "output_two";
generatePDF(url, outputFile);
