import requests
from model.jstesttask import JsTestTask

class Api:

    def __init__(self, config):
        self.base_url = config['baseUrl']
        self.method = config['method']
        self.search = config['search']
        self.sort_field = config['sort_field']

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
           # list.append(JsTestTask(name=name, image=image, price=price))
        return list
