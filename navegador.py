from selenium import webdriver

class Navegador():
    def __init__(self) -> None:
        driver = webdriver.Chrome()
        driver.get("http://selenium.dev")
        driver.quit

