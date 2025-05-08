from utils.create_driver import create_driver

def before_scenario(context, scenario):
    """Set up the driver before each scenario"""
    context.driver = create_driver()

def after_scenario(context, scenario):
    """Clean up after each scenario"""
    if hasattr(context, 'driver'):
        context.driver.quit()