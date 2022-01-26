from app.application import Application

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.events import EventFiringWebDriver

from support.logger import logger, MyListener

## BrowserStack ##
bs_user = ''
bs_pw = ''

## Allure command to wrap ALL or SPECIFIC tests ##
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature

## Allure command to show results ##
# allure serve test_results/


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    # context.driver = webdriver.Chrome(r'C:\Users\jessi\repo\qa_auto\ecommerce-project\chromedriver_win32\chromedriver.exe')
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox(executable_path=r'C:\Users\jessi\repo\qa_auto\ecommerce-project\geckodriver-v0.30.0-win64\geckodriver.exe')

    ## HEADLESS MODE ##
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1920,1080')
    # context.driver = webdriver.Chrome(r'C:\Users\jessi\repo\qa_auto\ecommerce-project\chromedriver_win32\chromedriver.exe',
    #                                   chrome_options=options)

    ## For BrowerStack ##
    # desired_cap = {
    #     'browser': 'Chrome',
    #     'browser_version': '97',
    #     'os': 'Windows',
    #     'os_version': '10',
    #     'name': test_name
    # }
    # url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    ## Mobile Emulation - local ##

    ## mobile - use device name ##
    # mobile_emulation = {"deviceName": "iPhone SE"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # chrome_options.add_experimental_option("w3c", False)
    # context.driver = webdriver.Chrome(
    #     r'C:\Users\jessi\repo\qa_auto\ecommerce-project\chromedriver_win32\chromedriver.exe',
    #     desired_capabilities=chrome_options.to_capabilities())

    ## mobile - specify device params ##
    # mobile_emulation = {
    #     "deviceMetrics": {"width": 360, "height": 700, "pixelRatio": 2.0, "mobile": True},
    #     "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 ("
    #                  "KHTML, like Gecko) Chrome/%s Mobile Safari/537.36"}
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(
    #     r'C:\Users\jessi\repo\qa_auto\ecommerce-project\chromedriver_win32\chromedriver.exe',
    #     chrome_options=chrome_options)

    ## mobile - remote (BrowserStack) - use device name ##
    desired_cap = {
        'browser': 'Chrome',
        'browser_version': '97',
        'os': 'Windows',
        'os_version': '10',
        'name': test_name
    }
    url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    mobile_emulation = {"deviceName": "iPhone SE"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_experimental_option("w3c", False)
    context.driver = webdriver.Remote(command_executor=url,
                                      desired_capabilities=desired_cap, options=chrome_options)

    # context.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
    #                                   desired_capabilities=chrome_options.to_capabilities())

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
