from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Demo():

    def locator_id(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://demo.automationtesting.in/")
        print("current URL is :", driver.current_url)
        print("current page title is :", driver.title)
        driver.fullscreen_window()
        sleep(2)
        driver.find_element(By.ID,"btn2").click()
        sleep(1)
        text = driver.find_element(By.XPATH, "//h1[normalize-space()='Automation Demo Site']").text
        print(text)
        sleep(2)
        driver.close()

d = Demo()
d.locator_id()
