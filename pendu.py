print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<      Bienvenus dans le jeu du PENDU     >>>>>>>>>>>>>>>>>>>>>>>>>>>>' ) 
#  choisir le niveau du jeu
Niveau=[]
while Niveau != 1 and Niveau != 2 and Niveau != 3:
    Niveau = int(input("\n Niveau que vous souhaité :\n\n Débutant (15 essais) = Tapez 1 \n\n Intermediaire (10 essais) = Tapez 2 \n\n Expert (5 essais)= Tapez 3 : "))
    if Niveau == 1:
        essais_restants = 15
    elif Niveau == 2:
        essais_restants = 10
    elif Niveau == 3:
        essais_restants = 5
    else:
        print(">>>>>>>>>>>>>>>>>>>    'Error' veuillez choisir un chiffre entre ( 1, 2, ou 3 ) Merci. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ")

import re, random

# Importer un mot du fichier dictionaire au hasard 

import random

mots = []
with open("dico_france.txt") as file:
    for line in file:
        mots.append(line.rstrip("\n"))
mot_secret = random.choice(mots)
#print(mot_secret)                        #ETAPE EN PLUS POUR FAIRE APARETRE LE MOT SECRET AVANT 
points = 0
modele_du_mot = ("_"*len(mot_secret))

lettres_proposees = []
def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")
    if index < 0:
        return newstring + s
    if index > len(s):
        return s + newstring
    return s[:index] + newstring + s[index + 1:]

# Affichage
	
while True:
	print("\nModèle du mot : " + modele_du_mot)
	print("\nLettres utilisées : " + str(lettres_proposees))	
	lettre = input("\nProposez une lettre: ")

# conditions et resultats
# mots proposé par le joueur 
	if len(lettre) > 1:
		if lettre == mot_secret:
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Perfect , le mot est bien : " + mot_secret + "'.")
			break
		else:
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Erreur: le mot ne correspond pas.")
			continue
# lettre prposée par le joueur
	if lettre in mot_secret:
		if not lettre in lettres_proposees:	
			points = points + mot_secret.count(lettre)
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Bien vu ")

			for x in [m.start() for m in re.finditer(lettre, mot_secret)]:
				modele_du_mot = replacer(modele_du_mot, lettre, x)

			if points == len(mot_secret):
				print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Tu as gagné")
				break
		else:
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Cette lettre a déjà été proposée...")

	else:
		essais_restants = essais_restants - 1
		if essais_restants == 0:
			print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> T'es un loser CIAO . Le mot était : " +  mot_secret )
			break
		print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Faux. Il vous reste " + str(essais_restants) + " essais.")

	if not lettre in lettres_proposees: lettres_proposees.append(lettre)
