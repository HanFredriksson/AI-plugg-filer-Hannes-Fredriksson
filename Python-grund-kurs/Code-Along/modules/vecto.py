import matplotlib.pyplot as plt

class Vector:
    """A class to represent Uclidean vectors"""

    def __init__(self, *numbers):
        #Error checking
        for number in numbers:
            if not isinstance(number,(float, int)):
                raise TypeError(f"{number} is not a valid number.")
        
        if len(numbers)<= 0:
            raise ValueError("Vector can't be empty.")
        
        self._numbers = tuple(float(number) for number in numbers)

    @property
    def numbers(self):
        return self._numbers
    
    @staticmethod
    def validate2d(isinstance):
        return len(isinstance) == 2

    def __add__(self, other):
        if self.validate_vector(other):
            numbers = (a + b for a, b in zip(self._numbers, other.numbers))
            return Vector(*numbers)
    
    def __sub__(self, other):
        if self.validate_vector(other):
            numbers = (a - b for a, b in zip(self._numbers, other.numbers))
            return Vector(*numbers)
        
    def __mul__(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Value must be a scaler(int or a flost).")
        numbers = (value*a for a in self.numbers)
        return Vector(*numbers)
    
    def __rmul__(self, value):
        return self*value

    def __len__ (self):
        return len(self._numbers)

    def validate_vector(self, other):
        if not isinstance(other, Vector):
            raise ValueError(f"{other} is not valid")
        
        if len(self) != len(other):
            raise TypeError(f"{len(other)} != {len(self)}")
        return True

    def __abs__(self):
        """Return the Euclidian norm of a Vector, aka the L2-norm"""

        return sum(a**2 for a in self.numbers) ** .5

    def __repr__(self):
        return f"Vector {self._numbers}"
    
    def __getitem__(self, index):
        return self.numbers[index]

    def __eg__(self, other):
        if not self.validate_vector(other):
            return False
        
        for v1, v2 in zip(self.numbers, other.numbers):
            if v1 != v2:
                return False
        return True

    def plot(self, *others):
        x, y = [], []
        if not Vector.validate2d(self):
            raise TypeError("Only 2d vectors can be plotted")

        for v in tuple(others):
            if Vector.validate2d(v):
                x.append(v[0])
                y.append(v[1])

        x.append(self[0])
        y.append(self[1])

        originx = originy = tuple(0 for _ in range(len(x)))
        plt.quiver([originx, originy], x ,y, angles='xy', scale_units='xy', scale=1)
        plt.xlim(-2, 10)
        plt.ylim(-2, 10)
        plt.grid()
        plt.show()



# Här kan vi köa den som ett skript. Detta importeras inte till annan kod som skriv under if __name___.
if __name__ == '__main__': #Detta är på global nivå
    VARIABEL = 0 # Variabler skrivs alltid med stora bokstäver
    print("Nu är vi vector modulen")

#else: # Gör inte så här!!! Bygg ine in funktinalitet
    #print(f"Hej, från vector modulen"{globals()['Vector']})