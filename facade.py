import random
class Generator:

    def generate(self, number):
        return random.sample(range(1, 10), number)

class Splitter:
    def split(self, matrix):
        result = []
        number = len(matrix)

        for row in matrix:
            result.append(row)

        for i in range(number):
            column = []
            for j in range(number):
                column.append(matrix[i][j])
            result.append(column)

        diagonal = []
        for i in range(number):
            diagonal.append(matrix[i][i])
        result.append(diagonal)

        second_diagonal = []
        for i in range(number):
            second_diagonal.append(matrix[i][number - 1 - i])
        result.append(second_diagonal)

        return result

class Verifier:
    def verify(self, parts):
        if not parts:
            return True

        target_sum = sum(parts[0])

        for rida in parts:
            if sum(rida) != target_sum:
                return False
        return True

class MagicSquareGenerator:
    def generate(self, size):
        splitter = Splitter()
        verifier = Verifier()

        while True:
            numbers = list(range(1, size * size + 1))
            random.shuffle(numbers)
            matrix = [numbers[i * size:(i + 1) * size] for i in range(size)]

            parts = splitter.split(matrix)

            if verifier.verify(parts):
                return matrix

g = Generator()
print(g.generate(9))

matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

s = Splitter()
for rida in s.split(matrix):
    print(rida)

v = Verifier()
print(v.verify([
[2, 7, 6],
[9, 5, 1],
[4, 3, 8],
[2, 9, 4],
[7, 5, 3],
[6, 1, 8],
[2, 5, 8],
[6, 5, 4]
]))

gen = MagicSquareGenerator()
square = gen.generate(3)

for row in square:
    print(row)
