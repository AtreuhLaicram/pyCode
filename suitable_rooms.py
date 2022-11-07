def solution(matrix):
    sumofsr = 0
    hounted_rooms = list(map(list, zip(*matrix)))
    for hounted_floor in hounted_rooms:
        for is_suitable in hounted_floor:
            if is_suitable != 0:
                sumofsr += is_suitable
            else:
                break
    return sumofsr


matrix = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]
print(solution(matrix))