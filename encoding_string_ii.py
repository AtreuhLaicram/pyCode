'''Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters'''


def solution(s):
    lttr = []
    ll = len(s)
    i = 1
    
    while ll > 1:
        c = 1
        while i < len(s)-1 and s[i] == s[i + 1]:
            c += 1
            i += 1
        if c == 1:
            lttr.append(s[i])
            ll -= c
        else:
            lttr.append(str(c) + s[i])
            ll -= c
        i += 1
        
    i -= 1
    if s[i] != s[i - 1]:
        lttr.append(s[i])

    return "".join(lttr)

if __name__ == '__main__':
    s = "aaaa"
    print(solution(s))