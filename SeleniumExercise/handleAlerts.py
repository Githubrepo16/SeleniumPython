from time import sleep
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class handleAlerts():

    def alert_box(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR,"input[value='Show alert box']").click()
        sleep(2)
        print(Alert(driver).text)
        Alert(driver).accept()
        sleep(2)
        driver.close()

    def confirm_alert(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
        driver.maximize_window()
        sleep(2)
        driver.find_element(By.ID,"confirmexample").click()
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.accept()
        sleep(2)
        print(driver.find_element(By.ID, "confirmreturn").text)
        print(driver.find_element(By.ID,"confirmexplanation").text)
        sleep(2)

        driver.find_element(By.ID, "confirmexample").click()
        driver.switch_to.alert.dismiss()
        sleep(2)
        print(driver.find_element(By.ID, "confirmreturn").text)
        print(driver.find_element(By.ID, "confirmexplanation").text)
        sleep(2)
        driver.close()

    def prompt_alert(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
        driver.maximize_window()
        sleep(2)
        driver.find_element(By.ID, "promptexample").click()
        sleep(2)
        print(Alert(driver).text)
        # Alert(driver).send_keys("Test")
        driver.switch_to.alert.send_keys("TestMe")
        sleep(2)
        Alert(driver).accept()
        sleep(2)
        print(driver.find_element(By.ID, "promptreturn").text)
        print(driver.find_element(By.ID, "promptexplanation").text)
        sleep(2)

        driver.find_element(By.ID, "promptexample").click()
        Alert(driver).dismiss()
        sleep(2)
        print(driver.find_element(By.ID, "promptreturn").text)
        print(driver.find_element(By.ID, "promptexplanation").text)
        sleep(2)
        driver.close()


ha = handleAlerts()
ha.alert_box()
ha.confirm_alert()
ha.prompt_alert()
