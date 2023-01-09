
def vecToMatrix(v):
    m = [[0] * 1 for i in range(3)]
    m[0][0] = v.x
    m[1][0] = v.y
    m[2][0] = v.z
    return m

def matrixToVec(m):
    v = PVector()
    v.x = m[0][0]
    v.y = m[1][0]
    if len(m) > 2:
        v.z = m[2][0]
    return v

def logMatrix(m):
    cols = len(m[0])
    rows = len(m)
    print(f"{rows}x{cols}")
    print("----------------")
    for i in range(rows):
        for j in range(cols):
            print(f"{m[i][j]} ", end="")
        print()
    print()

def matmul(a, b):
    if isinstance(b, PVector):
        m = vecToMatrix(b)
        return matrixToVec(matmul(a,m))
    else:
        colsA = len(a[0])
        rowsA = len(a)
        colsB = len(b[0])
        rowsB = len(b)

        if colsA != rowsB:
            print("Columns of A must match rows of B")
            return None

        result = [[0] * colsB for i in range(rowsA)]

        for i in range(rowsA):
            for j in range(colsB):
                sum = 0
                for k in range(colsA):
                    sum += a[i][k] * b[k][j]
                result[i][j] = sum
        return result