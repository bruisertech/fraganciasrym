from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file://{os.path.abspath('compare2.html')}")
    page.screenshot(path="compare2_pw.png")
    browser.close()
