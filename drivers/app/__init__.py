import time

from .conf_clicker import FirefoxBrowserZoomClicker
from config import GECKODRIVER_PATH


def run():
    conf_url = input("Conference_link: ")
    conf_code = input("Conference Code: ")
    nickname = input("Username: ")
    browser_exe_path = input("Path to browser: ")
    clicker = FirefoxBrowserZoomClicker(
        str(GECKODRIVER_PATH),
        browser_exe_path,
        conf_url,
        conf_code,
        nickname
    )
    clicker.conf_login()
    time.sleep(10)
