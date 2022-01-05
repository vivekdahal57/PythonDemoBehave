import os
import allure
from behave import use_fixture
from behave.log_capture import capture
from page_object.driver_factory_fixture import browser_chrome, browser_firefox, browser_ie, base_page, \
    browser_chrome_headless, browser_firefox_headless
from page_object.global_objects import erp_login_page

""" 
before all is called in order to execute before any tests starts executing
its parameters can ve either provided in ini file or from the command line
We are using before_feature here to use different instances for each feature level testing
"""


def before_feature(context, feature):
    try:
        if context.config.userdata.get('browser') == "chrome":
            if context.config.userdata.get('headless').lower() == "true":
                use_fixture(browser_chrome_headless, context)
            else:
                use_fixture(browser_chrome, context)
        if context.config.userdata.get('browser') == "firefox":
            if context.config.userdata.get('headless').lower() == "true":
                use_fixture(browser_firefox_headless, context)
            else:
                use_fixture(browser_firefox, context)
        if context.config.userdata.get('browser') == "ie":
            use_fixture(browser_ie, context)
    except Exception as ex:
        raise ex

@capture
def after_scenario(context, scenario):
    # Take screenshot if scenario fails
    if scenario.status == 'failed':
        allure.attach(base_page.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        url = context.web.get_current_url()
        # if "admin" in url.split("/"):
        #     admin_dashboard_page.logout()
        # elif "blueprint" in url.split("/"):
        #     blueprint_dashboard_page.logout()
        # elif "architect" in url.split("/") or "organize" in url.split("/") or "ingest" in url.split("/"):
        #     architect_dashboard_page.logout()
        # else:
        #     blueprint_dashboard_page.logout()


def make_dir(directories):
    """
    Checks if directory exists, if not make a directory, given the directory path
    :param: <string>dir: Full path of directory to create
    """
    if not os.path.exists(directories):
        os.makedirs(directories)
