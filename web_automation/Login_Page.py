"""
findElement() is used to get the address of first matching element on the webpage
==>Returntype is WebElement interface
==>If element unable to find we get "NoSuchElementException"

findElements() is used to get the address of all the matching elements on the webpage
==>Returntype is List<WebElement> interface
==>If element unable to find we get "emptyList"


"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open OrangeHRM login page
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
driver.maximize_window()

# Wait for the page to load
time.sleep(2)  # Explicit waits are better, but this is a simple example

# Locate username and password fields
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

# Enter login credentials
username_field.send_keys("Admin")
password_field.send_keys("admin123")

# Submit the form by clicking the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait and verify login success
time.sleep(5)

Actual_Title=driver.title
Excpted_Title = "OrangeHRM"

if Actual_Title == Excpted_Title:
    print(Actual_Title,Excpted_Title , "are same")

else :
    print(print(Actual_Title,Excpted_Title , "are not  same"))
print("Login script executed successfully!")


