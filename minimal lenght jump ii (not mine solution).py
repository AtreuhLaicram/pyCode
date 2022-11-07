'''You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.'''
def solution(inputArray):
    i=2
    while True:
        if all(j % i != 0 for j in inputArray):
            return i
        i += 1
    

if __name__ == '__main__':
    inputArray = [19, 32, 11, 23]
    print(solution(inputArray))