from sre_compile import isstring


def minion_game(string):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    consonant = 0
    vowel = 0
    
    for i in range(len(string)):
        if  string[i] in vowels:
            vowel += len(string)-i
        else:
            consonant += len(string)-i
    if consonant > vowel:
        print("Stuart " + str(consonant))
    elif consonant < vowel:
        print("Kevin " + str(vowel))
    else:
        print("Draw")

if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)