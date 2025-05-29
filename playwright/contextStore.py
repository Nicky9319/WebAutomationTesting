from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(storage_state = "auth_state.json")
    page = context.new_page()
    page.goto("https://example.com")

    # 🧠 Let user login manually or do auto-login via selectors
    input("Login manually, then press Enter...")

    # ✅ Save session info (cookies, localStorage) to disk
    context.storage_state(path="auth_state.json")

    print("Session saved to auth_state.json")
    browser.close()
