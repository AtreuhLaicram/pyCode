'''Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.'''

def minion_game(string):
    # your code goes here
    dic_scores ={}
    the_string = string.upper()
    dic_scores[the_string] = 0
    if 10**6 > len(the_string) > 0:
        lstring = [letra for letra in the_string]
        for i1 in range(len(lstring)+1):
            for i2 in range(i1+1, len(lstring)+1):
                substr = "".join(lstring[i1:i2])
                if substr == "" or not substr.isalpha():
                    pass
                elif substr not in dic_scores.keys():
                    dic_scores[substr] = 0
                dic_scores[substr] += 1
        vowels = ['A','E','I','O','U']
        wwv = 0
        wwc = 0
        for m in dic_scores.keys():
            if m[0] in vowels:
                wwv += dic_scores[m]
            else:
                wwc += dic_scores[m]
        if wwv > wwc:
            print('Kevin' + ' ' + str(wwv))
        elif wwv < wwc:
            print('Stuart' + ' ' + str(wwc))
        else:
            print('Draw')
    else:
        return
    
if __name__ == '__main__':
    s = input()
    minion_game(s)