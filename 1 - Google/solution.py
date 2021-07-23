def main():
    k = 18
    X = [10, 15, 3, 7]

    print(isSummable(k,X,0))

def isSummable(k, X, p):
    for v_f in X:
        for v_s in range(p, len(X)):
            if v_f + v_s == k: return True
        p =  X.index(v_f)

    return False
main()