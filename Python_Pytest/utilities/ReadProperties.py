import configparser

config = configparser.RawConfigParser()
config.read(".\\config\\config.ini")

class ReadBrowser():

    @staticmethod
    def getbrowser():
        browser = config.get('browser info', 'browser')
        return browser
    
class ReadConfig():
    @staticmethod
    def getURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

class ReadConfigUser():
    @staticmethod
    def getUsername():
        username = config.get('user info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('user info', 'password')
        return password