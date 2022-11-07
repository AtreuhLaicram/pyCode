'''Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.'''


def solution(n):
    b = list(map(int, str(n)))
    e = ["".join(map(str, y)) for y in [b[:x]+b[x+1:] for x in range(len(b))]]
    return max(map(int, e))
        

if __name__ == '__main__':
    n = 1001
    print(solution(n))