import random
import os
foglalt = []
sor = []
oszlop = []


for i in range(30):
    oszlop.append(i+1)
for s in range(7):
    sor.append(s+1)


class FOGLALAS():
    def __init__(self,f_oszlop,f_sor):
        self.f_oszlop = f_oszlop
        self.f_sor = f_sor

def kiir(foglalt,oszlop,sor):
    for i in range(len(sor)):
        for a in range(len(oszlop)):
            if  a+1 == sajat.f_oszlop and i+1 == sajat.f_sor and be=='i':
                print(f'🟩',end = " ")
            elif a+1 == sajat.f_oszlop and i+1 == sajat.f_sor:
                print(f'X', end=" ")
            elif (a+i) == (foglalt[a].f_oszlop+foglalt[i].f_oszlop) :
                print(f'◼', end=" ")
            
            
            else:
                print(f'☐', end=" ")
        print('')

for i in range(56):
    foglaltak = FOGLALAS(random.choice(oszlop),random.choice(sor))
    foglalt.append(foglaltak)

print(f"a teli négyzetek a foglathelyeket, az üres négyzetek az üres helyeket jelölik")
sajat = FOGLALAS(-1,-1)
be = ''
kiir(foglalt,oszlop,sor)
marfoglalt = False
sajatsor = int(input('Hanyadik sorban szeretnél helyet foglalni? (1-7) '))
sajatoszlop = int(input("Hanyadik helyet szeretnéd ebben a sorban? (1-30) "))
'''for a in foglalt:
    if FOGLALAS(sajatoszlop,sajatsor) == foglalt[a]:
        marfoglalt = True'''
while sajatsor > 7 or sajatoszlop > 30:

    print(f"Valamelyik bekérésnél túl nagy számot adtál meg!!")
    sajatsor = int(input('Hanyadik sorban szeretnél helyet foglalni? (1-7) '))
    sajatoszlop = int(input("Hanyadik helyet szeretnéd ebben a sorban? (1-30) "))
    
    
sajat = (FOGLALAS(sajatoszlop,sajatsor))

os.system('cls')
kiir(foglalt,oszlop,sor)
be = input("Biztosan ezt a helyet választod?(i/n) ")
if be != 'i':
    while be != 'i':
        sajatsor = int(input('Hanyadik sorban szeretnél helyet foglalni? (1-7) '))
        sajatoszlop = int(input("Hanyadik helyet szeretnéd ebben a sorban? (1-30) "))
    
        while sajatsor > 7 or sajatoszlop > 30:
    
            print(f"Valamelyik bekérésnél túl nagy számot adtál meg!!")
            sajatsor = int(input('Hanyadik sorban szeretnél helyet foglalni? (1-7) '))
            sajatoszlop = int(input("Hanyadik helyet szeretnéd ebben a sorban? (1-30) "))
    
        sajat = (FOGLALAS(sajatoszlop,sajatsor))
        kiir(foglalt,oszlop,sor)
        be = input("Biztosan ezt a helyet választod?(i/n) ")
kiir(foglalt,oszlop,sor)
print('Sikeresen lefoglaltad a helyed! \n98 ezer forint lessz! ')