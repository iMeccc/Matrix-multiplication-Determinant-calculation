# This algorithm is based on the recursive determinant calculation derived from mathematical induction.
# get the input
order = int(input("the order of the determinant is:"))

def det_init(order):
    det = [[0 for _ in range(order)]for _ in range(order)]
    return det

# do the calculation

def two_order_cal(det):
    result = det[0][0]*det[1][1]-det[0][1]*det[1][0]
    return result

def det_cal(det,order):
    final_result = 0
    if order > 2:    
        new_order = order-1
        result = [0 for _ in range(order)]
        for i in range(order):
            new_det = det_init(new_order)
            for p in range(new_order):
                for q in range(new_order):
                    if q < i:
                        new_det[p][q] = det[p+1][q]
                    elif q >= i:
                        new_det[p][q] = det[p+1][q+1]

        # code above has realised the input of the new determinant
        # code below will do the calculation
            result[i] = det[0][i]*det_cal(new_det,new_order)
            if i%2 == 0:
                result[i] = -result[i]
            final_result += result[i]

    elif order == 2:
        final_result = two_order_cal(det)

    return final_result

determinant = det_init(order)
for i in range(order):
        for j in range(order):
            determinant[i][j] = int(input(f"det[{i+1}][{j+1}]="))
result = det_cal(determinant,order)
print(f"The determinant equals to {result}")

