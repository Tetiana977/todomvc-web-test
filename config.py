from typing import Literal, Optional
import pydantic


EnvContext = Literal['local', 'stage', 'prod']
BrowserName = Literal['chrome', 'firefox']


class Settings(pydantic.BaseSettings):

    context: EnvContext = 'local'

    browser_name: BrowserName = "chrome"
    browser_quit_after_each_test: bool = False
    headless: bool = False
    browser_window_maximize: bool = False
    browser_window_width = 1440
    browser_window_height: int = 900
    remote_url: Optional[pydantic.AnyHttpUrl] = None
    remote_enableVNC: bool = True
    remote_screenResolution: str = '1980 * 600 * 24'


settings = Settings(_env_file=f'config.{Settings().context}.env')
