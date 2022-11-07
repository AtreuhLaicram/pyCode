'''Given two strings, find the number of common characters between them.'''
from unittest import result


def solution(s1, s2):
    knv1 = {}
    knv2 = {}
    for c in s1:
        if c not in knv1.keys():
            knv1[c] = 0
        knv1[c] += 1
    for b in s2:
        if b not in knv2.keys():
            knv2[b] = 0
        knv2[b] += 1
    rslt = 0
    for s in knv1.keys():
        if s in knv2.keys() and knv1[s] < knv2[s]:
            rslt += knv1[s]
    for t in knv2.keys():
        if t in knv1.keys() and knv2[t] <= knv1[t]:
            rslt += knv2[t]
    return rslt
s1 = "zzzz"
s2 = "zzzzzzz"
print(solution(s1, s2))