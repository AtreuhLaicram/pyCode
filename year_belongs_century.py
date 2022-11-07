def solution(year):
    k = year//100
    if year % 100 != 0:
        century = k+1
    else:
        century = k
    return century

year = int(input())
print(solution(year))