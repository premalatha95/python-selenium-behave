from behave import *

from pages.launch_page import Launcher

@given("user is on login page")
def navigate_to_login_page(context):
    context.launch_page = Launcher(context.driver)
    context.launch_page.navigate_to_login_page()