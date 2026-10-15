nb1 = int(input("Entrer un premier nombre :"))
nb2 = int(input("Entrer un second nombre :"))

print(f'Avant la permutation\nPremier nombre : {nb1} \nSecond nombre : {nb2}')
nb1, nb2 = nb2, nb1
print(f'Après la permutation\nPremier nombre : {nb1} \nSecond nombre : {nb2}')