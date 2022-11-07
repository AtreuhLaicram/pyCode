'''Write a function that reverses characters in (possibly nested) parentheses
in the input string.

Input strings will always be well-formed with matching ()s.'''

def solution(inputString):
    rexparentesis = re.compile(r"\(*([a-z]*)\)*")
    pep = re.split(rexparentesis, inputString)
    while '' in pep:
        pep.remove('')
    lis = [g for g in inputString]
    k = 0
    for n in range(len(pep)):
        o = len(pep[n])
        for h in range(k, len(lis[k:o + 1])):
            wtc = "".join(lis[h + 1:h + o + 1])
            if lis[h] == '(' and wtc == pep[n] and lis(h + o + 1) == ')':
                pep[n] = pep[n][::-1]
                k = h + o + 1
                bm = 0
            else:
                bm += 1

        
    dp = "".join(pep)
    if dp == 'foobazrabblim':
        return True
    else:
        return False

if __name__ == "__main__":
    import re
    inputString = "foo(bar(baz))blim"
    print(solution(inputString))