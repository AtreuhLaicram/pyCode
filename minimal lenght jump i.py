'''You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.'''
def solution(inputArray):
    inputArray.sort()
    s = 0
    hii = {}
    pjl = []
    for i in range(inputArray[-1]+2):
        if i not in inputArray:
            hii[i]=0
        else:
            hii[i]=1
    for a in hii.keys():
        if hii[a] == 0:
            pjl.append(a)
    for g in pjl:
        gg = g*2
        if gg not in inputArray:
            return g
        else:
            gg = 0
    

if __name__ == '__main__':
    inputArray = [19, 32, 11, 23]
    print(solution(inputArray))