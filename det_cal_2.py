# This algorithm is based on Gaussian elimination and reduces the time complexity (O(n^3))
def init_matrix(order):
    """初始化order×order的零矩阵"""
    return [[0 for _ in range(order)] for _ in range(order)]


def determinant_calculator(matrix, order):
    """
    使用高斯消元法计算行列式值
    原理：将矩阵化为上三角矩阵后，对角线元素乘积即为行列式值（需考虑行交换次数对符号的影响）
    """
    # 深拷贝矩阵避免修改原矩阵
    mat = [row.copy() for row in matrix]
    sign = 1  # 记录行交换次数的符号（偶数次为1，奇数次为-1）

    for col in range(order):  # 遍历每一列（主元列）
        # 步骤1：找到当前列中下方（包括当前行）绝对值最大的行作为主行（减少精度误差）
        pivot_row = col
        for row in range(col, order):
            if abs(mat[row][col]) > abs(mat[pivot_row][col]):
                pivot_row = row

        # 步骤2：若主元为0，行列式值为0（矩阵不可逆）
        if mat[pivot_row][col] == 0:
            return 0

        # 步骤3：交换当前行与主行（若需要），并更新符号
        if pivot_row != col:
            mat[col], mat[pivot_row] = mat[pivot_row], mat[col]
            sign *= -1  # 每交换一次行，符号反转

        # 步骤4：消去当前列下方所有元素（化为上三角矩阵）
        for row in range(col + 1, order):
            factor = mat[row][col] / mat[col][col]  # 计算消元因子
            for c in range(col, order):
                mat[row][c] -= factor * mat[col][c]  # 行变换：row = row - factor*col

    # 步骤5：计算上三角矩阵对角线元素的乘积，乘以符号得到行列式值
    result = sign
    for i in range(order):
        result *= mat[i][i]

    return round(result)  # 四舍五入处理浮点数精度误差


# 主程序：获取输入并计算行列式
if __name__ == "__main__":
    # 输入行列式阶数
    order = int(input("请输入行列式的阶数："))
    
    # 初始化并输入行列式元素
    det = init_matrix(order)
    for i in range(order):
        for j in range(order):
            det[i][j] = int(input(f"请输入行列式元素 det[{i+1}][{j+1}] = "))
    
    # 计算并输出结果
    determinant_value = determinant_calculator(det, order)
    print(f"该行列式的值为：{determinant_value}")
