srazky_celkem = {}
while True:
    mesto = input("Zadey mesto: ")
    if mesto == "":
        break
    nove_zadane_srazky = int(input("Zadej kolik naprselo: "))
    
    srazky_ve_meste = srazky_celkem.get(mesto, 0)
    srazky_celkem[mesto] = srazky_ve_meste + mm_srazek
    srazky_celkem[mesto] = puvodni_srazky + nove_zadane_srazky
    # if mesto in srazky_celkem:
    #     srazky_celkem[mesto] += mm_srazek
    # else:
    #     srazky_celkem[mesto] = mm_srazek
    
    for mesto, srazek in srazky_celkem.items():
        print(mesto + ":" + str(srazek)) 
        
        
