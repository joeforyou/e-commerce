from system.core.model import Model


class Ride(Model):
    def __init__(self):
        super(Ride, self).__init__()

    def load_profile(self, user_id):
    	data = {'user_id': user_id}
    	query = "SELECT * FROM requests WHERE :user_id = request['user_id']"
    	ride_requests = self.db.query_db(query, data)
    	query = "SELECT * FROM offers WHERE :user_id = offer['user_id']"
    	ride_offers = self.db.query_db(query, data)
    	return [ride_request, ride_offers]
    def postneed(self, data)
    	query = "INSERT INTO requests (to_zip, from_zip, pickup, destination) VALUES (:to_zip, :from_zip, :pickup, :destination)"
    	return self.db.query_db(query, data)
