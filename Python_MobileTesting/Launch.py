from appium import webdriver
import time
import os

def open_command_prompt_and_launch_appium():
    os.system("start cmd /C appium --base-path /wd/hub --relaxed-security --log-timestamp")  # Opens command prompt and starts Appium server with specified flags

def close_command_prompt():
    os.system("taskkill /f /im cmd.exe")  # Closes command prompt

def launch_app():
    try:
        # Define Desired Capabilities
        desired_capabilities = {
            "platformName": "Android",  # Change to "iOS" for iOS devices
            "platformVersion": "13",  # Adjust according to your device version
            "deviceName": "emulator-5554",  # Change to your actual device name
            # "app": "path/to/your/app.apk",  # Path to the application file
            "automationName": "UiAutomator2",  # Use XCUITest for iOS
            "appPackage": "com.android.car.settings",  # Replace with your app package
            "appActivity": "com.android.car.settings.Settings_Launcher_Homepage",  # Replace with your main activity
            "noReset": True  # Prevents clearing app data
        }

        # Start Appium session
        appium_server_url = "http://localhost:4723/wd/hub"  # Appium server URL
        driver = webdriver.Remote(appium_server_url, desired_capabilities)
        
        driver.implicitly_wait(10)  # Set implicit wait time to 10 seconds
        # Wait for a few seconds to see the app launch
        time.sleep(5)
        
        # Perform any additional actions here
        
    except Exception as e:
        print(f"An error occurred: {e}")


# Call the functions
if __name__ == "__main__":
    open_command_prompt_and_launch_appium()
    time.sleep(10)  # Give some time for the Appium server to start
    launch_app()
    time.sleep(5)  
    close_command_prompt()