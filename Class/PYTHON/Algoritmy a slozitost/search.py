seznam = [6, 8, 9, 13]

#je osmicka v seznamu???
#find, index, in

hledana_promena = 8

for cislo in seznam:
    if cislo == 8:
        print("Hura, nalezeno, muzeme skoncit")
        break
    print("Smutne, neni tu")
    
#casova slozitost: 2 * n => o(n) = linearni
#proto se tomu rika linearni vyhledavani

# ukol napsat program binary search vyhledavani = logaritmicka slozitost
