class Router:
    def __init__(self):
        self.id = None
        self.table = Table()
        self.key = None
    def Send(self, msg, destination):
        pass
    def Receive(self, msg):
        pass

class Table:
    def __init__(self):
        self.entries =  [Entry()]
        
class Entry:
    def __init__(self):
        self.source = None
        self.message = None
        self.desitation = None
    def Decrypt(encrypted_msg):
        pass
    def Encrypt(decrypted_msg):
        pass

class Message:
    def __init__(self):
        pass

class Catalouge:
    def __init__(self):
        self.entries = [Message()]

class Network:
    def __init__(self):
        self.routers = [Router()]

class Interface:
    def __init__(self):
        self.Catalouge = Catalouge()
        self.Network = Network()
    def buy():
        pass
    def generateRoute():
        pass

class User:
    def __init__(self):
        pass

class World:
    def __init__(self):
        self.Interface = Interface()
        self.users = [User()]
