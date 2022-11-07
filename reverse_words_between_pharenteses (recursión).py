'''Write a function that reverses characters in (possibly nested) parentheses
in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
'''

def solution(inputString):
    rexparentesis = re.compile(r"\(*([a-z]*)\)*")
    pep = re.split(rexparentesis, inputString)
    while '' in pep:
        pep.remove('')
    if len(pep) == 0:
        return ''
    lis = [g for g in inputString]
    k = 0
    f = lis.count(')')
    if f < 1 and len(pep) > 0:
        return inputString
    for n in range(len(pep)):
        o = len(pep[n])
        for h in range(k, k + o + 1):
            if lis[h] == '(':
                wtc = "".join(lis[h + 1:h + o + 1])
                pp = lis[h]
                up = lis[h + o + 1]
                if pp == '(' and wtc == pep[n] and up == ')':
                    pep[n] = pep[n][::-1]
                    lis = lis[:h] + list(pep[n]) + lis[h+o+2:]
                    return solution("".join(lis))
                else:
                    k = h + o + 1
                    break
            else:
                k = h + o
                break
            
if __name__ == "__main__":
    import re
    inputString = "(abc)d(efg)"
    print(solution(inputString))