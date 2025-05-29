from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://discord.com")

        # This function will receive click coordinates from the page
        def handle_click(x, y):
            print(f"Mouse clicked at coordinates: x={x}, y={y}")

        # Expose the Python function to the page as 'reportClick'
        page.expose_function("reportClick", handle_click)

        # Add click listener in the page that calls 'reportClick' with click coordinates
        page.evaluate("""
            document.addEventListener('click', event => {
                // event.clientX/Y are coordinates relative to viewport
                window.reportClick(event.clientX, event.clientY);
            });
        """)

        print("Click anywhere in the browser window and watch the coordinates print here.")
        input("Press Enter to exit...")

        browser.close()

run()
