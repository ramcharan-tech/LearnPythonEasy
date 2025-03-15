def checkbalanced(str):
    dict = {"{":"}","[":"]","(":")"}
    stack = []
    for s in str:
        if s in dict:
            stack.append(s)
        elif not stack or s!=dict[stack.pop()]: 
            return False
    return True if not stack else False

print(checkbalanced("{}"))