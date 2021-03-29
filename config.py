from typing import Literal
import pydantic


EnvContext = Literal['local', 'stage', 'prod']


class Options(pydantic.BaseSettings):

    context: EnvContext = 'local'

    browser_name: str = "chrome"
    browser_quit_after_each_test: bool = False


_context = Options().context
options = Options(_env_file=f'config.{_context}.env')
