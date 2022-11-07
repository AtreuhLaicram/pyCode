'''You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.'''

def solution(names):
    othernames = []
    for i in range(len(names)):
        elmnti = names[i]
        if elmnti not in othernames:
            othernames.append(elmnti)
        else:
            tlp = names[:i].count(elmnti)
            if tlp == 0:
                tlp = 1
            uvi = elmnti + '(' + str(tlp) + ')'
            while uvi in othernames:
                tlp += 1
                uvi = elmnti + '(' + str(tlp) + ')'
            othernames.append(uvi)
    return othernames

if __name__ == '__main__':

    names = ["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
    print(solution(names))
    names = ["dd", "dd(1)", "dd(2)", "dd", "dd(1)", "dd(1)(2)", "dd(1)(1)", "dd", "dd(1)"]
    print(solution(names))
    names = ["name", "name", "name(1)", "name(3)", "name(2)", "name(2)"]
    print(solution(names))
    names = ["doc", "doc", "image", "doc(1)", "doc"]
    print(solution(names))
    names = []
    print(solution(names))