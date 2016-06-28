from system.core.controller import *

class Rides(Controller):
    def __init__(self, action):
        super(Rides, self).__init__(action)
        self.load_model('User')
        self.db = self._app.db

    def index(self):
        return self.load_view('profilepage.html')

    def postneed(self):
    	return self.load_view('postneed.html')