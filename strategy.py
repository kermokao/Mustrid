import math

class DiscriminantStrategy:
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b**2 - 4*a*c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        d = b**2 - 4*a*c
        if d < 0:
            return float("nan")


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):

       d = self.strategy.calculate_discriminant(a, b, c)
       sqrt_d = math.sqrt (d)


       x1 = (-b - sqrt_d) / (2 * a)
       x2 = (-b + sqrt_d) / (2 * a)
       
       return (x1, x2)

solver = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
print(solver.solve(1, 10, 16))

solver = QuadraticEquationSolver(RealDiscriminantStrategy())
print(solver.solve(1, 4, 5))

       

