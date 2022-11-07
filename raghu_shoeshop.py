''' Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
INPUT
The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
spl = []
total = 0
# first line contains X, the number of shoes.
x = int(input())
if 0 < x < 10**3:
    # second line contains the space separated list of all the shoe sizes in the shop.
    sz = input().split()
    sz.sort()
    sizes = Counter(sz)
    # third line contains N, the number of customers.
    n = int(input())
    if 0 < n <= 10**3:
        # next n lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.
        for pl in range(n):
            spl.append(input().split())
        # Creates a list for prices and a dict of sizes and prices asked by customers
        for size, price in spl:
            if sizes[size] > 0:
                sizes[size] -= 1 #Substracts a unit from size inventory
                total += int(price) # Sums the price of the desired shoe
        print(total)