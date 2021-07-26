from playLA.Matrix import Matrix
from playLA.Vector import Vector

if __name__ == "__main__":

    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)
    print("matrix.shape = {}".format(matrix.shape()))
    print("matrix.size = {}".format(matrix.size()))
    print("len(matrix) = {}".format(len(matrix)))
    print("matrix[0][0] = {}".format(matrix[0, 0]))
    print(f"matrix[0][0] = {matrix[0, 0]}")

    matrix2 = Matrix([[5, 6], [7, 8]])
    print(f"add: {matrix + matrix2}")
    print(f"subtract: {matrix - matrix2}")
    print(f"scalar-mul: {matrix * 2}")
    print(f"scalar-mul: {2 * matrix}")
    print(f"zero_2_3: {Matrix.zero(2, 3)}")

    T = Matrix([[1.5, 0], [0, 2]])
    p = Vector([5, 3])
    print(f"T.dot(p) = {T.dot(p)}")

    P = Matrix([[0, 4, 5], [0, 0, 3]])
    print(f"T.dot(P) = {T.dot(P)}")

    print(f"A.dot(B) = {matrix.dot(matrix2)}")
    print(f"B.dot(A) = {matrix2.dot(matrix)}")

    print(f"P.T = {P.T()}")

    I = Matrix.identity(2)
    print(I)
    print(f"A.dot(I) = {matrix.dot(I)}")
    print(f"I.dot(A) = {I.dot(matrix)}")