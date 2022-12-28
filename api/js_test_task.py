
import requests
from model.jstesttask import JsTestTask

class Api:

    def __init__(self, config):
        self.base_url = config["js_test_task"]['baseUrl']
        self.method = config["js_test_task"]['method']
        self.search = config["js_test_task"]['search']
        self.sort_field = config["js_test_task"]['sort_field']

    def get_results(self, search='', sort_field=''):
        if search != '':
            search_product = (self.search + search)
        else:
            search_product = ''
        if sort_field != '':
            sort = (self.sort_field + sort_field)
        else:
            sort = ''
        response = requests.get(f'{self.base_url}{self.method}?{search_product}&{sort}')
        list = []
        for search in response.json()['products']:
            list.append(JsTestTask.parse_obj(search))
        return list
