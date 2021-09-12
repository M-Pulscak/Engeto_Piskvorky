from os import system

pole = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
oddelovac = "~" * 40
hra, volba, hrac = True, True, "X"
volna_pole = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(oddelovac, "   Vitej ve hre   P I S K V O R K Y", oddelovac, sep="\n")
print("PRAVIDLA HRY")
print('''2 hraci umistuji stridave na hraci pole sve znacky X/O.
Vitezi hrac, kteremu se podari obsadit 3 sousedici pole
v rade, sloupci nebo diagonalne.
Znacky umistujes zadanim cisla volneho policka od 1-9.
Hru spust libovolnou klavesou, hodne stesti ;)''')
input()

while hra:
    system("cls")
    print('', "     +---+---+---+", f"     | {(pole[1])} | {pole[2]} | {pole[3]} |",
          "     +---+---+---+", f"     | {(pole[4])} | {pole[5]} | {pole[6]} |",
          "     +---+---+---+", f"     | {(pole[7])} | {pole[8]} | {pole[9]} |",
          "     +---+---+---+", oddelovac, sep="\n")

    #   Slouceni policek do rad, sloupcu a diagonal
    rada1, rada2, rada3 = pole[1:4], pole[4:7], pole[7:10]
    sloup1 = pole[1] + pole[4] + pole[7]
    sloup2 = pole[2] + pole[5] + pole[8]
    sloup3 = pole[3] + pole[6] + pole[9]
    diag1 = pole[1] + pole[5] + pole[9]
    diag2 = pole[3] + pole[5] + pole[7]

    #   Vyhodnoceni viteze
    if rada1.count("X") == 3 or rada2.count("X") == 3 or rada3.count("X") == 3:
        print("Gratuluji, hrac X zvitezil!", oddelovac, sep="\n")
        exit()
    elif sloup1.count("X") == 3 or sloup2.count("X") == 3 or sloup3.count("X") == 3:
        print("Gratuluji, hrac X zvitezil!", oddelovac, sep="\n")
        exit()
    elif diag1.count("X") == 3 or diag2.count("X") == 3:
        print("Gratuluji, hrac X zvitezil!", oddelovac, sep="\n")
        exit()

    if rada1.count("O") == 3 or rada2.count("O") == 3 or rada3.count("O") == 3:
        print("Gratuluji, hrac O zvitezil!", oddelovac, sep="\n")
        exit()
    elif sloup1.count("O") == 3 or sloup2.count("O") == 3 or sloup3.count("O") == 3:
        print("Gratuluji, hrac O zvitezil!", oddelovac, sep="\n")
        exit()
    elif diag1.count("O") == 3 or diag2.count("O") == 3:
        print("Gratuluji, hrac O zvitezil!", oddelovac, sep="\n")
        exit()

    #  Vycerpana pole
    if pole.count(" ") == 1:
        print("Vsechna pole obsazena, konec hry. REMIZA", oddelovac, sep="\n")
        exit()

    #    Kontrola vstupu od hrace
    while volba:
        vstup = input(f"Hraje hrac {(hrac)}  Zadej cislo pole: ")
        if not vstup.isnumeric():
            print(f"{(vstup)} neni cislo, zkus to znova!")
            continue
        elif int(vstup) not in list(range(1, 10)):
            print(f"{(vstup)} je mimo hraci pole, zkus to znova!")
            continue
        elif int(vstup) not in volna_pole:
            print("Policko je obsazene! Zkus to znova!")
            continue
        vstup = int(vstup)
        volna_pole.remove(vstup)
        break

    #     Stridani hracu a prirazeni hracova symbolu
    pole[int(vstup)] = hrac  # policko zvoleneho indexu se zameni za hracuv X/O
    hrac = ["X", "O"][hrac == "X"]
