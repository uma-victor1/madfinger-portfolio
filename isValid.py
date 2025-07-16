import collections


def isValid(string: str) -> str:
    # Write your code here
    strdict = collections.Counter(string)

    valuearr = list(strdict.values())
    valuearr.sort()
    print(strdict)
    print(valuearr)
    if valuearr[0] == valuearr[-1]:
        return "YES"
    if valuearr[0] == 1 and valuearr[1] == valuearr[-1]:
        return "YES"
    if valuearr[-1] == valuearr[-2] + 1 and valuearr[0] == valuearr[-2]:
        return "YES"

    return "NO"


print(isValid("abcdefghhgfedecba"))


"""
[1,2,3,3,3,4,4]
str= 'abcccaabbddeeeffgg'
dict= {}

loop through the string

"""
