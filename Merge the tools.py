'''
Consider the following: 
• A string, s, of length n where s = c0c1 ... cn-1
 • An integer, k, where k is a factor of n.
We can split s into substrings where each substring, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:
• The characters in ui are a subsequence of the characters in ti.
 • Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index < j in tį, then do not include the character in string ui.
Given s and k print n/k lines where each line i denotes string ui.
'''
def merge_the_tools(string, k):
    # your code goes here
    ls = len(string)
    listastring = [string[i:i+k] for i in range(0, ls,k)]
    for ministring in listastring:
        nsl=[p for o, p in enumerate(ministring) if ministring.index(p) == o]
        print("".join(nsl))

if __name__ == '__main__':
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)