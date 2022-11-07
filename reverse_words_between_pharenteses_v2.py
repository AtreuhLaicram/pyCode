'''Write a function that reverses characters in (possibly nested) parentheses
in the input string.

Input strings will always be well-formed with matching ()s.'''
def solution(inputString):
    w = inputString.split('(')
    x = inputString.split(')')
    for i in range(len(w)):
        if ')' in w[i]:
            k = w[i].split(')')
            xn = k[0][::-1]
            w[i] = xn + k[1]
    for j in range(len(x)-1, 0, -1):
        if '(' in x[j]:
            m = x[j].split('(')
            yn = m[1][::-1]
            x[j] = m[0] + yn
    finalw = []
    for f in range(len(x)):
        if x[f] not in w:
            finalw.insert(f, x[f])
    for g in range(len(w)):
        if w[g] not in x:
            finalw.insert(g, w[g])
    return finalw


if __name__ == "__main__":
    import re
    inputString = input()
    print(solution(inputString))