from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class HandleIframe():

    def handle_iframe(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/")
        driver.maximize_window()
        driver.find_element(By.ID, "iFrame").click()
        driver.switch_to.frame(3)
        #driver.switch_to.frame(driver.find_element(By.TAG_NAME,"iframe")[3])
        sleep(2)
        driver.find_element(By.CSS_SELECTOR,"img[alt='Selenium Online Training']").click()
        sleep(2)
        print(driver.title)
        sleep(2)

ifr = HandleIframe()
ifr.handle_iframe()
