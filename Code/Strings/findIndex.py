def findOccurence(s):
    # Write your code here
    a = s.find('b')  #find first occurrence of "b" in the string
    b = s.find('ccc')#find first occurence  of "ccc" in the string
    return [a, b]

print(findOccurence('aaabbbccc'))