# Manoir hanté
from random import randint
print ('Le Manoir Hanté')
je_suis_courageux = True
score = 0
while je_suis_courageux:
    porte_fantôme = randint(1, 5)
    print('Tu te retrouves face à cinq portes...')
    print('Derrière laquelle se cache le fantôme?')
    print ('Quelle porte ouvres-tu?')
    porte = input ('1, 2, 3, 4 ou 5?')
    num_porte = int(porte)
    if num_porte == porte_fantôme:
        print('UN FANTÔME!')
        je_suis_courageux = False
    else:
        print('Pas de fantôme!')
        print('Tu entres dans la prochaine salle')
        score = score + 1
print('Au secours!')
print('Partie terminée ! Ton score :', score)
input('Press ENTER to exit')
