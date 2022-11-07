'''You are given an array of integers a.
Your task is to calculate how many numbers in the array are equal to the arithmetic mean of their immediate neighbors.

In other words, count the number of indices i such that a[i] = (a[i - 1] + a[i + 1]) / 2.

Note: If a[i - 1] or a[i + 1] don't exist, they should be considered equal to 0'''
def solution(a):
    l = len(a)
    sum=0
    for i in range(l):
        v=a[i]
        am=0
        if i==0:
            am = a[i+1]//2
            if am == v:
                sum+=1
        elif i==l-1:
            am = a[i-1]//2
            if am == v:
                sum+=1
        else:
            am = (a[i-1] + a[i+1])//2
            if am == v:
                sum += 1
    return sum

array = [2,4,5,6,3,2,4,5,6,3]
print(solution(array))