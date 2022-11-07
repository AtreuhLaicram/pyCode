import re
'''An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").

The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. Here you can look at several examples of correct and incorrect email addresses.

Given a valid email address, find its domain part.'''

def solution(address):
    patternts = r"([\w.%+-]+)@([^.][\w.-]+)"
    addressParts = re.search(patternts, address)
    if addressParts[1] != None and addressParts[2] != None:
        return addressParts[2]

if __name__ == '__main__':
    
    address = 'marcialh@mhcomputadoras.mx'
    print(solution(address))