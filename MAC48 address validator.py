'''MAC address validator'''

import re
def solution(inputString):
    pattern = r"[A-F0-9]{2}"
    mal = inputString.split("-")
    fl = True
    for x in range(len(mal)):
        if len(mal) != 6 or len(mal[x]) != 2 or mal[x].count(' ') !=0 or not re.search(pattern, mal[x]):
            fl = False
    return fl
if __name__ == '__main__':
    inputString = "02-03-04-05-06-07-"
    print(solution(inputString))