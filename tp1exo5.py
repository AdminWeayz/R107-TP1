jour = 0
heure = 0
minute = 0

jour = int(input("Entrer un jour : "))
heure = int(input("Entrer un heure : "))
minute = int(input("Entrer un minute : "))

minute += (jour * (24 * 60) + heure * 60)
print(f"Ce mois ci il c'est passer {minute} minutes")