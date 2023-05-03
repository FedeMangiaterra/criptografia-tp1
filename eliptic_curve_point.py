class ElipticCurvePoint:
    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.y**2 != self.x**3 + a * x + b: 
            raise ValueError(f'({x}, {y}) is not on the curve')

    def __eq__(self, other): 
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

    def __add__(self, other):
        return
    
    def duplicate(self):
        return