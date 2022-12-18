import pytest
from fixture.application import Application
from fixture_2.js_test_task import Api
import os.path
import json

fixture = None


@pytest.fixture
def app(request):
    web_config = load_config()
    fixture = Application(base_url=web_config["baseUrl"])
    fixture.session.basic_auth(login=web_config["login"], password=web_config["password"])
    return fixture

def load_config():
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "target.json")
    with open(config_file) as f:
        config = json.load(f)
    return config


@pytest.fixture(scope='session')
def config_task2():
    config = load_config_task2()
    fixture = Api(config)
    return fixture

def load_config_task2():
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config_for_task2.json')
    with open(config_file) as f:
        config = json.load(f)
    return config