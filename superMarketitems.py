'''You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.'''
from collections import OrderedDict
items = int(input())
superMarketitems = OrderedDict()
for it in range(items):
    itstring = input().split()
    if len(itstring) > 2:
        itname = itstring[0] + ' ' + itstring[1]
        itprice = int(itstring[2])
    else:
        itname = itstring[0]
        itprice = int(itstring[1])
    if itname not in superMarketitems.keys():
        superMarketitems[itname] = 0
    superMarketitems[itname] += itprice
for item_name, net_price in superMarketitems.items():
    print(item_name, net_price)