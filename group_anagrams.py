#group anagrams
def groupAnagrams(words):
    # dictionary
    anagrams={}

    for word in words:

        #for sorting the the letters in each word using for loop to go to each word
        sortedWord = "".join(sorted(word))
        # print(sortedWord)

        if sortedWord in anagrams:
            #for each sorted word
            anagrams[sortedWord].append(word)
        
        else:
            #make a key of that word
            anagrams[sortedWord] = [word]

        # print(anagrams)
    return list(anagrams.values())

print(groupAnagrams(("Ant","dog","bat","abt")))
