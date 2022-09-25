import numpy as np
from tabulate import tabulate


class Matrix:

    def __init__(self, arr, verbose=True):
        self.matrix = np.array(arr, dtype=float)
        self.nrow = self.matrix.shape[0]
        self.ncol = self.matrix.shape[1]
        self.v = verbose
        self.print("Initial Matrix")

    def print(self, msg=""):
        print(msg)
        print(tabulate(self.matrix, floatfmt=".1f"))

    def add(self, row1, row2):
        """Add row1 to row2 in matrix m"""
        self.matrix[row2] += self.matrix[row1]
        if self.v:
            self.print(f"Add row {row1} to row {row2}")

    def multiply(self, row, constant):
        """Multiply row by constant"""
        self.matrix[row] *= constant
        if self.v:
            self.print(f"Multiply row {row} by {constant:.2f}")

    def swap(self, row1, row2):
        """Swap row1 and row2"""
        self.matrix[[row1, row2]] = self.matrix[[row2, row1]]
        if self.v:
            self.print(f"Swap {row1} and row {row2}")

    def add_multiply(self, row1, constant, row2):
        """Add constant * row1 to row2"""
        self.matrix[row2] += self.matrix[row1] * constant
        if self.v:
            self.print(f"Add {constant:.2f} * row {row1} to row {row2}")

    def row_echelon(self):
        assert self.nrow == self.ncol - 1
        for i in range(self.nrow):
            if self.matrix[i][i] != 0:
                self.multiply(i, 1.00 / self.matrix[i][i])
            for j in range(i + 1, self.nrow):
                self.add_multiply(i, -self.matrix[j][i], j)
        for i in range(self.nrow - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                self.add_multiply(i, -self.matrix[j][i], j)
        self.print("Reduced row echelon form")


def main():
    # M = Matrix([[-2, 2, 1, 14], [3, -2, 1, -5], [-1, 1, -2, -8]])

    # M = Matrix([[1, 2, -1, 1, 6], [-1, 1, 2, -1, 3], [2, -1, 2, 2, 14], [1, 1, -1, 2, 8]], verbose=False)

    M = Matrix(
        [[1.5, -2, 1, 3, 0.5, 7.5], [3, 1, -1, 4, -3, 16],
         [2, 6, -3, -1, 3, 78], [5, 2, 4, -2, 6, 71], [-3, 3, 2, 5, 4, 54]],
        verbose=False)
    M.row_echelon()


main()
