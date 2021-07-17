#O(n)time/ O(n)space
def isPalindrome(string, i=0):
    j = len(string)-1-i
    #if i=1, j=len(String)-1-1 --->2nd last ele
    return True if i>=j else string[i]==string[j] and isPalindrome(string, i+1)

string="abcdcba"
ans=isPalindrome(string)
if ans==True:
    print("palindrome")
else:
    print("not")