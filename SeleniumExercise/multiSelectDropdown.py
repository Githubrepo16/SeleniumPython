from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class MultiDropdown():

    def multi_DD(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html")
        driver.fullscreen_window()
        dropdown = driver.find_element(By.ID, "ide")
        dd = Select(dropdown)
        dd.select_by_index(0)
        sleep(2)
        dd.select_by_value("vs")
        sleep(2)
        dd.select_by_visible_text("NetBeans")
        sleep(2)
        dd.deselect_by_index(3)
        sleep(2)
        dd.deselect_by_value("nb")
        sleep(2)
        dd.deselect_by_visible_text("Eclipse")
        sleep(2)
        dd.select_by_index(1)
        dd.select_by_index(2)
        dd.select_by_index(3)
        dd.select_by_index(0)
        sleep(2)
        dd.deselect_all()
        sleep(2)
        driver.close()


d = MultiDropdown()
d.multi_DD()
