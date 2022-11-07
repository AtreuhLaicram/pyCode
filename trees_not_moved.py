'''Some people are standing in a row in a park.
There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in a non-descending order
without moving the trees. People can be very tall!'''
def solution(a):
    b=[]
    for i in range(len(a)):
        if a[i] == -1:
            b.append(i)
    a.sort()
    
    for k in range(len(a)): 
        if a[0] == -1:
            try:
                a.remove(-1)
            except:
                pass
    for i in b:
        a.insert(i, -1)
    return a

a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(solution(a))