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
    if 0 < len(string) <= 10**6:
        s_score = 0
        k_score = 0
        vowels = 'AEIOU'
        for x in range(len(string)):
            for i in string:
                if i in vowels:
                    k_score += string.count(i)
                else:
                    s_score += string.count(i)
            string = string[:-1]
            
        if k_score > s_score:
            print("Kevin {}".format(k_score))
        elif k_score < s_score:
            print("Stuart {}".format(s_score))
        else:
            print("Draw")    
    
        
if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)