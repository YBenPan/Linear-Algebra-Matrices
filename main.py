import numpy as np
from tabulate import tabulate


class Matrix:

    def __init__(self, arr):
        self.matrix = np.array(arr)
        self.row = self.matrix.shape[0]
        self.col = self.matrix.shape[1]
        self.print("Matrix at the beginning")

    def print(self, msg):
        print(msg, tabulate(self.matrix))

    def add(self, row1, row2):
        """Add row1 to row2 in matrix m"""
        self.matrix[row2] += self.matrix[row1]
        self.print(f"Matrix afer adding row {row1} to row {row2}")

    def multiply(self, row, constant):
        """Multiply row by constant"""
        self.matrix[row] *= constant
        self.print(f"Matrix afer multiplying row {row} by {constant}")

    def swap(self, row1, row2):
        self.matrix[[row1, row2]] = self.matrix[[row2, row1]]
        self.print(f"Matrix after swapping row {row1} and row {row2}")


def main():
    M = Matrix([[1, 0, 1], [0, 2, 3], [0, 3, 3]])
    M.add(0, 1)
    M.multiply(0, 2)
    M.swap(0, 1)


main()
