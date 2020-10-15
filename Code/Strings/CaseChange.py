def changeCase(s):
    # Write your code here
    a = s.upper() # convert string to "AAA BBB CCC"
    b = a.lower() # convert string to "aaa bbb ccc"
    return [a, b]

str = "AAA bbb CCC"
print(changeCase(str))