from selenium import webdriver
from selenium.webdriver.common.by import By  # Missing import
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def launch_orangehrm():
    # Set up WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Open OrangeHRM login page
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)

    return driver  # Return the driver so you can use it elsewhere

def login_orangehrm(driver, username, password):
    # Locate username and password fields
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Enter login credentials
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the form by clicking the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Wait and verify login success
    time.sleep(5)   
def verify_Title(driver,ExpectedTitle):
    # Verify the page title after login
    actual_title = driver.title
    print("Expected title: ", ExpectedTitle)
    print("Actual title: ", actual_title)
    if actual_title == ExpectedTitle:
        print("Login successful!")
    else:
        print("Login failed. Expected title: {}, Actual title: {}".format(ExpectedTitle, actual_title))

      
def scroll_to_click_element(driver, xpath):
    try:
        element = driver.find_element(By.XPATH, xpath)
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
        time.sleep(2)
    except Exception as e:
        print(f"Error scrolling to element: {e}")

def click_element(driver, xpath):
    try:
        element = driver.find_element(By.XPATH, xpath)
        element.click()
    except Exception as e:
        print(f"Error clicking element: {e}")

def take_screenshot(driver, filename):
    # Take a screenshot and save it to the specified filename
    driver.save_screenshot(filename)


# Example usage
if __name__ == "__main__":
    driver = launch_orangehrm()
    login_orangehrm(driver, "Admin", "admin123")
    verify_Title(driver,"OrangeHRM")
    click_element(driver, "//a[.='My Info']")
    scroll_to_click_element(driver, "//a[.='(1) Record Found']")


