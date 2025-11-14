# This algorithm can achieve dynamic input of determinant data, that is, there is no need to input the order of the determinant in advance.
def parse_input():
    """
    动态接收用户输入，构建行列式矩阵
    输入规则：每行元素用空格分隔（如"1 2 3"），输入空行或"end"结束输入
    返回：有效的行列式矩阵（方阵），若输入无效则返回None
    """
    matrix = []
    print("请逐行输入行列式元素（每行元素用空格分隔，输入空行或'end'结束）：")
    
    while True:
        # 接收一行输入并去除首尾空白
        line = input().strip()
        
        # 结束输入条件
        if line.lower() == "end" or line == "":
            break
        
        # 分割元素并转换为数值（支持整数和浮点数）
        try:
            # 按空格分割，过滤空字符串（处理连续空格的情况）
            elements = list(map(float, filter(None, line.split())))
            matrix.append(elements)
        except ValueError:
            print("输入错误！请确保每行元素都是数字（用空格分隔），重新输入该行：")
            continue
    
    # 校验是否为方阵（行数=列数，且每行元素数量相同）
    if not matrix:  # 空矩阵
        print("未输入任何元素，无法计算行列式！")
        return None
    
    order = len(matrix)  # 行列式阶数=行数
    for i, row in enumerate(matrix):
        if len(row) != order:
            print(f"输入错误！第{i+1}行有{len(row)}个元素，与行数{order}不匹配（必须为方阵）！")
            return None
    
    return matrix


def determinant_calculator(matrix):
    """使用高斯消元法计算行列式值（输入为方阵）"""
    order = len(matrix)
    if order == 0:
        return 0
    
    # 深拷贝矩阵避免修改原矩阵
    mat = [row.copy() for row in matrix]
    sign = 1  # 行交换符号（偶数次为1，奇数次为-1）
    
    for col in range(order):
        # 选主元：找到当前列下方（含当前行）绝对值最大的行
        pivot_row = col
        for row in range(col, order):
            if abs(mat[row][col]) > abs(mat[pivot_row][col]):
                pivot_row = row
        
        # 主元为0则行列式值为0
        if mat[pivot_row][col] == 0:
            return 0
        
        # 交换行并更新符号
        if pivot_row != col:
            mat[col], mat[pivot_row] = mat[pivot_row], mat[col]
            sign *= -1
        
        # 消去当前列下方元素
        for row in range(col + 1, order):
            factor = mat[row][col] / mat[col][col]
            for c in range(col, order):
                mat[row][c] -= factor * mat[col][c]
    
    # 计算对角线乘积×符号
    result = sign
    for i in range(order):
        result *= mat[i][i]
    
    return round(result, 6)  # 保留6位小数处理精度问题


# 主程序
if __name__ == "__main__":
    # 动态获取行列式矩阵
    det_matrix = parse_input()
    
    # 计算并输出结果（仅当矩阵有效时）
    if det_matrix:
        order = len(det_matrix)
        value = determinant_calculator(det_matrix)
        print(f"\n{order}阶行列式的值为：{value}")
