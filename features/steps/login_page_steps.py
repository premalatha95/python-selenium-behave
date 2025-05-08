from behave import *

from pages.login_page import LoginPage


@when("user chooses to signup with")
def user_chooses_to_sign_up_with(context):
    for row in context.table:
        name = row['name']
        email = row['email']
        context.login_page = LoginPage(context.driver)
        context.login_page.sign_up_with(name, email)
