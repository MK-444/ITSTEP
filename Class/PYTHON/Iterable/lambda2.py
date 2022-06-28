seznam = [2, 5, 6, 7, 9]

# def na_druhou(cislo):
#     return cislo * cislo 

novy_seznam = list(map(lambda x : x * x, seznam))

novy_seznam2 = list(filter(lambda x: x > 5, seznam))

# lepsi list comprehension 

seznamX = [(2, 6), (3, 13), (5, 9), (7, 3), (4, 0)]

print(sorted(seznamX, key= lambda x: x[1]))
print(max(seznamX, key= lambda x: x[1]))
print(min(seznamX, key= lambda x: x[1]))

slova = ["jablko", "ananasasaas" "adam", "Eva", "Boris", "rajcatko", "paprika"]

print(sorted(slova, key=lambda s: s.lower()))
print(sorted(slova, key=len))

