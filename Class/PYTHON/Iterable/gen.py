
# def my_generator():
#     slovnik = {"klic": 2}
#     for klic in slovnik.keys():
#         if klic.sartswitch("a"):
#             yield slovnik[klic].capitalize()
#     yield 5
#     print("ahoj, jak se mas")
#     yield 6
#     yield 7 
#     yield 8
    
# gen1 = my_generator()
# print(next(gen1))

def my_generation():
    seznam = [1,2,3,4,5]
    for i in seznam:
        yield i * i 
    # a = 5
    # for i in range(3):
    #     a = a * 5
    #     yield a 
        
for cislo in my_generation():
    print(cislo)