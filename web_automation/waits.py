"""
# Types of Waits in Selenium:
1. Implicit Wait:
   - Automatically waits for a specified amount of time when searching for elements before throwing an exception.
   - No need to give any condition and declare as one time its method it will work all find elemetnt and fine elements
   -no object need of creation.
   -if element not found within maximm time, we get NoSuchElementException/EmptyList

2. Explicit Wait:
   - Waits for a specific condition to occur (like visibility or clickability of an element) for a defined period.
   -We create an object of WebDriverWait class
   -We should provide condition according to the situation
    -In ExplicitlyWait, if condition does not become true within maximum time, then we get TimeoutException

3. Static Wait (time.sleep):
   - Halts execution for a fixed amount of time regardless of the browser state (generally less preferred).
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open OrangeHRM login page
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
driver.maximize_window()

# **Implicit Wait** - Applies to all element searches
driver.implicitly_wait(5)  # Wait up to 5 seconds for elements to be available

# Locate username and password fields
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

# Enter login credentials
username_field.send_keys("Admin")
password_field.send_keys("admin123")

# **Explicit Wait** - Wait for the login button to be clickable
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds for the condition
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

# **Static Wait (Not Recommended)** - Explicit time wait
time.sleep(5)  # Only use if other wait mechanisms don't work

# **Page Load Wait** - Wait until page title changes (used here after login)
wait.until(EC.title_contains("OrangeHRM"))

# Verify login success by checking the page title
Actual_Title = driver.title
Expected_Title = "OrangeHRM"

if Actual_Title == Expected_Title:
    print(f"{Actual_Title} and {Expected_Title} are the same")
else:
    print(f"{Actual_Title} and {Expected_Title} are not the same")

print("Login script executed successfully!")

# Close the browser
driver.quit()
