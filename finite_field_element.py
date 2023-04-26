class FiniteFieldElement:
    def __init__(self, number, prime):
        if number >= prime or number < 0:
            raise ValueError(f"Number has to be between 0 and {prime}")
        self.number = number
        self.prime = prime

    def _add_(self, other):
        if self.prime != other.prime: 
            raise TypeError('Cannot add two numbers in different Fields')
        new_number = (self.number + other.number) % self.prime 
        return self.__class__(new_number, self.prime)

    def _sub_(self, other):

        return

    def _mul_(self, other):

        return
    
    def _truediv_(self, other):

        return