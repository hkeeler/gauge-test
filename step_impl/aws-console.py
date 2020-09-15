from getgauge.python import after_spec, before_spec, data_store, custom_screenshot_writer, Screenshots, step
import chromedriver_binary  # Adds chromedriver binary to path
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from uuid import uuid4


@step("Take a screenshot of <url>.")
def browse_to(url):
    driver = data_store.spec['webdriver']

    # Browse to AWS Console home page for specified region
    driver.get(url)
    sleep(2)
    Screenshots.capture_screenshot()


@step('User is logged in to AWS Console on <region> region.')
def login_to_aws_console(region):
    driver = data_store.spec['webdriver']

    # Browse to AWS Console home page for specified region
    driver.get(f'https://console.aws.amazon.com/console/home?region={region}#')

    # Select "IAM user" radio button
    #driver.find_element_by_id('aws-signin-general-user-selection-iam').click()

    # Fill in "Account ID (12 digits) or account alias"
    #driver.find_element_by_id('resolving_input').send_keys('cfpb-sandbox')
    #driver.find_element_by_id('next_button').click()
    
    # Wait up to 2 minutes for user to login
    WebDriverWait(driver, 120).until(
        expected_conditions.title_is('AWS Management Console')
    )


@custom_screenshot_writer
def take_screenshot():
    driver = data_store.spec['webdriver']
    image = driver.get_screenshot_as_png()
    base_dir = os.getenv("gauge_screenshots_dir")
    file_name = f"screenshot-{uuid4()}.png"
    file_path = os.path.join(base_dir, file_name)

    open(file_path, "wb").write(image)

    #return os.path.basename(file_name)
    return file_name


'''
@before_spec()
def init_webdriver():
    driver = webdriver.Chrome()

    # Stash credential report for use in scenarios
    data_store.spec['webdriver'] = driver


@after_spec()
def close_webdriver():
    driver = data_store.spec['webdriver']
    driver.close()
'''