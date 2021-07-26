import numpy as np

if __name__ == "__main__":

    # 矩阵的创建
    A = np.array([[1, 2], [3, 4]])
    print(A)

    # 矩阵的属性
    print(A.shape)
    print(A.T)

    # 获取矩阵的元素
    print(A[1, 1])
    # 第一行
    print(A[0])
    # 第一列
    print(A[:, 0])
    # 第二行 等价于 A[1]
    print(A[1, :])

    # 矩阵的基本运算
    B = np.array([[5, 6], [7, 8]])
    print(A + B)
    print(A - B)
    print(10 * A)
    print(A * 10)
    # 对应位置的数相乘，无意义
    print(A * B)
    print(A.dot(B))

    p = np.array([10, 100])
    # 高维和低维运算，叫广播
    print(A + p)
    print(A + 1)

    print(A.dot(p))

    # 单位矩阵
    I = np.identity(2)
    print(I)
    print(A.dot(I))
    print(I.dot(A))

    # 逆矩阵
    invA = np.linalg.inv(A)
    print(invA)
    print(invA.dot(A))
    print(A.dot(invA))