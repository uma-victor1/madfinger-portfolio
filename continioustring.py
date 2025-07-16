def get_min_deletions(string: str) -> int:
    # loop over string
    # assign the element to a variable
    # change the variable if you encounter a different character
    # repeat but each time you remove and element update a count variable

    new_str = [string[0]]
    for i in range(len(string)):
        if string[i] == new_str[-1]:
            continue
        else:
            new_str.append(string[i])

    return len(string) - len(new_str)


print(get_min_deletions("AABBAAAAAAB"))
"""
news = [s[0]] // ["A", 'B"]
s = "AABBAA"
loop 6 times:
    s[i]

"""
