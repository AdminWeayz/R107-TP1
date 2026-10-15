def check(nb:float) -> str:
    if nb == 0:
        return "nul"
    elif nb > 0:
        return 'positif'
    else:
        return 'negatif'

while True:
    choice = input("Choisissez un nombre ou q pour quitter : ")
    if choice == "q":
        break
    else:
        print(check(float(choice)))