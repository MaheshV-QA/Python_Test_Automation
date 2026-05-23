import pytest
from selenium import webdriver
from utilities.ReadProperties import ReadConfig
from utilities.customLogger import LogGen
from PageObjects.Login import LoginPage
from utilities.Browser_setup import setup

@pytest.mark.usefixtures("setup")
class Test_Login():
    url = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_hometitle(self):
        self.logger.info("*************** Starting HomePage Title Test ***************")
        driver = setup
        # url = self.url
        driver.get(self.url)
        page_title =driver.title
        if page_title == "OrangeHRM":
            assert True
            self.logger.info("***************Home Page Title Test Passed ***************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("*************** Home Page Title Test Failed ***************")
            assert False
        self.logger.info("*************** Finished Home Page Title Test ***************")



    




