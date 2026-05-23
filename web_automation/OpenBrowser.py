from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class BrowserAutomation:
    def __init__(self):
        self.driver = None
        
    def open_and_maximize(self, url):
        # Set up Edge driver using WebDriver Manager
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

        # Maximize the browser window
        self.driver.maximize_window()

        # Open the specified URL
        self.driver.get(url)


