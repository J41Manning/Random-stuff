#python script to figure out how Jenny will take coffee
import random


def what_do_they_say(question):
	nonsense=True
	while(nonsense):
		words=raw_input(question)
		words.lower()
		if words=='y' or words=='yes':
			return True
		elif  words=='n' or words=='no':
			return False
		else:
			print("I'm sorry I didn't get that. Can you try again?")

noCoffee=True
while(noCoffee):
	coffee= what_do_they_say("Did she ask for coffee? ")
		
	if coffee:
		break
	elif not coffee:
		wat=what_do_they_say("Are you sure? ")
		if wat:
			print("I don't believe you.\n")
		if not wat:
			print("Oh, well I'll ask again then!\n")

iced=what_do_they_say("Is it iced coffee? ")
if iced:
	print("Sweetened with no milk. Oh! Light ice please!")
else:
	roast=what_do_they_say("Blonde roast brewing? ")
	if roast:
		print("Black please.")
		exit()	
	productive=what_do_they_say("Hmm well, is she working on something? ")
	if not productive:
		if random.randint(1,20) % 7==0:
			print("Lightly sweetened and light vanilla creamer")
			print("I really mean light. Don't go overboard.")
			exit()
	print("Black please.")
