from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class AutoSuggestDropdown():

    def full_text(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://demo.automationtesting.in/Register.html")
        driver.fullscreen_window()
        try:
            element = driver.find_element(By.XPATH, "//span[@role='combobox']")
            element.click()
            sleep(2)
            textbox = driver.find_element(By.XPATH, "//input[@role='textbox']")
            textbox.send_keys("New Zealand")
            sleep(2)
            textbox.send_keys(Keys.ENTER)
            sleep(2)
        except Exception as ex:
            print(ex)
        driver.close()

    def half_text(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://demo.automationtesting.in/Register.html")
        driver.fullscreen_window()
        try:
            element = driver.find_element(By.XPATH, "//span[@role='combobox']")
            element.click()
            sleep(2)
            textbox = driver.find_element(By.XPATH, "//input[@role='textbox']")
            textbox.send_keys("Ne")
            sleep(2)
            search_results = driver.find_elements(By.XPATH, "//span[@class='select2-results']/ul/li")
            sleep(2)
            print(len(search_results))
            for result in search_results:
                if "Netherlands" in result.text:
                    result.click()
                    sleep(2)
                    break
            sleep(2)
        except Exception as ex:
            print(ex)

        driver.close()


d = AutoSuggestDropdown()
d.full_text()
d.half_text()
