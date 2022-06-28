from random import choice, seed


class NahodnaProchazka:
    def __init__(self, pocet_kroku=5000):
        self.pocet_kroku =pocet_kroku
        self.kroky_X = []
        self.kroky_Y = []
        
    def vytvor(self):
        x = 0
        y = 0
        smery = [-1, 1]
        rychlost = [0,1,2,3]
        #self.kroky.append((x, y))
        self.kroky_X.append(x)
        self.kroky_Y.append(y)
        seed(53)
        for _ in range(self.pocet_kroku):
            smer_x = choice(smery)
            smer_y = choice(smery)
            rychlost_x = choice(rychlost)
            rychlost_y = choice(rychlost)
            x += smer_x * rychlost_x
            y += smer_y * rychlost_y
            #self.kroky.append((x,y))
            self.kroky_X.append(x)
            self.kroky_Y.append(y)
# bacha, muze spusobit konflikt z obvykle aliasem pro NumPy  - radej takto nedelat
np = NahodnaProchazka(100)
np.vytvor()

print(np.kroky_X)
print(np.kroky_Y)