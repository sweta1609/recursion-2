def removeX(string,x): 
    pass
    l = len(string)
    if l == 0:
        return " "
    if string[0] == x:
        return  removeX(string[1:],x)
    return string[0] + removeX(string[1:],x)

# Main
string = input()
print(removeX(string,'x'))
