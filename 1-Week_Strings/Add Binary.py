"""
"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"
"""
def addBinary(s1, s2):
    carry = 0
    res = ''

    s1 = list(s1)
    s2 = list(s2)

    while s1 or s2 or carry:
        if s1:
            carry+=int(s1.pop())
        if s2:
            carry+=int(s2.pop())

        res += str(carry%2)
        carry//=2
    
    return res[::-1]

print(addBinary("100", "1"))
print(addBinary("11", "1"))
print(addBinary("1", "0"))

print('-------------------')
def addBinary(s1, s2):
    pass
print(addBinary("100", "1"))
print(addBinary("11", "1"))
print(addBinary("1", "0"))