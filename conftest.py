import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                      help='Choose site language')

@pytest.fixture()
def browser(request):
    user_lang = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(20.0)
    if user_lang == 'es':
        print("\n Run test on Espaniol")
    elif user_lang != "es":
        print("\n Run test on English")
        user_lang = 'en'
    yield browser
    print("\nquit browser..")
    browser.quit()