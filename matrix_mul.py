import sys

def input_matrix(rows, cols, name):
    """输入矩阵数据（带整数校验）"""
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            while True:
                try:
                    val = int(input(f"{name}[{i+1}][{j+1}]="))
                    matrix[i][j] = val
                    break
                except ValueError:
                    print("请输入整数！", end=" ")
    return matrix

def matrix_multiply(A, B):
    """矩阵乘法：A×B，返回结果矩阵"""
    row_A, col_A = len(A), len(A[0]) if A else 0
    row_B, col_B = len(B), len(B[0]) if B else 0

    # 初始化结果矩阵并计算每个元素
    result = []
    for i in range(row_A):
        current_row = []  # 存储结果矩阵的第i行
        for j in range(col_B):
            # 提取B的第j列：[B[0][j], B[1][j], ..., B[row_B-1][j]]
            col_B_j = [B[k][j] for k in range(row_B)]
            # 计算A的第i行与B的第j列的点积（核心步骤）
            dot_product = 0
            for a, b in zip(A[i], col_B_j):
                dot_product += a * b
            current_row.append(dot_product)
        result.append(current_row)
    return result

def print_matrix(matrix, name="结果矩阵"):
    """格式化打印矩阵，确保对齐"""
    print(f"\n{name} =")
    for row in matrix:
        print(" ".join(f"{num:4}" for num in row))  # 每个元素占6位宽度

if __name__ == "__main__":
    # 输入矩阵维度（带校验）
    try:
        row_A = int(input("矩阵A行数："))
        col_A = int(input("矩阵A列数："))
        row_B = int(input("矩阵B行数："))
        col_B = int(input("矩阵B列数："))
    except ValueError:
        print("维度必须是整数！")
        sys.exit(1)

    # 检查乘法可行性
    if col_A != row_B:
        print(f"无法相乘：A列数({col_A})≠B行数({row_B})")
        sys.exit(1)

    # 输入矩阵数据
    matrix_A = input_matrix(row_A, col_A, "A")
    matrix_B = input_matrix(row_B, col_B, "B")

    # 计算并打印结果
    result = matrix_multiply(matrix_A, matrix_B)
    print_matrix(result, "A × B")
    