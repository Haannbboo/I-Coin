import requests
import hashlib as hl
import socket
import rsa


class API:
    ip = socket.gethostbyname(socket.gethostname())
    def __init__(self):
        self.ip = ip if 'http://' in ip else 'http://'+ip
        self.public_key = None

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
            self.private = private

    def Transaction(self, recipient=None, amount=None, private_key=None):
        sender = self.account
        params = {'sender': sender, 'recipient': recipient, 'amount': amount}
        _, code = self._authorize_transaction(params, private_key)
        # check amount
        _, code = requests.post('/'.join(self.ip, 'transactions/new'),
                                json = params)
        if code == 400:
            return "Missing values"

    def Resolve(self):
        _, code = requests.get('/',join(self.ip, '/nodes/resolve'))
        if code == 200:
            return

    def _authorize_transaction(self, trans_msg, private_key):
        if self.public_key is None:
            return "Missing public key", 400

        signature = rsa.sign(trans_msg.encode(), private_key, 'SHA-256')
        try:
            rsa.verify(trans_msg.encode(), signature, self.public_key)
            return "Verify succeed", 200
        except rsa.pkcs1.VerificationError:
            return "Verify failed", 502

        
