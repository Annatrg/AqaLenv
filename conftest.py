import pytest
# from digift.application import Application
from api.js_test_task import Api
import os.path
import json
from selenium import webdriver
from digift.session import Session

fixture = None

@pytest.fixture(scope='session')
def app():
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    yield wd
    wd.quit()

@pytest.fixture(scope='session')
def load_config():
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "target.json")
    with open(config_file) as f:
        config = json.load(f)
    return config


@pytest.fixture(scope='session')
def app2():
    config = load_config_2()
    fixture = Api(config)
    return fixture

def load_config_2():
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config_for_task2.json')
    with open(config_file) as f:
        config = json.load(f)
    return config
