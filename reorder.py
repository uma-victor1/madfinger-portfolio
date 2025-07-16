# logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]


# Output: [
#     "let1 art can",
#     "let3 art zero",
#     "let2 own kit dig",
#     "dig1 8 1 5 1",
#     "dig2 3 6",
# ]

# logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
Output = ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]


def reorderData(logarr: list[str]) -> list[str]:
    pass
    """
    check the second elemement in the each item of arr
    if it starts with a number its a digit log so append to new array and remove from the current array.
    
    sort the letter logs by content that remain in arr lexicographically
    check if two sorted content lexicographically are same then sort by indentifiers  
    
    """
    digitarr = []

    for item in logarr[:]:
        # check that second element in item is number
        if item.split()[1].isdigit():
            digitarr.append(item)
            logarr.remove(item)

        ## sort letterlogs
    logarr.sort(key=lambda log: (log.split(" ", 1)[1], log.split(" ", 1)[0]))
    print(logarr + digitarr)
    return logarr + digitarr


reorderData(
    ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
)

# a = {"g1": "act zoo", "a8": "act zoo"}
# print(sorted(list(a.values())))
# print(sorted(list(a.values())))
# for key, val in a.items():
#     for item in list(a.values()):
#         if val == item:
#             print(key, val)
