'''Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.'''

def solution(st):
    w = list(st.strip())
    k = 2
    ale = len(w)
    if 3 <= ale <= 10:
        while w[:] != w[::-1]:
            i = ale
            if w[-(k+1)] == w[i-1] and k <= ale:
                k += 1
                ale -= 1
            else:
                w.append(w[i-k])
                k += 1
    if len(w) % 2 != 0:
        j = int(len(w) / 2)
        if w[j] == w[j - 1] and w[j + 1]:
            w.pop(j)
    return "".join(w)

if __name__ == '__main__':
    
    st = 'ababab'
    print(solution(st))