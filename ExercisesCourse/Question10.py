stringExample = input("Please enter a string")
char_count = {}

for char in stringExample:
    if char in char_count:
        char_count[char] = char_count[char] + 1
    else:
        char_count[char] = 1
print(char_count)
