'''Write a function that reverses characters in (possibly nested) parentheses
in the input string.

Input strings will always be well-formed with matching ()s.'''
def solution(inputString):
    oppar = {}
    
    revw = ''
    for i in range(len(inputString)):
        if inputString[i] == '(' or inputString[i] == ')':
            oppar[i] = inputString[i]



 
if __name__ == "__main__":
    import re
    inputString = "foo(bar(baz))blim"
    print(solution(inputString))