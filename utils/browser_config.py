from typing import Dict, Callable
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def create_chrome_driver():
    options = ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(options=options)

def create_firefox_driver():
    options = FirefoxOptions()
    # options.add_argument('--headless')
    return webdriver.Firefox(options=options)

# Dictionary mapping browsers to their configuration functions
browser_configs: Dict[str, Callable] = {
    'chrome': create_chrome_driver,
    'firefox': create_firefox_driver
} 