w = input()
abcl = [ch for ch in w]
size = len(abcl)
if 0 < size < 27:
    list3 = []
    j = 0
#   abcl = [chr(letra) for letra in range(96 + size, 96, -1)] # List of characters to use
    for linea_num in range(len(abcl)): # Iterates over abcl
        list2 = [] # Keeps characters
        list2.append(abcl[linea_num]) # Appends the last letter in abcl
        if linea_num > 0: # The line 0 only has one element
            for m in range(linea_num, 0, -1): # Iterates over the rest of abcl
                list2.insert(0, abcl[m - 1]) # Insert a previus letter
                list2.append(abcl[m - 1]) # Appends the same to the end of the list
        list3.append(list2) # Keeps the lists
for line_list3 in list3: # Iterates over each list inside to print the upper side
        rangoli = "-".join(line_list3) # Creates a line with the inside elements of the list
        print(rangoli.center((len(list3[-1])*2)-1, "-")) # Send to STDOUT a line centered
list3.reverse() # To print the second part of the rangoli pattern
for line_list3 in list3[1:]: # Iterates over each list inside. The 1st elemnt ommited
    rangoli2 = "-".join(line_list3) # Creates a line with the inside elements of the list
    print(rangoli2.center((len(list3[0])*2)-1, "-")) # Send to STDOUT a line centered