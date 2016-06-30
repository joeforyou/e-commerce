from system.core.controller import *

class Rides(Controller):
    def __init__(self, action):
        super(Rides, self).__init__(action)
        self.load_model('User')
        self.db = self._app.db

    def index(self):
        return self.load_view('profilepage.html')

    def postneed(self):
    	extract_to_zip_code = request.form['to'].split(" ")
    	extract_from_zip_code = request.form['from'].split(" ")
    	temp = {
    		'to_zip': extract_to_zip_code[len(extract_to_zip_code) - 1]
    		'from_zip': extract_from_zip_code[len(extract_from_zip_code) -1]
    		'destination': request.form['to'].split(" ")
    		'pickup': request.form['from'].split(" ")
    	}
    	self.load_model['Ride'].postneed(temp)
    	return self.load_view('profile.html')

    def load_profile(self):
    	session['currentUser']['id'] = current_user_id
    	offers_requests = self.load_model['Ride'].load_profile('current_user_id')
    	self.load_view('profile.html', offers_requests=offers_requests)
