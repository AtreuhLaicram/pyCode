'''A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.

Given a string, check whether it is beautiful.'''

def solution(inputString):
    w = {}
    abcd = [chr(letter) for letter in range(97, 123)]
    res = True
    for mi in abcd:
        if mi not in w:
            w[mi] = 0
    letlis = [l for l in inputString]
    for d in letlis:
        w[d] += 1
    g = sorted(w.keys())
    for r in range(len(g)):
        if g[r] == 'a':
            pass
        elif w[g[r]] > w[g[r-1]]:
            res = False
            break
    return res

if __name__ == '__main__':
    
    inputString = 'bbbaacdafe'
    print(solution(inputString))