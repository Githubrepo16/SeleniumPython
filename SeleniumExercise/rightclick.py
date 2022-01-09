from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class RightClick():

    def right_click(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        sleep(10)
        driver.maximize_window()
        sleep(2)
        ac = ActionChains(driver)
        button_one = driver.find_element(By.CSS_SELECTOR, ".context-menu-one.btn.btn-neutral")
        ac.context_click(button_one).perform()
        sleep(2)
        driver.close()

rc = RightClick()
rc.right_click()
