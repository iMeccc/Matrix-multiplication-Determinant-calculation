import sys
# 导入矩阵乘法相关函数
from matrix_mul import input_matrix, matrix_multiply, print_matrix
# 导入行列式计算相关函数
from det_cal_2 import init_matrix, determinant_calculator

def main():
    print("矩阵运算工具")
    print("1. 矩阵乘法")
    print("2. 行列式计算")
    
    while True:
        try:
            choice = int(input("请选择操作 (1/2): "))
            if choice in [1, 2]:
                break
            else:
                print("请输入1或2选择操作")
        except ValueError:
            print("请输入有效的数字")
    
    if choice == 1:
        # 矩阵乘法操作
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
    
    else:
        # 行列式计算操作
        try:
            order = int(input("请输入行列式的阶数："))
            if order <= 0:
                print("阶数必须是正整数")
                sys.exit(1)
        except ValueError:
            print("阶数必须是整数！")
            sys.exit(1)
        
        # 初始化并输入行列式元素
        det = init_matrix(order)
        for i in range(order):
            for j in range(order):
                while True:
                    try:
                        det[i][j] = int(input(f"请输入行列式元素 det[{i+1}][{j+1}] = "))
                        break
                    except ValueError:
                        print("请输入整数！", end=" ")
        
        # 计算并输出结果
        determinant_value = determinant_calculator(det, order)
        print(f"该行列式的值为：{determinant_value}")

if __name__ == "__main__":
    main()