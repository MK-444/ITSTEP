def jeden_ukon():
    3 + 4

def pet_ukonu():
    5 + 9
    9 - 3
    12 + 1
    2 * 7
    8 - 7
    
#clovek 1:
jeden_ukon

#clovek 2:
pet_ukonu()

#1 nebo 5 ukonu  = konstantn9 slozitost 


seznam = [2, 3, 5, 7]
# nevim jak je dlouhy
# N = delka seznamu

for x in seznam:
    jeden_ukon()
    
#slozitost 1 * n = n

for x in seznam:
    pet_ukonu()
    
#slozitost 5 * n = 5n

# n nebo 2n nebo 5n = linearni slozitost

for x in seznam:
    pet_ukonu()
    
jeden_ukon()

#5 * n + 1 => 5n + 1 => 5n => n

for i in seznam:
    for j in seznam:
        jeden_ukon()
        
        
for i in seznam:
    for j in seznam:
        pet_ukonu

# 5 * n * n => n * n => n^2

        
for i in seznam:
    for j in seznam:
        for k in seznam:
            pet_ukonu()
            
# 5 * n * n * n => n * n * n => n^3

# n ^ 3 + 100 * n ^ 2 + 1000 * n + 100 000 000




