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
            return {'public_key': self.public_key,
                    'private_key': self.private_key}

    def Transaction(self, recipient=None, amount=None, private_key=None):
        sender = self.account
        params = {'sender': sender, 'recipient': recipient, 'amount': amount}
        _, code = self._authorize_transaction(params, private_key)
        if code == 502:
            return "Verification failed"
        elif code != 200:
            return "Something wrong with verification"
        # check amount
        _, code = requests.post('/'.join(self.ip, 'transactions/new'),
                                json = params)
        if code == 400:
            return "Missing values"
        else:
            return "Transcation made"

    def Resolve(self):
        response, code = requests.get('/',join(self.ip, 'nodes/resolve'))
        if code == 200:
            return response

    def Wallet(self, public_key, private_key):
        response, code = requests.post('/'.join(self.ip, '/wallet'), json=params)
        if code == 201:
            return response  # and something else

    def _authorize_transaction(self, trans_msg, private_key):
        if self.public_key is None:
            return "Missing public key", 400

        signature = rsa.sign(trans_msg.encode(), private_key, 'SHA-256')
        try:
            rsa.verify(trans_msg.encode(), signature, self.public_key)
            return "Verify succeed", 200
        except rsa.pkcs1.VerificationError:
            return "Verify failed", 502

        
