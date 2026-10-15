def check(nb:float) -> str:
    if nb == 0:
        return "nul"
    elif nb > 0 and nb%2 == 0:
        return 'positif pair'
    elif nb > 0 and nb%2 == 1:
        return 'positif impair'
    elif nb < 0 and nb%-2 == 0:
        return 'negatif pair'
    else:
        return 'negatif impair'

while True:
        try:
            choice = (input("Choisissez un nombre ou q pour quitter : "))
            if choice == 'q' or choice == 'Q':
                break
            else:
                choice = float(choice)
                print(check(choice))
        except ValueError:
            print('Valeur invalide')
