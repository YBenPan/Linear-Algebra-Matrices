import numpy as np
from tabulate import tabulate


class Matrix:

    def __init__(self):
        self.matrix = np.array([[1, 0, 1], [0, 2, 3], [0, 3, 3]])
        self.print("Matrix at the beginning")

    def print(self, msg):
        print(msg, tabulate(self.matrix))

    def add(self, row1, row2):
        """Add row1 to row2 in matrix m"""
        row1 -= 1
        row2 -= 1
        self.matrix[row2] += self.matrix[row1]
        self.print(f"Matrix afer adding row {row1} to row {row2}")

    def multiply(self, row, constant):
        """Multiply row by constant"""
        row -= 1
        self.matrix[row] *= constant
        self.print(f"Matrix afer multiplying row {row} by {constant}")

    def swap(self, row1, row2):
        row1 -= 1
        row2 -= 1
        # TODO: Implement swap using numpy indexing
        self.print(f"Matrix after swapping row {row1} and row {row2}")


def main():
    M = Matrix()
    M.add(1, 2)
    M.multiply(1, 3)
    M.swap(1, 2)


main()
