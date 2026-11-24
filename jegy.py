
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
            if a+1 == sajat.f_oszlop and i+1 == sajat.f_sor and be=='i':
                print(f'🟩',end = " ")
            elif a+1 == sajat.f_oszlop and i+1 == sajat.f_sor:
                print(f'X', end=" ")
            elif any(a+1 == x.f_oszlop and i+1 == x.f_sor for x in foglalt):
                print(f'◼', end=" ")
            else:
                print(f'☐', end=" ")
        print('')

for i in range(random.randint(5, 205)):
    foglaltak = FOGLALAS(random.choice(oszlop),random.choice(sor))
    foglalt.append(foglaltak)

print(f"A teli négyzetek a foglalt helyeket, az üres négyzetek az üres helyeket jelölik.\n")
sajat = FOGLALAS(-1,-1)
be = ''
kiir(foglalt,oszlop,sor)
marfoglalt = False
print("Az 1-3. sor 4000 Ft, a többi 2000 Ft")
sajatsor = int(input('Hanyadik sorban szeretnél helyet foglalni? (1-7) '))
sajatoszlop = int(input("Hanyadik helyet szeretnéd ebben a sorban? (1-30) "))

while sajatsor > 7 or sajatsor < 1 or sajatoszlop > 30 or sajatoszlop < 1:
    print(f"Valamelyik bekérésnél túl nagy vagy túl kicsi számot adtál meg!!")
    sajatsor = int(input('Hanyadik sorban szeretnél helyet foglalni? (1-7) '))
    sajatoszlop = int(input("Hanyadik helyet szeretnéd ebben a sorban? (1-30) "))

marfoglalt = any(x.f_oszlop == sajatoszlop and x.f_sor == sajatsor for x in foglalt)

while marfoglalt:
    print("Ez a hely már foglalt! Válassz másikat!")
    sajatsor = int(input('Hanyadik sorban szeretnél helyet foglalni? (1-7) '))
    sajatoszlop = int(input("Hanyadik helyet szeretnéd ebben a sorban? (1-30) "))

    while sajatsor > 7 or sajatsor < 1 or sajatoszlop > 30 or sajatoszlop < 1:
        print(f"Valamelyik bekérésnél túl nagy vagy túl kicsi számot adtál meg!!")
        sajatsor = int(input('Hanyadik sorban szeretnél helyet foglalni? (1-7) '))
        sajatoszlop = int(input("Hanyadik helyet szeretnéd ebben a sorban? (1-30) "))

    marfoglalt = any(x.f_oszlop == sajatoszlop and x.f_sor == sajatsor for x in foglalt)

sajat = (FOGLALAS(sajatoszlop,sajatsor))
ar = 0
os.system('cls')
kiir(foglalt,oszlop,sor)
be = input("Biztosan ezt a helyet választod?(i/n) ")
if be != 'i':
    while be != 'i':
        os.system('cls')
        sajat = FOGLALAS(-1,-1)
        kiir(foglalt,oszlop,sor)
        sajatsor = int(input('Hanyadik sorban szeretnél helyet foglalni? (1-7) '))
        sajatoszlop = int(input("Hanyadik helyet szeretnéd ebben a sorban? (1-30) "))

        while sajatsor > 7 or sajatsor < 1 or sajatoszlop > 30 or sajatoszlop < 1:
            os.system('cls')
            print(f"Valamelyik bekérésnél túl nagy vagy túl kicsi számot adtál meg!!")
            sajatsor = int(input('Hanyadik sorban szeretnél helyet foglalni? (1-7) '))
            sajatoszlop = int(input("Hanyadik helyet szeretnéd ebben a sorban? (1-30) "))

        marfoglalt = any(x.f_oszlop == sajatoszlop and x.f_sor == sajatsor for x in foglalt)

        while marfoglalt:
            print("Ez a hely már foglalt! Válassz másikat!")
            sajatsor = int(input('Hanyadik sorban szeretnél helyet foglalni? (1-7) '))
            sajatoszlop = int(input("Hanyadik helyet szeretnéd ebben a sorban? (1-30) "))

            while sajatsor > 7 or sajatsor < 1 or sajatoszlop > 30 or sajatoszlop < 1:
                os.system('cls')
                print(f"Valamelyik bekérésnél túl nagy vagy túl kicsi számot adtál meg!!")
                sajatsor = int(input('Hanyadik sorban szeretnél helyet foglalni? (1-7) '))
                sajatoszlop = int(input("Hanyadik helyet szeretnéd ebben a sorban? (1-30) "))

            marfoglalt = any(x.f_oszlop == sajatoszlop and x.f_sor == sajatsor for x in foglalt)

        sajat = (FOGLALAS(sajatoszlop,sajatsor))
        kiir(foglalt,oszlop,sor)

        be = input("Biztosan ezt a helyet választod?(i/n) ")

os.system('cls')
kiir(foglalt,oszlop,sor)
if sajatsor<=2:
    ar = 4000
else:
    ar = 2000
print(f'Sikeresen lefoglaltad a helyed!\n{ar} Ft lesz! ')
