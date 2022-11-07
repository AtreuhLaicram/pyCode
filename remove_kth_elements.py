'''Removes the k'th digits of a given array'''

def solution(inputArray, k):
    inputArray.insert(0, 0)
    del inputArray[::k]
    return inputArray
if __name__ == '__main__':
    inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3
    print(solution(inputArray, k))