'''You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.'''

import re
def solution(names):
    pattern = r'\((\d+)\)'
    othernames = []
    if len(names) == 0:
        return othernames
    for i in range(len(names)):
        elmnti = names[i]
        if elmnti not in othernames:
            othernames.append(elmnti)
        else:
            k = names[:i].count(elmnti)
            uvi = elmnti + '(' + str(k + 1) + ')'
            if uvi in othernames:
                mk = re.findall(pattern, uvi)
                othernames.append(elmnti + '(' + str(int(mk[0]) + 1) + ')')
            else:
                othernames.append(uvi)
    return othernames

if __name__ == '__main__':

    names = ["dd", "dd(1)", "dd(2)", "dd", "dd(1)", "dd(1)(2)", "dd(1)(1)", "dd", "dd(1)"]
    print(solution(names))
""" names = ["name", "name", "name(1)", "name(3)", "name(2)", "name(2)"]
    print(solution(names))
    names = ["doc", "doc", "image", "doc(1)", "doc"]
    print(solution(names))
    names = ["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
    print(solution(names))"""