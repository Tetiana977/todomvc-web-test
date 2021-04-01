from typing import Literal
import pydantic


EnvContext = Literal['local', 'stage', 'prod']
BrowserName = Literal['chrome', 'firefox']


class Settings(pydantic.BaseSettings):

    context: EnvContext = 'local'

    browser_name: BrowserName = "chrome"
    browser_quit_after_each_test: bool = False
    headless: bool = False


_context = Settings().context
settings = Settings(_env_file=f'config.{_context}.env')
