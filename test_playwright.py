from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file://{os.path.abspath('test.html')}")
    page.screenshot(path="test_overlap_pw.png")
    browser.close()
