'''Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.'''

def solution(st):
    w = list(st)
    i = 0
    ale = len(w)
    if 3 <= ale <= 10:
        while w[:] != w[::-1]:
            w.insert(len(w)-i, w[i])
            i += 1
        return "".join(w)
    else:
        return st

if __name__ == '__main__':
    st = input()
    print(solution(st))