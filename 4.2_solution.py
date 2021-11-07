#pierwsza próba rozwiązania:

word = "kajak"

def palindrom(word):
    if word[0] == word[-1]:
        if word[1] == word[-2]:
            if word[2] == word[-3]:
                return "True"
            else: 
                return "False"
        else: 
            return "False"             
    else: 
        return "False"    

print(palindrom(word))

#druga próba rozwiązania:

word = "kajak"

def palindrom(word):
    j=-1
    for letter in word:
        if letter == word[j]:
            j=j-1
            continue
            return "True"        
        else: 
            return "False"    

print(palindrom(word))
