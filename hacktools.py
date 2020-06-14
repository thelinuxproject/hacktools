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


def conte_a_rebour(nombre, text="", msgfinal=""):
	os.system("clear")
	while nombre > 0:
		print(text)
		print("\n\n\ntemps {}s".format(nombre))
		sleep(1)
		nombre-=1
		os.system("clear")
	print("msgfinal")
	sleep(1)
#------------------------------------#


while on_off:
#------------------------------------#
#           choix de nom             #
#------------------------------------#
	if username == "--":
		userNameChoice = input("[*]vouler-vous choisir un nom d'utilisateur ?\n[1]OUI\n[2]NON\n{}>".format(username))
		userNameChoice = str(userNameChoice)#									cast des valeur sasi dans le but de limité les erreur


		if userNameChoice=="1":
			username = input("Entrée votre nom d'utilisateur \n{}>".format(username))
			username = str(username)#											cast des valeur sasi dans le but de limité les erreur

		elif userNameChoice=="2":
			username = ">>"

		else :
			conte_a_rebour(5, printError)
#																				choix dune option entre instalation / utilisation / chager de nom / ou sortie de hacktools
	else:
		os.system("clear")
		print("[*]Choisir une option :\n\n[1]installation des outils\n[2]Option & Réglage \n[3]Aide \n[4]Changer de nom \n[5]sortie")
		user_choice = input("{}>".format(username))
		user_choice = str(user_choice)#											choix d'une option instalation 
		if user_choice == "1":#													menu user_choise
			os.system("clear")#													netoyage du terminal
			print("[*]Choisir une option :\n\n[1]installé les outils de phishing\n[2]installé Saycheesapp \n[3] \n[4]sortie")
			user_choice_tools = input("{}>".format(username))
			user_choice_tools = str(user_choice_tools)#							cast des valeur sasi dans le but de limité les erreur
			if user_choice_tools == "1":#										choix n°1 pour istaller les outils de phishing
				os.system("mkdir tools")
				os.system("git clone https://github.com/thelinuxproject/instagram tools/instagram")#	installation de instapump
				os.system("git clone https://github.com/thelinuxproject/paypal tools/paypal")#	installation de paypal
				os.system("clear")
				conte_a_rebour(3, "téléchargement en cour...","operation terminer")#attente de 4 seconde	
			elif user_choice_tools == "2":#										choix n°1 pour istaller les outils de phishing
				os.system("mkdir tools")
				os.system("git clone https://github.com/thelinuxproject/saycheesapp tools/saycheesapp")#	installation de saycheesapp 
				os.system("clear")
				conte_a_rebour(3, "téléchargement en cour...","operation terminer")#attente de 4 seconde	
			elif user_choice_tools == "4":#										choix n°4 pour quitter le choi de téléchargement des des depots
				user_choice = "0"#												retour au menu user_choise
			else :
				conte_a_rebour(5, printError)
		
		elif user_choice == "2":
			os.system("clear")
			print("[*]Option & Réglage :\n\n[1]Clavier azerty (sur Linux)\n[2]\n[3] \n[4]sortie")
			user_option = input("{}>".format(username))
			user_option = str(user_option)#										cast de la variable user_option
			if user_option == "1":
				os.system("setxkbmap fr")
				os.system("clear")
				conte_a_rebour(3, "changement en cour...","operation terminer")
			else :
				conte_a_rebour(5, printError)

		elif user_choice == "3":
			os.system("clear")
			print("[*]Aide pour :\n\n[1]phishing\n[2]saycheesapp \n[3] \n[4]sortie")
			user_choice_help = input("{}>".format(username))
			user_choice_help = str(user_choice_help)#							cast de la variable user_chice_help
			
			if user_choice_help == "1":
				os.system("clear")
				print("[*]Aide pour :\n\n[1]instagram\n[2]paypal \n[3] \n[4]sortie")
				user_choice_help_ph = input("{}>".format(username))
				user_choice_help_ph = str(user_choice_help_ph)
				
				if user_choice_help_ph == "1":
					os.system("clear")
					conte_a_rebour(10, "\nCommandes pour créer un lien de phisning instagram sont les suivantes :\n\n\n	•cd tools/instagram\n\n	•bash instagram.sh", "au revoir :)")

				elif user_choice_help_ph == "1":
					os.system("clear")
					conte_a_rebour(10, "\nCommandes pour créer un lien de phisning paypal sont les suivantes :\n\n\n	•cd tools/paypal\n\n	•bash paypal.sh", "au revoir :)")

				else :
					conte_a_rebour(5, printError)

			elif user_choice_help == "2":
				os.system("clear")
				conte_a_rebour(10, "\nCommandes pour créer un lien de phisning instagram evc un controle sur la webcam sont les suivantes :\n\n\n	•cd tools/saycheesapp\n\n	•bash saycheesapp.sh", "au revoir :)")

			elif user_choice_help == "4":#										choix n°4 pour quitter le chois de l'outis
				user_choice = "0"#												retour au menu user_choise
			
			else :
				conte_a_rebour(5, printError)

		elif user_choice == "4":
			username = "--"#													retour au menu changer de nom
		elif user_choice == "5":
			on_off = 0#															sortir de hacktools
		else :
			conte_a_rebour(5, printError)
