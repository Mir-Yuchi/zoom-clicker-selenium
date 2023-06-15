import time
from typing import Any

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class FirefoxBrowserZoomClicker(webdriver.Firefox):

    def __init__(self, driver_path: str, browser_loc: str, conf_url: str, conf_key: str, nickname: str):
        opt = self.__configure(browser_loc)
        super().__init__(
            executable_path=driver_path,
            options=opt
        )
        self.conf_url = conf_url
        self.conf_key = conf_key
        self.nickname = nickname

    def __configure(self, browser_location: str):
        options = Options()
        options.binary_location = browser_location
        # options.headless = True
        return options

    def browser_quit(self):
        self.close()
        self.quit()

    def __del__(self):
        self.browser_quit()

    def iterate_and_click_by_xpath(self, xpath_list: list[str], sleep_times: list[int]):
        for index, xpath in enumerate(xpath_list):
            self.find_element(
                By.XPATH,
                xpath
            ).click()
            time.sleep(sleep_times[index])

    def iterate_and_send_by_xpath(self, xpath_list: list[str], sleep_times: list[int], values_list: list[Any]):
        for index, xpath in enumerate(xpath_list):
            self.find_element(
                By.XPATH,
                xpath
            ).send_keys(values_list[index])
            time.sleep(sleep_times[index])

    def conf_login(self):
        self.get(self.conf_url)
        time.sleep(10)
        click_xpaths_list = [
            "/html/body/div[4]/div[3]/div/div/div[2]/div/div/button",
            "/html/body/div[2]/div[2]/div/div[1]/div/div",
            "/html/body/div[2]/div[2]/div/div[2]/h3[2]/span/a",
        ]
        self.iterate_and_click_by_xpath(
            click_xpaths_list,
            [5, 5, 5]
        )
        conf_enter_form_xpath = [
            "/html/body/div[1]/div[4]/div[2]/div[2]/div/form/div/div[2]/div[2]/input",
            "/html/body/div[1]/div[4]/div[2]/div[2]/div/form/div/div[3]/div[2]/input"
        ]
        self.iterate_and_send_by_xpath(
            conf_enter_form_xpath,
            [5, 5],
            [self.conf_key, self.nickname]
        )
        click_xpaths_list_2 = [
            "/html/body/div[1]/div[4]/div[2]/div[2]/div/form/div/div[5]/div/button",
            "/html/body/div[2]/div[2]/div/div[1]/button"
        ]
        sleep_times = [5, 10]
        self.iterate_and_click_by_xpath(
            click_xpaths_list_2,
            sleep_times
        )
        microphone_btn = self.find_element(
            By.XPATH,
            "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[11]/div[3]/div/div[2]/div/button"
        )
        if microphone_btn:
            microphone_btn.click()
