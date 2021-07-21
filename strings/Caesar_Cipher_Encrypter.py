def encrypter(string, key):
    for letter in string:
        nlc = ord(letter)+key
        if nlc <=122:
            # return chr(nlc)
            new.append(chr(nlc))
        else:
            # return chr(96+nlc%122)
            new.append(chr(96+nlc%122))
        # if ord(letter)>=97 and ord(letter)<=122:
        #     new.append(chr(ord(letter)+key))
    return "".join(new)

new=[]
key=2%26
string = "mazx"
str= encrypter(string, key)
print(str)