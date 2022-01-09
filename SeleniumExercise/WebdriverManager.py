from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# from webdriver_manager.firefox import GeckoDriverManager


class Webdrivermanager():

    def drivermanager(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("http://demo.automationtesting.in/")
        driver.close()


d = Webdrivermanager()
d.drivermanager()
