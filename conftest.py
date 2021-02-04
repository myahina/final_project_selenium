import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


'''def pytest_addoption(parser):                                            
    parser.addoption('--language', action='store', default= "en",
                     help="Enter language: es")
'''

@pytest.fixture(scope="function")                               
def browser(request):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
    browser = webdriver.Chrome(options=options)
    print("\nstart browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()