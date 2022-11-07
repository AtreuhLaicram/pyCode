def solution(sequence):
    l2 = 0
    i = 1
    if len(sequence) == 1:
        return True
    while i < len(sequence):
        if sequence[i] > sequence[i - 1]:
            i += 1
        elif i == 1 or sequence[i] > sequence[i - 2]:
            sequence.pop(i - 1)
            l2 += 1
            i = 1            
        else:
            sequence.pop(i)
            l2 += 1
            i = 1
        if l2 > 1:
            return False
    return True


sequence = [1, 2, 5, 3, 5]
print(solution(sequence))