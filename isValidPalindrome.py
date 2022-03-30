def isPalindrome( s):
    s = s.replace(' ','')
    s = str(s)
    s = ''.join(filter(str.isalnum, s))
    s = s.lower()
    r ='' 
    for i in range(len(s)-1,-1,-1):
        r+=s[i]
    if (s == r):
        return True
    else:
        return False

    

inputStr = "A man, a plan, a canal: Panama"
print(isPalindrome(inputStr))