from playwright.sync_api import sync_playwright
import os
import time

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file://{os.path.abspath('index.html')}")
    page.wait_for_timeout(100) # wait briefly to capture mid-animation if needed, but we want to see it at 100%
    page.screenshot(path="anim_0.1s.png")
    page.wait_for_timeout(500) # wait to capture the final frame
    page.screenshot(path="anim_final.png")
    browser.close()
