def solution(inputString):
    new_string = ""
    reverse_string = ""
    y = 1
    for x in inputString:
        if x != " " or y != 0:
            new_string += x.lower()
            reverse_string += inputString[-y].lower()
            y += 1
        else:
            y += 1
    if new_string == reverse_string:
        return True
    else:
        return False

if __name__ == '__main__':
    
    inputString = 'abcdc'
    print(solution(inputString))        