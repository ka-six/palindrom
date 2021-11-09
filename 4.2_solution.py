word = "kajak"

def palindrom(word):
    j=-1
    for letter in word:
        if letter == word[j]:
            j=j-1
            continue 
        else: 
            return "False"  
    return "True"

print(palindrom(word))
