'''Define a word as a sequence of consecutive English letters. Find the longest word from the given string.'''

import re
def solution(text):
    pattern = r'[a-zA-Z][a-zA-Z]*'
    wot = re.findall(pattern, text)
    c = {}
    for wt in wot:
        if wt not in c.keys():
            c[wt] = 0
        c[wt] = len(wt)
    s = max(c.values())
    dr = []
    for xm in c.keys():
        if c[xm] == s:
            dr.append(xm)
    return ', '.join(dr)

if __name__ == '__main__':
    text = 'Mexico is the beautiest country in the world'
    print(solution(text))