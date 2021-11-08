#pierwsza próba rozwiązania:

word = "kajak"

def palindrom(word):
    for i in range(len(word)):
        p = 0
        o = -1
        if word[p] == word[o]:
            p = p+1
            o = o-1
            return "True"            
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

#proszę o podpowiedź :(