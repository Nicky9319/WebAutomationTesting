from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://discord.com")

    # Click at coordinates x=100, y=200 in the viewport
    page.mouse.click(1190, 66)

    input("Click performed at (1190, 66). Press Enter to exit...")

    browser.close()
