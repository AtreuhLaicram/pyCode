'''Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.'''

def solution(n):
    s = [i for i in str(n)]
    iod = len(s)
    dd = 0
    while iod > 1:
        a = 0
        for x in s:
            a += int(x)
        s = [i for i in str(a)]
        iod = len(s)
        dd += 1
    return dd
    
if __name__ == '__main__':
    
    n = 5
    print(solution(n))