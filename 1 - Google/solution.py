def main():
    k = 17
    X = [10, 15, 3, 7]

    print("First Solution: ", isSummable(k,X,0))
    print("Second Solution: ", isSummableBis(k,X))
#O(N^2) time
#O(1) space
def isSummable(k, X, p):
    for v_f in X:
        for v_s in range(p, len(X)):
            if v_f + v_s == k: return True
        p =  X.index(v_f)

    return False

#O(N Log N) time
#O(1) space
def isSummableBis(k, X):
    l_seen = set()
    for v in X:
        if k - v in l_seen:
            return True
        l_seen.add(v)
    return False
main()
