# rjust()
# center()
# rjust()
# ljust()
# startswith()
# endswitch()
# replace()
# find()
# rfind()
# chr(49)
# ord("a")
# sort()


def calculate(word):
    """Calculates how many vowels are in the word"""
    vowels = 0
    for letter in word:
        if letter.isalpha():
            if letter.lower() in 'aeiouy':
                vowels += 1
    print(vowels)
calculate("elephant")


#=====================================

sent = "ahoj jak se mas"
sent_title = sent.title()
print(sent_title)

sent_lower = sent_title.lower()
print(sent_lower)

sent_upper = sent_lower.upper()
print(sent_upper)

sent_first_letter = sent_lower.capitalize()
print(sent_first_letter)



#=======================

def caesars_cipher_next(word, num_move):
    #Caesar's cipher - the letters move to the next letter in the alphabet
	result = ""
	for i in range(len(word)):
		char = word[i]
		if (char.isupper()):
			result += chr((ord(char) + num_move - 65) % 26 + 65)
		else:
			result += chr((ord(char) + num_move - 97) % 26 + 97)
	return result
word = "ahoj"
num_move = 1
print ("Text : " + word)
print ("Shift : " + str(num_move))
print ("Cipher: " + caesars_cipher_next(word, num_move))







def caesars_cipher_previously(word, num_move):
    #Caesar's cipher - the letters move to the letter previously in the alphabet
    result = ""
    for i in range(len(word)):
        char = word[i]
        if (char.isupper()):
            result += chr((ord(char) - num_move - 65) % 26 + 65)
        else:
            result += chr((ord(char) - num_move - 97) % 26 + 97)
    return result
word = "bipk"
num_move = 1
print ("Text : " + word)
print ("Shift : " + str(num_move))
print ("Cipher: " + caesars_cipher_previously(word, num_move))


#===========================

def find_longest_substring():
    """
    funkci, která vezme řetězec, a najde nejdelší podřetězec,
    ve kterém jsou písmena řazená podle abecedy
    """
    string = "azcbobobegghakl"
    longest = string[0]
    current = string[0]
    for letter in string[1:]:
        if letter >= current[-1]:
            current += letter
            if len(current) > len(longest):
                longest = current
        else:
            current = letter
    print (longest)
print(find_longest_substring())


def sort_string_alphab(str):
    """
    Napište funkci, která vezme řetězec 
    a seřadí písmena v něm podle abecedy
    """
    str = ''.join(sorted(str))
    print(str)
s = "bac"
sort_string_alphab(s)




def count_occurs():
    """
    Spočíta, kolikrát se ve slově vyskytuje sekvence "bob"
    """
    string = 'azcbobobegghakl'
    occurs = 'bob'
    count = 0
    flag = True
    start = 0
    while flag:
        a = string.find(occurs, start)  
        if a == -1:          
            flag = False
        else:               
            count += 1        
            start = a + 1
    print(count)
count_occurs()


def set_country():
    country = {"Czech Republic", "Russia", "USA", "Germany"}
    print(country)
    getCountry = input("Write: \n■ 1 Add a country;\n■ 2 Delete a country;\n■ 3 Search for a country by entered characters;\n■ 4 Check whether the country exists inside the set:\n")
    if getCountry == '1':
            whatCountry = input("What county you want to add?: ")
            country.add(whatCountry)
            print(country)
    elif getCountry == '2':
        whatCountry = input("What county you want to remove: ")
        country.remove(whatCountry)
        print(country)
    elif getCountry == '3':
        whatCountry = input("character search: ")
        for i in country:
            if i[0] == whatCountry:
                print(i)
        print(country)
    elif getCountry == '4':
        whatCountry = input("What county exists: ")
        if whatCountry in country:
            print("Yes")
        else:
            print("No")
        print(country)
print(set_country())