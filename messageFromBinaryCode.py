'''You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts to find a clue, you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. After some thought, your first guess is that each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.

Assuming that your hunch is correct, decode the message.'''

def solution(code):
    bic = []
    secretPhrase = ''
    for i in range(0, len(code), 8):
        bic.append(code[i:i + 8])
    for j in range(len(bic)):
        alfa = chr(int(bic[j], base=2))
        secretPhrase += alfa
    return secretPhrase + ', always!'

if __name__ == '__main__':

    code = "01001101011000010111100100100000011101000110100001100101001000000100011001101111011100100110001101100101001000000110001001100101001000000111011101101001011101000110100000100000011110010110111101110101"
    print(solution(code))