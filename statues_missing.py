def solution(statues):
    counter = 0
    statues.sort()
    for i in range(len(statues) - 1):
        pf = statues[i + 1] - statues[i]
        if pf != 1:
            counter += pf - 1

statues = list(map(int, input().split(', ')))
print(solution(statues))