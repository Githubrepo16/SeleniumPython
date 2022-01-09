from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class IsHidden():

    def elementHidden(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://training.openspan.com/")
        driver.fullscreen_window()
        state = driver.find_element(By.ID,"login_button").is_enabled()
        print("Status :", state)
        sleep(2)
        driver.close()

d = IsHidden()
d.elementHidden()

