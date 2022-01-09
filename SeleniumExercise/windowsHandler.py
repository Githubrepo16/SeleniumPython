from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class WindowsHandler():

    def windows_handler(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://demo.automationtesting.in/Windows.html")
        driver.maximize_window()
        # This is for opening a new window in a new tab
        print("Parent Page Title is :", driver.title)
        driver.find_element(By.LINK_TEXT, "Open New Tabbed Windows").click()
        sleep(1)
        parent_handler = driver.current_window_handle
        print("This is the current window handler: ", parent_handler)
        sleep(2)
        driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()
        all_handles = driver.window_handles
        print("This is the second window handler: ", all_handles)
        for i in all_handles:
            if i != parent_handler:
                driver.switch_to.window(i)
                print("Tabbed Page Title is :", driver.title)
                sleep(2)
                driver.close()
                break
        driver.switch_to.window(parent_handler)
        # This is for opening a new window in a separate window
        driver.find_element(By.LINK_TEXT, "Open New Seperate Windows").click()
        sleep(1)
        parent_handler = driver.current_window_handle
        driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
        all_handles = driver.window_handles
        print(all_handles)
        for i in all_handles:
            if i != parent_handler:
                driver.switch_to.window(i)
                print("New window Page Title is :", driver.title)
                sleep(2)
                driver.close()
                break
        driver.switch_to.window(parent_handler)
        sleep(2)
        # This is for opening in a separate multiple tabs
        driver.find_element(By.CSS_SELECTOR,".analystic[href='#Multiple']").click()
        sleep(1)
        parent_handler = driver.current_window_handle
        driver.find_element(By.XPATH,"//button[@onclick='multiwindow()']").click()
        all_handles = driver.window_handles
        print(all_handles)
        for i in all_handles:
            if i != parent_handler:
                driver.switch_to.window(i)
                print("Multiple window first Page Title is :", driver.title)
                sleep(2)
                driver.close()
                break
        driver.switch_to.window(parent_handler)
        sleep(2)
        driver.close()


d = WindowsHandler()
d.windows_handler()
