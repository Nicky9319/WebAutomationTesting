import asyncio
from playwright.async_api import async_playwright

import time

async def main():
    async with async_playwright() as p:

        # Launch browser in headful mode so you see the window
        # browser = await p.chromium.launch(headless=False, args=["--disable-gpu"])

        browser = await p.chromium.launch(
            executable_path="/home/paarth/web_automation/playwrith/chrome-linux/chrome",
            headless=False,  # Set to True if you want to run in headless mode
            args=["--disable-gpu"]
        )
            
        
        # Create a new browser context and page
        context = await browser.new_context()
        page = await context.new_page()
        
        time.sleep(5)

        # Visit first website
        url1 = "https://discord.com/"
        print(f"Loading {url1} ...")
        await page.goto(url1)
        # Wait for network to be idle (page loaded fully)
        await page.wait_for_load_state("networkidle")
        # Take screenshot
        await page.screenshot(path="screenshot1.png")
        print(f"Screenshot of {url1} saved as screenshot1.png")
        
        # Visit second website
        url2 = "https://www.wikipedia.org"
        print(f"Loading {url2} ...")
        await page.goto(url2)
        await page.wait_for_load_state("networkidle")
        await page.screenshot(path="screenshot2.png")
        print(f"Screenshot of {url2} saved as screenshot2.png")
        
        # Keep the program open until you close manually
        print("Browser is open. Close the browser window or press Ctrl+C to exit.")
        
        try:
            # Wait forever until interrupted manually
            await asyncio.Event().wait()
        except KeyboardInterrupt:
            print("\nExiting program by user interruption.")
        
        # Clean up
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
