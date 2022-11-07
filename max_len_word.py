inputArray = ["enyky", "benyky", "yely", "varennyky"]
max_len_word = max(list(map(len, inputArray)))
output_array = [word for word in inputArray if len(word) == max_len_word]
print(output_array)