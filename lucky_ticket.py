'''Ticket numbers usually consist of an even number of digits.
A ticket number is considered lucky if the sum of the first half of the digits
is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not.'''
def solution(n):
    lis = str(n)
    half_lenght1 = len(lis)//2
    firsth_half = list(map(int, lis[:half_lenght1]))
    second_half = list(map(int, lis[half_lenght1:]))
    if sum(firsth_half) == sum(second_half):
        return True
    return False


n = 239017
print(solution(n))