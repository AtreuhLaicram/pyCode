'''Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters'''

def solution(s):
    setos = list(s)
    h = []
    
    for ss in setos:
        cc = 1
        ni = 0
        while ni < len(s)-1 and s[ni] == ss:
            cc += 1
            ni += 1
        if cc != 1:
            h.append(str(cc) + ss)
        else:
            h.append(ss)
        
    return "".join(h)

if __name__ == '__main__':
    s = "aabbbccccabc"
    print(solution(s))