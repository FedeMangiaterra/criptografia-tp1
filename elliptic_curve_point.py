'''Implementar un tipo de dato para puntos de una curva elíptica, junto con las operaciones de grupo
(suma de puntos distintos y duplicación de puntos), utilizando la forma de Weierstrass. Hacer pruebas
con la curva y 2=x 3 -3x-3 y p=1021, determinando la cantidad de puntos que tiene la curva. Usando P=(379,1011), 
obtener kP, siendo k=655.'''
from finite_field_element import FiniteFieldElement

class EllipticCurvePoint:
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
        if self == other and self.y == 0 * self.x:
            return self.__class__(None, None, self.a, self.b)
        
        #Mismo punto con y distinto de 0
        if self == other:
            slope = (3 * (self.x ** 2) + self.a) / (2 * self.y)
            new_x = slope ** 2 - 2 * self.x
            new_y = slope * (self.x - new_x) - self.y
            return self.__class__(new_x, new_y, self.a, self.b)
        
        #Suma de puntos con distinto x, distinto y
        slope = (other.y - self.y) / (other.x - self.x)
        new_x = slope ** 2 - self.x - other.x
        new_y = slope * (self.x - new_x) - self.y
        return self.__class__(new_x, new_y, self.a, self.b)
    
    def __rmul__(self, coefficient):
        coef = coefficient
        current = self 
        result = self.__class__(None, None, self.a, self.b) 
        while coef:
            if coef & 1: 
                result += current
            current += current 
            coef >>= 1 
        return result
    
    def get_curve_size(self, prime):
        points_amount = 1 #Punto en el infinito
        for i in range(0, prime):
            for j in range(0, prime):
                x = FiniteFieldElement(i, prime)
                y = FiniteFieldElement(j, prime)
                try:
                    point = self.__class__(x, y, self.a, self.b)
                    points_amount += 1
                except ValueError:
                    continue
        return points_amount

    def get_subgroup(self):
        order = 0
        finished_cycling = False
        subgroup = []
        while not finished_cycling:
            order += 1
            point = order * self
            subgroup.append(point)
            if point == self.__class__(None, None, self.a, self.b):
                finished_cycling = True
        return subgroup, order
    
    def print_info(self):
        if type(self.x) == FiniteFieldElement:
            return (f"({self.x.number}, {self.y.number}) mod {self.x.prime}")
        else:
            return (f"({self.x}, {self.y})")

def main():
    p = 1021
    a = FiniteFieldElement(-3, p)
    b = FiniteFieldElement(-3, p)

    #Calculo cantidad de puntos en la curva
    points_amount = 1 #Punto en el infinito
    for i in range(0, p):
        for j in range(0, p):
            x = FiniteFieldElement(i, p)
            y = FiniteFieldElement(j, p)
            try:
                point = EllipticCurvePoint(x, y, a, b)
                points_amount += 1
                #print(f"({x.number}, {y.number}) is on the curve")
            except ValueError:
                continue
    print(f"The curve has {points_amount} points")

    #Calculo kP
    x = FiniteFieldElement(379, p)
    y = FiniteFieldElement(1011, p)
    k = 655
    point = EllipticCurvePoint(x, y, a, b)
    kP = (k * point)
    print(f"kP with P=({x.number}, {y.number}) mod {x.prime} and k={k} is the point ({kP.x.number}, {kP.y.number})")
    return

if __name__ == "__main__":
    main()