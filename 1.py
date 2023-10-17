import asyncio
import puppeteer

async def main():
    # Create a new Puppeteer browser instance
    browser = await puppeteer.launch()

    # Navigate to the target web page
    page = await browser.newPage()
    await page.goto("https://example.com")

    # Wait for the page to load
    await page.waitForNavigation()

    # Extract the data you need
    title = await page.title()
    content = await page.evaluate(lambda: document.querySelector("div.content").textContent)

    # Close the browser
    await browser.close()

    # Print the extracted data
    print(title)
    print(content)

if __name__ == "__main__":
    asyncio.run(main())
