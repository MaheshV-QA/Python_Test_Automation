import pytest
from utilities.ReadProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Login:
    url = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_hometitle(self, setup):
        self.logger.info("Starting Home Page Title Test")
        driver = setup
        driver.get(self.url)

        page_title = driver.title
        if page_title == "OrangeHRM":
            self.logger.info("Home Page Title Test Passed")
        else:
            driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")
            self.logger.error("Home Page Title Test Failed")
            pytest.fail("Home Page Title did not match expected value")

        self.logger.info("Finished Home Page Title Test")



    




