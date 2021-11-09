word = input("Podaj wyraz:")

def palindrom(word):
    j=-1
    for letter in word:
        if letter == word[j]:
            j=j-1
            continue 
        else: 
            return "False"  
    return "True"

print(f"Czy to słowo jest palindromem: {palindrom(word)}")
