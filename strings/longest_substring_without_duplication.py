def longest_substring_without_duplication(s):
    sub={}
    cur_sub_start = 0#it will move up whenever we will find duplicate
    cur_length = 0
    longest_length = 0
    #Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
    for i,letter in enumerate(s):
        #i-->index
        if letter in sub and sub[letter] > cur_sub_start:
            cur_sub_start = sub[letter]+1
            #sub[letter] is indexposition of duplicate
            #update our current length
            cur_length = i - sub[letter]
            sub[letter] = i
        
        else:
            # sub[letter] = i
            cur_length = cur_length+1
            if cur_length > longest_length:
                longest_length = cur_length

        return longest_length

s = "abcdecfab"
print(longest_substring_without_duplication(s))
