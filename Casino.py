# -*-coding:Utf-8 -*
import os # On importe le module os pour faire pause
import random # On importe le module random pour générer le nombre aléatoire de la roulette
import math # On importe le module math

# Le joueur saisit son solde de départ, on vérifie qu'il rentre un nombre valide
solde = 0
while solde <= 0:
	solde = input("Saisissez votre solde ")
	try:
		solde = int(solde)
	except ValueError:
		print("Veuillez saisir un nombre")
		solde = 0
		continue
	if solde <= 0:
		print("Saisissez un solde positif")

while solde > 0: #Tant que le joueur a de l'argent

	#Saisie de la mise
	mise = 0
	while mise <= 0 or solde < mise:
		mise = input("Saisissez votre mise ")
		try:
			mise = int(mise)
		except ValueError:
			print("Veuillez saisir un nombre")
			mise = -1
			continue
		if solde < mise:
			print("Vous n'avez pas assez d'argent")
		if mise <= 0:
			print("Saisissez une mise positive")
			
	
	solde = solde - mise
	
	#Saisie du numéro que le joueur choisi
	num_joueur = -1
	while num_joueur < 0 or num_joueur > 49:
		num_joueur = input("Choisissez un numéro entre 0 et 49 sur lequel miser ")
		try:
			num_joueur = int(num_joueur)
		except ValueError:
			print("Veuillez saisir un nombre")
			num_joueur = -1
			continue
		if num_joueur < 0 or num_joueur > 49:
			print("Ce nombre n'est pas compris entre 0 et 49")
		

	num_gagnant = random.randrange(50)
	print("le numéro gagnant est le ", num_gagnant)

	if num_joueur == num_gagnant:
		solde += (mise + mise * 3)
		print ("Jackpot, votre numéro est bien le numéro gagant gain = : ", mise * 3, "nouveau solde = ", solde)
	elif num_joueur % 2 == num_gagnant % 2:
		solde += + math.ceil(mise + mise / 2)
		print ("Pas si mal, gain = : ", math.ceil(mise / 2), "nouveau solde = ", solde)
	else:
		print ("perdu, nouveau solde = ", solde)
		
	if solde == 0:
		print("Vous n'avez plus d'argent. Fin de la partie")

os.system("pause") #Pause du programme