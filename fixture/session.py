
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def basic_auth(self, login, password):
        wd = self.app.wd
        wd.get(f"http://{login}:{password}@{self.app.base_url}")
