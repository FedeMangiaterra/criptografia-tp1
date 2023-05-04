from finite_field_element import FiniteFieldElement

class ElipticCurvePoint:
    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None: 
            return
        if self.y**2 != self.x**3 + a * x + b: 
            raise ValueError(f'({x}, {y}) is not on the curve')

    def __eq__(self, other): 
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError(f'Points {self}, {other} are not on the same curve')
        # Elemento neutro
        if self.x is None:
            return other
        if other.x is None:
            return self
        
        #Inverso aditivo
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)
        
        #Mismo punto con y = 0 (tangente vertical)
        if self == other and self.y == 0:
            return self.__class__(None, None, self.a, self.b)
        
        #Mismo punto con y distinto de 0
        if self == other:
            slope = (3 * (self.x ** 2) + self.a) / 2 * self.y
            new_x = slope ** 2 - 2 * self.x
            new_y = slope * (self.x - new_x) - self.y
            return self.__class__(new_x, new_y, self.a, self.b)
        
        #Suma de puntos con distinto x, distinto y
        slope = (other.y - self.y) / (other.x - self.x)
        new_x = slope ** 2 - self.x - other.x
        new_y = slope * (self.x - new_x) - self.y
        return self.__class__(new_x, new_y, self.a, self.b)

def main():
    p = 1021
    a = FiniteFieldElement(-3, p)
    b = FiniteFieldElement(-3, p)
    points_amount = 1 #Point at infinity
    for i in range(0, p):
        for j in range(0, p):
            x = FiniteFieldElement(i, p)
            y = FiniteFieldElement(j, p)
            try:
                point = ElipticCurvePoint(x, y, a, b)
                points_amount += 1
                print(f"({x.number}, {y.number}) is on the curve")
            except ValueError:
                continue
    print(f"The curve has {points_amount} points")
    return

main()