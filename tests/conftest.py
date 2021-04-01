import pytest
from selene.support.shared import browser
import config


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.browser_name = config.settings.browser_name

    driver = _maybe_driver_from_settings(config.settings)
    if driver:
        browser.config.driver = driver

    yield

    if config.settings.browser_quit_after_each_test:
        browser.quit()
    else:
        browser.clear_local_storage()


def _maybe_driver_from_settings(settings: config.Settings):
    from selenium import webdriver
    driver = None
    if config.settings.browser_name == 'chrome':
        from webdriver_manager.chrome import ChromeDriverManager
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = settings.headless
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
            options=chrome_options
        )
    elif config.settings.browser_name == 'firefox':
        from webdriver_manager.firefox import GeckoDriverManager
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = settings.headless
        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(),
            options=firefox_options
        )
    return driver
