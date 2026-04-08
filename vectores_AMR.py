"""
Clase Vector con operaciones de multiplicación y ortogonalidad.

Álvaro Marcos Rodríguez

Tests unitarios:
>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2, 4, 6])
>>> v1 * v2
Vector([4, 10, 18])
>>> v1 @ v2
32
>>> v1 = Vector([2, 1, 2])
>>> v2 = Vector([0.5, 1, 0.5])
>>> v1 // v2
Vector([1.0, 2.0, 1.0])
>>> v1 % v2
Vector([1.0, -1.0, 1.0])
"""


class Vector:
    """
    Clase que representa un vector de números reales.
    """

    def __init__(self, iterable):
        """
        Construye un Vector a partir de un iterable de números.
        """
        self.vector = list(iterable)

    def __repr__(self):
        """
        Retorna la representación del vector.
        """
        return f"Vector({self.vector})"

    def __add__(self, other):
        """
        Retorna la suma de dos vectores.
        """
        return Vector(a + b for a, b in zip(self.vector, other.vector))

    def __mul__(self, other):
        """
        Multiplica el vector por un escalar o por otro vector (Hadamard).
        """
        if isinstance(other, Vector):
            return Vector(a * b for a, b in zip(self.vector, other.vector))
        return Vector(a * other for a in self.vector)

    def __rmul__(self, other):
        """
        Multiplica el vector por un escalar.
        """
        return self.__mul__(other)

    def __matmul__(self, other):
        """
        Retorna el producto escalar de dos vectores.
        """
        return sum(a * b for a, b in zip(self.vector, other.vector))

    def __floordiv__(self, other):
        """
        Retorna la componente de self paralela (tangencial) a other.
        """
        escalar = (self @ other) / (other @ other)
        return escalar * other

    def __mod__(self, other):
        """
        Retorna la componente de self perpendicular (normal) a other.
        """
        return self + (-1) * (self // other)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
