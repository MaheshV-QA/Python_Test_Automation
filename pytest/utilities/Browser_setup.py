import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Browser to run tests: chrome, firefox, edge'
    )

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser').lower()

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge")
    else:
        driver = webdriver.Chrome()
        print(f"Unknown browser '{browser}', launching Chrome by default")

    driver.maximize_window()
    yield driver
    driver.quit()

# pytest HTML reports
def pytest_html_report_title(report):
    report.title = "Test Execution Report (OrangeHRM)"


def pytest_configure(config):
    config.stash[metadata_key]["Project"] = "OrangeHRM"
    config.stash[metadata_key]["Module"] = "PIM"
    config.stash[metadata_key]["Tester"] = "Silas Francis"


def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
    metadata.pop('Packages', None)
    metadata.pop('Platform', None)

