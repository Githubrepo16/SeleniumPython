from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DriverMethods():

    def dmethods(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://demo.automationtesting.in/")
        print("current URL is :", driver.current_url)
        print("current page title is :", driver.title)
        driver.fullscreen_window()
        sleep(2)
        driver.minimize_window()
        sleep(4)
        driver.maximize_window()
        sleep(2)
        driver.find_element(By.ID,"btn2").click()
        driver.refresh()
        print("current page title is :", driver.title)
        driver.back()
        print("current page title is :", driver.title)
        sleep(2)
        driver.forward()
        print("current page title is :", driver.title)
        sleep(2)
        driver.close()


d = DriverMethods()
d.dmethods()
