from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Set up WebDriver for Edge
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# Open the website
url = "https://demoqa.com/"
driver.get(url)
driver.maximize_window()

try:
    # Use WebDriverWait for element visibility and click it
    wait = WebDriverWait(driver, 10)
    alert_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[.='Alerts, Frame & Windows']")))
    alert_element.click()

    # Adding a wait to ensure the next element is loaded or visible
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='element-list collapse show']//span[.='Alerts']")))

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()
