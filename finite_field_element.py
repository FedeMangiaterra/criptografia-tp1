'''Implementar un tipo de dato para un elemento de cuerpo finito, junto con sus operaciones aritméticas
fundamentales (adición, sustracción, multiplicación y división).'''

class FiniteFieldElement:
    def __init__(self, number, prime):
        self.number = number % prime
        self.prime = prime

    def __eq__(self, other):
        if other is None:
            return False
        return self.number == other.number and self.prime == other.prime

    def __add__(self, other):
        if self.prime != other.prime: 
            raise TypeError('Cannot add two numbers in different Fields')
        new_number = (self.number + other.number) % self.prime 
        return self.__class__(new_number, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime: 
            raise TypeError('Cannot substract two numbers in different Fields')
        new_number = (self.prime + (self.number - other.number)) % self.prime 
        return self.__class__(new_number, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime: 
            raise TypeError('Cannot multiply two numbers in different Fields')
        new_number = (self.number * other.number) % self.prime
        return self.__class__(new_number, self.prime)
    
    def __rmul__(self, coefficient):
        new_number = (self.number * coefficient) % self.prime
        return self.__class__(new_number, self.prime)
    
    def __pow__(self, exponent):
        n = exponent % (self.prime - 1) 
        num = pow(self.number, n, self.prime)
        return self.__class__(num, self.prime)
    
    def __truediv__(self, other):
        if self.prime != other.prime: 
            raise TypeError('Cannot divide two numbers in different Fields')
        new_number = (self.number * pow(other.number, self.prime - 2, self.prime)) % self.prime #Pequeño teorema de fermat optimizado por la funcion pow()
        return self.__class__(new_number, self.prime)
    
    def print_info(self):
        print(f"{self.number} mod {self.prime}")

def main():
    number_1 = FiniteFieldElement(7,1000)
    number_2 = FiniteFieldElement(5,1000)
    number_3 = FiniteFieldElement(-3,1021)
    print((number_1 - number_2).number)
    print((number_1 * number_2).number)
    print((number_1 / number_2).number)
    print((201 * number_2).number)

if __name__ == "__main__":
    main()