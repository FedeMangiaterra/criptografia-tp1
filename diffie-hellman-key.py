from eliptic_curve_point import ElipticCurvePoint
from finite_field_element import FiniteFieldElement

class DiffieHellmanPeer:
    def __init__(self, x, y, a, b, private_key):
        self.generator = ElipticCurvePoint(x, y, a, b)
        self.private_key = private_key
        self.public_key = private_key * self.generator
        self.peer_public_key = None
    
    def send_key(self, peer):
        peer.peer_public_key = self.public_key

    def calculate_secret(self):
        secret = self.private_key * self.peer_public_key
