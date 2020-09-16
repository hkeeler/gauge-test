from getgauge.python import after_spec, before_spec, data_store, custom_screenshot_writer, Screenshots, step
import chromedriver_binary  # Adds chromedriver binary to path
import os
from splinter import Browser
from time import sleep


@step("Browse to <url>.")
def browse_to(url):
    browser = data_store.spec['browser']

    browser.visit(url)

@step("Scroll page to <page_text>.")
def scroll_page_to(page_text):
    browser = data_store.spec['browser']

    browser.is_text_present(page_text, wait_time=10)

    found_elements = browser.find_by_text(page_text)

    assert len(found_elements) != 0, f'Could not find text "{page_text}" on the page.'
    assert not len(found_elements) > 1, f'Text "{page_text}" found multiple times. Specify a more specific term.'
    
    found_elements.first.scroll_to()


@step("Take a screenshot.")
def take_screenshot():
    Screenshots.capture_screenshot()


@step('User is logged in to AWS Console on <region> region.')
def login_to_aws_console(region):
    browser = data_store.spec['browser']

    # Browse to AWS Console home page for specified region
    browser.visit(f'https://console.aws.amazon.com/console/home?region={region}#')

    # Select "IAM user" radio button
    #driver.find_element_by_id('aws-signin-general-user-selection-iam').click()

    # Fill in "Account ID (12 digits) or account alias"
    #driver.find_element_by_id('resolving_input').send_keys('cfpb-sandbox')
    #driver.find_element_by_id('next_button').click()
    
    # Wait up to 2 minutes for user to login
    browser.is_text_present('AWS Management Console', wait_time=120)


@custom_screenshot_writer
def write_screenshot():
    browser = data_store.spec['browser']
    
    base_dir = os.getenv("gauge_screenshots_dir")
    prefix = "screenshot-"
    path_with_prefix = os.path.join(base_dir, prefix)

    # NOTE: The docs say `screenshot()` expects a relative path of
    #       the screenshot filename, but really it expects a path
    #       with a filename prefix.
    # SEE:  https://splinter.readthedocs.io/en/latest/screenshot.html
    actual_path = browser.screenshot(path_with_prefix, full=True)

    #special_pic = browser.find_by_text('Alternate Contacts').first.screenshot(name=path_with_prefix, full=True)
    #print(f'SPECIAL: {special_pic}')

    return actual_path


# FIXME: Switch to "Browser" singleton
@before_spec()
def init_browser():
    browser = Browser('chrome')

    # Stash credential report for use in scenarios
    data_store.spec['browser'] = browser


@after_spec()
def close_browser():
    browser = data_store.spec['browser']
    #browser.quit()
