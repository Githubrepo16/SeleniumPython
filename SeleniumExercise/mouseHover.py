from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MouseHover():

    def mouse_hover(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://testpages.herokuapp.com/styled/csspseudo/css-hover.html")
        driver.maximize_window()
        sleep(2)
        # driver.find_element(By.ID, "hoverpara").click() # if use this need to remove ActionChains implementation
        button_one= driver.find_element(By.ID, "hoverpara")
        ac = ActionChains(driver)
        ac.move_to_element(button_one).perform()
        sleep(2)
        hover_para = driver.find_element(By.ID, "hoverparaeffect").text
        print(hover_para)
        sleep(2)


        # driver.find_element(By.ID, "hoverdivpara").click() # if use this need to remove ActionChains implementation
        button_two = driver.find_element(By.ID, "hoverdivpara")
        ac.move_to_element(button_two).perform()
        sleep(4)
        hover_div_para = driver.find_element(By.ID, "hoverdivparaeffect").text
        print(hover_div_para)
        hover_div_link = driver.find_element(By.ID, "hoverlink")
        print(hover_div_link.text)
        hover_div_link.click()
        # ac.click(hover_div_link).perform() # this way also work
        sleep(2)
        print(driver.find_element(By.CLASS_NAME, "explanation").text)
        sleep(2)
        driver.find_element(By.ID, "returnlink").click()
        sleep(2)
        page_title = driver.title
        print(page_title)
        driver.close()

mh = MouseHover()
mh.mouse_hover()