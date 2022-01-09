from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class IsEnabled():

    def elementDisabled(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://training.openspan.com/")
        driver.fullscreen_window()
        state = driver.find_element(By.ID,"login_button").is_enabled()
        print("Status :", state)
        sleep(2)
        driver.close()

    def elementEnabled(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://training.openspan.com/")
        driver.fullscreen_window()
        driver.find_element(By.NAME, "user_name").send_keys("Test")
        driver.find_element(By.NAME, "user_pass").send_keys("Test")
        state = driver.find_element(By.ID,"login_button").is_enabled()
        print("Status :", state)
        sleep(2)
        driver.close()

d = IsEnabled()
d.elementDisabled()
d.elementEnabled()
