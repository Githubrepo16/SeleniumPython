import time

import webdriver_manager.firefox
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoCalender():

    def handle_calnder(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.qatarairways.com/en-gb/homepage.html?")
        driver.maximize_window()
        time.sleep(2)
        departure_textbox = driver.find_element(By.XPATH,"//span[contains(@class,'twitter-typeahead')]//input[@id='bw-from']")
        departure_textbox.click()
        departure_textbox.send_keys("London")
        all_options = driver.find_element(By.XPATH, "(//a[@id='all-tab'])[1]")
        print(all_options.get_attribute("class"))
        print(all_options.text)
        time.sleep(3)
        all_options.click()
        time.sleep(3)
        # all = driver.find_elements(By.XPATH, "//div[contains(@class,'suggestion-list')]")
        all = driver.find_elements(By.XPATH, "//div[contains(@class,'suggestion-list')]//div")
        print(len(all))
        for i in all:
            if "Gatwick Airport(LGW)" in all.text:
                i.click()
                break

        # print(all)
        # for city in all:
        #     if city.get_attribute("class").text == "Stansted Airport(STN)":
        #         city.click()
        #         break
        #     else:
        #         print("Cannot find a city")
        #         break
        time.sleep(2)
        driver.close()

dc = DemoCalender()
dc.handle_calnder()


