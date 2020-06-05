#coding:utf-8

"""
	Cette aplication fonctionne sur Linux MacOS(X) ...
	Le code est en Python et non pas en bash(shell) pour l'executer vous devririés taper la commande suivante :
	python <--Nom_du_Fichier-->

	ATTANTION :
		Le code ne fonctionne pas sous windows car les comamde du terminal ne son pas les même
		Merci de votre compréhention en cas de probleme contacter moi à l'adresse mail suivante :
		juliedbac@gmail.com

"""
#------------------------------------#
#				VARIABLE			 #
#------------------------------------#
username = "--"
on_off = True
#
#------------------------------------#

#------------------------------------#
#				MODULE				 #
#------------------------------------#
import os
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
	if username == "--":
		userNameChoise = input("[*]vouler-vous choisir un nom d'utilisateur ?\n[1]OUI\n[2]NON\n{}>".format(username))
		if userNameChoise=="1":
			username = input("Entrée votre nom d'utilisateur \n{}>".format(username))

		elif userNameChoise=="2":
			username = ">>"

		else :
			printError()

	else:
		os.system("clear")
		print("[*]Choisir une option :\n\n[1]installation des outils \n[2] \n[3]Changer de nom \n[4]sortie")
		userChoise = input(f"{username}>")

		if userChoise == "1":
			os.system("clear")
			print("[*]Choisir une option :\n\n[1]installé les outils de phishing\n[2] \n[3] \n[4]sortie")
			userChoise = input(f"{username}>")

			if userChoise == "1":
				os.system("mkdir tools")
				os.system("cd tools")
				os.system("git clone https://github.com/thelinuxproject/instagram")
				print("operation terminer")
			elif userChoise == "4":
				on_off = 0
			else :
					printError()

		elif userChoise == "2":
			print("vous aver choisie 2:) \n")
		elif userChoise == "3":
			username = "--"
		elif userChoise == "4":
			on_off = 0
		else :
			os.system("clear")
			printError()
