jour = 0
heure = 0
minutes = 0
temp = 0

minute = int(input("Entrer les minutes écoulé : "))

temp = minute//60
minute = minute%60
heure += temp
temp = heure//24
heure %= 24
jour += temp

print(f"{jour} octobre, {heure}:{minute}")