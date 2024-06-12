from playwright.sync_api import sync_playwright
import pandas as pd

def get_data_from_google_search(search_string:str,fd:bool=True):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=fd)
        search_ = browser.new_page()
        search.goto(search_string)

        browser.close()

if __name__=="__main__":
    get_data_from_google_search("Ladies Cosmetics",fd=False)
