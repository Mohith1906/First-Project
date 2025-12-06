import pytest
from selenium import webdriver
from Utilities import Read_Configurations

# Add optional imports for webdriver-manager to auto-download matching drivers
try:
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from selenium.webdriver.edge.service import Service as EdgeService
    WEBDRIVER_MANAGER_AVAILABLE = True
except Exception:
    WEBDRIVER_MANAGER_AVAILABLE = False

@pytest.fixture
def setup_and_teardown(request):
    browser = Read_Configurations.read_configurations("basic_info","browser")
    driver = None
    if browser.__eq__("chrome"):
        if WEBDRIVER_MANAGER_AVAILABLE:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        else:
            # Fall back to Selenium default (Selenium Manager) or chromedriver in PATH
            driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        if WEBDRIVER_MANAGER_AVAILABLE:
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        if WEBDRIVER_MANAGER_AVAILABLE:
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            driver = webdriver.Edge()
    else:
        print("Provide a valis browser name from this list chrome/firefox/edge")
    driver.maximize_window()
    driver.implicitly_wait(10)
    app_url = Read_Configurations.read_configurations("basic_info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
