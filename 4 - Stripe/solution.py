
def lowestPositive(array):
    for index, val in enumerate(array, start=0):
        if val < 0:
            return index
            
    return len(array)

#O(N) Time
#O(N) space
def main():
    #array = [3,4,-1,1] 
    array = [1,3,0]

    print(lowestPositive(array))


main()