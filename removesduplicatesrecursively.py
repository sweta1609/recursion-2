def removeConsecutiveDuplicates(string):
    # Please add your code here
    pass
    l = len(string)
    if l == 0 or l == 1:
        return string
    if (string[0] == string[1]):
        output = removeConsecutiveDuplicates(string[1:])
        return output
    else:
        output = removeConsecutiveDuplicates(string[1:])
        return string[0] + output

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
