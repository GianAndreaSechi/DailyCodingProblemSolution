def main():
    A = [1, 2, 3, 4, 5]

    print("Solution: ", productArray(A))

def productArray(A):
    tot_prod = 1
    product_A = []
    for v in A: tot_prod*=v
    for v in A: 
        new_val = tot_prod / v
        product_A.append(new_val)
    return product_A
main()