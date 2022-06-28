seznam = [23, 56, 79, 154, 32]
seznam = seznam[2:4]
iterator = iter(seznam)
retezec = "ahoj"
retezec = iter(retezec)
ntice = (1, 5, 67, 8)
ntice = iter(ntice)
# seznam = next(seznam)
# print(seznam)

muj_iterator = iter("ahoj")
iterator =  next(muj_iterator)
print(iterator)

it = iter(2, 3, 5, 7, 8)
ite = next(it)
print(ite)
