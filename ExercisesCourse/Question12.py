def count_repeated_characters(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)
    repeated_chars = {char: count for char, count in char_count.items() if count > 1}
    return repeated_chars


sample_string = 'thequickbrownfoxjumpsoverthelazydog'
repeated_characters = count_repeated_characters(sample_string)
print(repeated_characters)
for char, count in repeated_characters.items():
    print(char, count)
