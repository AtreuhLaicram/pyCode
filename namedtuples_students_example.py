'''The average of a list of grades with namedtuple()
Example:
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
5          80         Peter      6
4          72         Stewart    5
3          91         Adrian     9
2          50         Steven     4
The average must be 78.00'''

from collections import namedtuple
n = int(input())
zum = 0
Student = namedtuple('Student', input().split()) # The subclass Student field names definition
a = [Student(*input().split()) for i in range(n)] # The list of grades (Research the use of * before the input)
for b in a:
    zum = sum(b.MARKS) # Accessing the value by its name
averages = zum/n
print(averages)