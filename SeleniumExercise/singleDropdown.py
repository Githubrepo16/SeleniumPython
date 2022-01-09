from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class SimpleDropdown():

    def simple_DD(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://demo.automationtesting.in/Register.html")
        driver.fullscreen_window()
        dropdown = driver.find_element(By.ID, "Skills")
        dd = Select(dropdown)
        dd.select_by_index(5)
        sleep(2)
        dd.select_by_value("Content Management Systems (CMS)")
        sleep(2)
        dd.select_by_visible_text("Engineering")
        sleep(2)
        driver.close()


d = SimpleDropdown()
d.simple_DD()
