from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Demo():

    def locator_id(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://demo.automationtesting.in/")
        driver.fullscreen_window()
        sleep(2)
        valueOfClass = driver.find_element(By.ID, "btn2").get_attribute("class")
        print("valueOfClass :" + valueOfClass)
        sleep(2)
        driver.close()


d = Demo()
d.locator_id()
