class FiniteFieldElement:
    def __init__(self, number, prime):
        if number >= prime or number < 0:
            raise ValueError(f"Number has to be between 0 and {prime}")
        self.number = number
        self.prime = prime

    def __add__(self, other):
        if self.prime != other.prime: 
            raise TypeError('Cannot add two numbers in different Fields')
        new_number = (self.number + other.number) % self.prime 
        return self.__class__(new_number, self.prime)

    def __sub__(self, other):

        return

    def __mul__(self, other):

        return
    
    def __truediv__(self, other):

        return

def main():
    number_1 = FiniteFieldElement(4,7)
    number_2 = FiniteFieldElement(5,7)
    print((number_1 + number_2).number)

main()