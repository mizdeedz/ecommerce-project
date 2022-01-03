from app.application import Application

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    # context.driver = webdriver.Chrome(r'C:\Users\jessi\repo\qa_auto\ecommerce-project\chromedriver_win32\chromedriver.exe')
    # context.driver = webdriver.Safari()
    context.driver = webdriver.Firefox(executable_path=r'C:\Users\jessi\repo\qa_auto\ecommerce-project\geckodriver-v0.30.0-win64\geckodriver.exe')

    ## HEADLESS MODE ##
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1920,1080')
    # context.driver = webdriver.Chrome(r'C:\Users\jessi\repo\qa_auto\ecommerce-project\chromedriver_win32\chromedriver.exe',
    #                                   chrome_options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
