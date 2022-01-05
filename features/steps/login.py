import time

from behave import given, when, then, step
from page_object.global_objects import *


def get_username(context, username):
    if username == 'correct_username':
        return context.config.userdata.get('correct_normal_username')
    else:
        return username


def get_password(context, password):
    if password == 'correct_password':
        return context.config.userdata.get('correct_normal_password')
    else:
        return password


@given("admin user is in dashboard page after login with {username} and {password}")
def login(context, username, password):
    username = get_username(context, username)
    password = get_password(context, password)
    erp_login_page.open(context.config.userdata.get('app_url'))
    erp_login_page.verify_login_page()
    erp_login_page.login(username, password)
    # erp_login_page.verify_login_pass()
