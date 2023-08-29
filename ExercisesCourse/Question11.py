def swap_and_combine_strings(str1, str2):
    if len(str1) >= 2 and len(str2) >= 2:
        new_str1 = str2[:2] + str1[2:]
        new_str2 = str1[:2] + str2[2:]
        result = new_str1 + ' ' + new_str2
        return result
    else:
        return "Both strings should have at least 2 characters."

# Sample strings
string1 = 'abc'
string2 = 'xyz'

# Call the function and print the result
result = swap_and_combine_strings(string1, string2)
print(result)
