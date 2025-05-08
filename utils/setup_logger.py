import logging
from typing import Optional

def setup_logger(name: str = None) -> logging.Logger:
    """
    Set up and configure a logger with console handler.
    
    Args:
        name (str, optional): Name of the logger. Defaults to None.
        
    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logger
    logger = logging.getLogger(name or __name__)
    logger.setLevel(logging.DEBUG)
    
    # Prevent adding handlers multiple times
    if logger.handlers:
        return logger
    
    # Create console formatter
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    
    # Console handler - logs INFO and above
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)
    
    # Add handler to logger
    logger.addHandler(console_handler)
    
    return logger

# Create a default logger instance
logger = setup_logger('browser_automation')
