import pytest
from selene.support.shared import browser
import config


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.browser_name = config.options.browser_name

    yield
    if config.options.browser_quit_after_each_test:
        browser.quit()
    else:
        browser.clear_local_storage()
