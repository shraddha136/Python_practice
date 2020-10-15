def getStr(s):
    ## Write your code here
    ## Transform the string
    ## Update length of string
    result = ''
    for a in s:
        result += a * 3

    s = result
    strlen = len(s)
    return [s, strlen]

print(getStr("abc"))