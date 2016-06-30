from system.core.model import Model

import re

NAME_REGEX = re.compile(r'^[a-zA-Z]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASS_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    
    def registerUser(self, userData):
        hasErrors = False
        if len(userData['email']) < 1:
            hasErrors = True
        elif not EMAIL_REGEX.match(userData['email']):
            hasErrors = True
        elif not NAME_REGEX.match(userData['firstName']):
            hasErrors = True
        elif not NAME_REGEX.match(userData['lastName']):
            hasErrors = True
        elif not PASS_REGEX.match(userData['password']):
            hasErrors = True
        elif userData['password'] != userData['confirmPassword']:
            hasErrors = True
        elif userData['phoneNumber'] == None:
            hasErrors = True
        elif hasErrors == False:
            query = 'INSERT INTO user (email, first_name, last_name, password, phone_number) VALUES (:email, :firstName, :lastName, :password, :phoneNumber)'
            data = {
                'email': userData['email'],
                'firstName': userData['firstName'],
                'lastName': userData['lastName'],
                'password': userData['password'],
                'phoneNumber': userData['phoneNumber']
                }
            return self.db.query_db(query, data)
        else:
            return False

    def loginUser(self, userData):
        hasErrors = False
        if len(userData['email']) < 1:
            hasErrors = True
        elif not EMAIL_REGEX.match(userData['email']):
            hasErrors = True
        elif hasErrors == False:
            query = "SELECT * FROM user WHERE email = :email AND password = :password"
            data = {'email': userData['email'],'password': userData['password']}
            return self.db.query_db(query, data)
        else:
            return False
    def load_results(self, destination)
        data = { 
            'request.to_zip': destination[:-5]
            }
        query = "SELECT * FROM (SELECT * FROM offers WHERE :to_zip = offer.to_zip) WHERE offer.interest NOT >= offer.seat"
        return self.db.query_db(query, data)

