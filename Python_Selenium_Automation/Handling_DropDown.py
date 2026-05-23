from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open demo page
url = "https://demoqa.com/select-menu"
driver.get(url)
driver.maximize_window()

# **Implicit Wait** - Applies to all element searches
driver.implicitly_wait(5)  # Wait up to 5 seconds for elements to be available

# Locate the "Widgets" section and click
widgets = driver.find_element(By.XPATH, "//span[.='Widgets']")
widgets.click()

time.sleep(100)
