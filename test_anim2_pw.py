from playwright.sync_api import sync_playwright
import os
import time

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file://{os.path.abspath('index.html')}")
    page.wait_for_timeout(600) # wait to capture the final frame
    page.screenshot(path="anim_final2.png")
    browser.close()
