class User():
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
        
    def json(self):
        return {
    'email': self.email,
    'username': self.username,
    'password': self.password
    }

    
class Task():
    def __init__(self, help, username, accepted = False, acceptor = None ):
        self.help=help
        self.taskauthor=username
        self.accepted = accepted
        self.acceptor = acceptor

    def json(self):
        return{
            'help': self.help,
            'taskauthor':self.taskauthor,
            'accepted':self.accepted,
            'acceptor':self.acceptor
        }
