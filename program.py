import random
foglalt = []
sor = []
oszlop = []




for i in range(25):
    oszlop.append(i+1)
for s in range(15):
    sor.append(s+1)




class FOGLALAS():
    def __init__(self,f_oszlop,f_sor):
        self.f_oszlop = f_oszlop
        self.f_sor = f_sor


def kiir(foglalt,oszlop,sor):
    for i in range(15):
        for a in range(25):
            if a+i == foglalt[a].f_oszlop+foglalt[i].f_oszlop :
                print(f'◼', end=" ")
            else:
                print(f'☐', end=" ")
        print('')
'''
for i in range(10):
    random.shuffle(oszlop)
    random.shuffle(sor)
    foglaltak=(FOGLALAS(oszlop.pop(), sor.pop()))
    foglalt.append(foglaltak)'''
for i in range(26):
    foglaltak = FOGLALAS(random.choice(oszlop),random.choice(sor))
    foglalt.append(foglaltak)


for u in range(len(foglalt)):
    print(foglalt[u].f_sor)
    print("niaeeafrewf")
    print(foglalt[u].f_oszlop)
kiir(foglalt,oszlop,sor)