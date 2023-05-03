class FiniteFieldElement:
    def __init__(self, number, prime):
        if number >= prime or number < 0:
            raise ValueError(f"Number has to be between 0 and {prime}")
        self.number = number
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
    
    def __truediv__(self, other):
        if self.prime != other.prime: 
            raise TypeError('Cannot divide two numbers in different Fields')
        new_number = (self.number * pow(other.number, self.prime - 2, self.prime)) % self.prime #Pequeño teorema de fermat optimizado por la funcion pow()
        return self.__class__(new_number, self.prime)

def main():
    number_1 = FiniteFieldElement(7,1000)
    number_2 = FiniteFieldElement(5,1000)
    number_3 = FiniteFieldElement(10,19)
    print((number_1 - number_2).number)
    print((number_1 * number_2).number)
    print((number_1 / number_2).number)

main()