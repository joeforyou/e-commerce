from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def login(self):
        self.load_model('User')
        userArray = self.models['User'].loginUser(request.form)
        if userArray:
            session['currentUser'] = userArray[0]
            return redirect('/profile')
        else:
            flash('Failed to login! Please try again.')
            return redirect('/')

    def signup(self):
        return self.load_view('register.html')

    def register(self):
        self.load_model('User')
        userArray = self.models['User'].registerUser(request.form)
        if userArray:
            return redirect('/')
        else:
            flash('Failed to register. Password must contain eight characters including one uppercase letter and one number. Please try again.')
            return redirect('/')

    def logout(self):
        session.pop('currentUser', None)
        return redirect('/')

    def load_results(self, to):
        res = self.models['User'].load_results('to')
        self.load_view('results.html', results=res)
            
