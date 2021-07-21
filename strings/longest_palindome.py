def palindrome(str, left, right):
    while left>=0 and right<len(str) and str[left]==str[right]:
        left-=1
        right+=1
    return str[left+1: right]


def longest_palindome(str):
    longest_palindome=""
    
    for i in range(len(str)):
        center = palindrome(str, i, i)
        inbetween = palindrome(str, i ,i+1)

        longest_palindome = max(longest_palindome, center, inbetween, key=len)
    
    return longest_palindome

print(longest_palindome("xabcdcbay"))























# def longest_palindome(string):
#     c_longest = [0,1]
#     #string [0:1] --> slicing
#     print(string)
#     for i in range(0, len(string)):
#         #we start from 1 and not 0 as we already know that the first letter is already a palindrome
#         odd = get_Longest(string, i-1, i+1)
#         even = get_Longest(string, i-1, i)
#         longest=max(odd, even, key=lambda x: x[1]-x[0])
#         c_longest=max(longest,c_longest, key=lambda x: x[1]-x[0])
#         return c_longest
# def get_Longest(string, left, right):
#     while left>=0 and right<len(string):
#         if string[left]!= string[right]:
#             break 
#         left-=left-1
#         right+=right+1
#     return[left+1,right]
# longest_palindome("abaxyzzyxf")

