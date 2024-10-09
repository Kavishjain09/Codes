def Duplicate_Char(s):
    seen=set()
    for i in s:
        if i not in seen:
            seen.add(i)
        else:
            return True
    return False
print(Duplicate_Char("abcde"))
print(Duplicate_Char("aaabbcde"))