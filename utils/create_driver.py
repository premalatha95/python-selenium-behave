import os
from selenium import webdriver
from .browser_config import browser_configs
from .setup_logger import logger

def create_driver() -> webdriver.Remote:
    """
    Create and return a WebDriver instance based on the BROWSER environment variable.
    
    Returns:
        webdriver.Remote: Configured WebDriver instance
        
    Raises:
        ValueError: If BROWSER environment variable is not set or browser is not supported
    """
    browser = os.environ.get('BROWSER')
    if not browser:
        logger.error("BROWSER environment variable is not set")
        raise ValueError("BROWSER environment variable is not set")
        
    browser = browser.lower()
    logger.info(f"Initializing {browser} browser")
    
    try:
        if browser not in browser_configs:
            logger.error(f"Unsupported browser: {browser}")
            raise ValueError(f"Browser {browser} is not supported. Supported browsers: {', '.join(browser_configs.keys())}")
            
        driver = browser_configs[browser]()
        driver.implicitly_wait(10)  # Set implicit wait time
        logger.info(f"Successfully initialized {browser} browser")
        return driver
        
    except Exception as e:
        logger.error(f"Failed to initialize {browser} driver: {str(e)}", exc_info=True)
        raise RuntimeError(f"Failed to initialize {browser} driver: {str(e)}") 