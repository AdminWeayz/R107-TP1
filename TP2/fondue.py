BASE = 4
fromage = 800.0
eau:float = 2.0 #dl
ail = 2.0
pain = 400

nbConvives = int(input('Nombre de convive invite :'))

quantitefromage = fromage * nbConvives / BASE
quantiteeau = eau * nbConvives / BASE
quantitepain = pain * nbConvives / BASE
quantiteail = ail * nbConvives / BASE

print(f'Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :')
print(f'\t-{quantitefromage} gr de fromage\n \t-{quantiteeau} de eau\n \t-{quantitepain} de pain\n \t-{quantiteail} de ail')