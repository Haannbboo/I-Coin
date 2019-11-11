import requests
import hashlib as hl
from urllib import urlencode
import socket
import rsa


class DynamicMain:
    ip = socket.gethostbyname(socket.gethostname())
    def __init__(self):
        self.ip =  if 'http://' in ip else 'http://'+ip

    def Mine(self):
        _, code = requests.get('/'.join(self.ip, 'mine'))
        if code == 200:
            return

    def Register(self):
        public, private = rsa.newkeys(1024)
        self.account = public
        # data = 
        _, code = requests.post('/'.join(self.ip, 'nodes', 'register'), json=data)
        if code == 201:
            return private

    def Transaction(self, recipient=None, amount=None, key=None):
        sender = self.account
        params = {'sender': sender, 'recipient': recipient, 'amount': amount}
        # check signature
        # check amount
        _, code = requests.post('/'.join(self.ip, 'transactions/new'),
                                json = params)
        if code == 400:
            return "Missing values"

    def _check_signature(self, key):
        pass
