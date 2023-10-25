from playwright.sync_api import sync_playwright
import os


def play(username, password):
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://www.instagram.com/accounts/login/?source=auth_switcher')
        page.get_by_label("Phone number, username, or email").fill(username)
        page.get_by_label("Password").fill(password)
        page.get_by_role('button', name='Log in', exact=True).click()
        page.wait_for_timeout(3000)
        page.get_by_alt_text(f"{username}'s profile picture").click()
        page.get_by_role("link", name="Clip").click()
        page.wait_for_timeout(1000)
        page.screenshot(path='post_one.png')
        browser.close()


username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
play(username, password)
