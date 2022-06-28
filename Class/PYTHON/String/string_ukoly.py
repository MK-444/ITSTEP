def pig_latin():
    word = input("Napiste slovo: ")
    samohlaska = ['a', 'u', 'y', 'e', 'o', 'i']
    souhlaska = ['q', 'w', 'r', 't', 'p', 's', 'd', 'g', 'f', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm' ]
    if  word[0] in samohlaska:
                word += "way"
    elif word[0] in souhlaska:
            word = word.lstrip(word[0])
            word += "ay"
    print(word)
pig_latin()


def upper_word():
    word = input("Napiste slovo: ")
    if word[0].isupper == True:
        word = word[0].rstrip()
        word = word[0].upper()
        print(word)
upper_word()  
    



pc = "4567"
user = "2567"
cows = 0
for x in range(4):
    if pc[x] == user[x]:
        cows += 1
        
        

    