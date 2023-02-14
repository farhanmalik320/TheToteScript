from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from seleniumwire import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

@pytest.fixture(params=["chrome"], scope='class')
def setup(request):
    if request.param=="chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("user-data-dir=F:\\testing\\ToteUser")
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--allow-running-insecure-content")
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        web_driver.maximize_window()
    if request.param=="firefox":
        options = Options()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--allow-running-insecure-content")
        web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.fixture(params=["chrome"], scope='class')
def merchant(request):
    if request.param=="chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("user-data-dir=F:\\testing\\ToteMerchant")
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--allow-running-insecure-content")
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        web_driver.maximize_window()
    if request.param=="firefox":
        options = Options()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--allow-running-insecure-content")
        web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    request.cls.driver = web_driver
    yield
    web_driver.close()