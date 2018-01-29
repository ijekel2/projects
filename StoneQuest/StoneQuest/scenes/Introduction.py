from sys import exit

class Introduction(object):
	
	def enter(self):
	
		##
		## Print the game title and description.
		print("\n\n\n\n\n\n\n\n\n\n")
		print("                          *****************")
		print("                          ** STONE QUEST **")
		print("                          *****************")
		print("----------------------------------------------------------------------")
		print("In this thrilling adventure, you will guide Harry, Ron, and Hermione")
		print("through several deadly challenges in a quest to save the Sorcerer's")
		print("Stone from the clutches of the evil and power-hungry Severus Snape.")
		print("----------------------------------------------------------------------\n")
		
		##
		## Ask the user if they want to play the game.
		print("Would you like to play?")
		answer = input("[y/n]> ")
		
		if answer == "y":
			return 'Fluffy'
		else:
			print("Goodbye!")
			exit(1)
		