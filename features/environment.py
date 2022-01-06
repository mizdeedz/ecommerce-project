from app.application import Application

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver

from support.logger import logger, MyListener

## BrowserStack ##
# bs_user = ''
# bs_pw = ''


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    context.driver = webdriver.Chrome(r'C:\Users\jessi\repo\qa_auto\ecommerce-project\chromedriver_win32\chromedriver.exe')
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox(executable_path=r'C:\Users\jessi\repo\qa_auto\ecommerce-project\geckodriver-v0.30.0-win64\geckodriver.exe')

    ## HEADLESS MODE ##
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1920,1080')
    # context.driver = webdriver.Chrome(r'C:\Users\jessi\repo\qa_auto\ecommerce-project\chromedriver_win32\chromedriver.exe',
    #                                   chrome_options=options)

    ## for browerstack ##
    # desired_cap = {
    #     'browser': 'Chrome',
    #     'browser_version': '96',
    #     'os': 'Windows',
    #     'os_version': '10',
    #     'name': test_name
    # }
    # url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    ## EventFiringWebDriver - log file ##
    ## event for drivers ##
    # context.driver = EventFiringWebDriver(webdriver.Chrome(r'C:\Users\jessi\repo\qa_auto\ecommerce-project\chromedriver_win32\chromedriver.exe'),
    #                                      MyListener())

    ## event for headless mode ##
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    # logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        # logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
