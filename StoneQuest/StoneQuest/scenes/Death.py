##
## Game Over class that takes user back to Level 1
class DeathToFluffy(object):
	
	def enter(self):
	
		##
		## Tell player the game is over
		print("")
		print("                           ***************")
		print("                           ** GAME OVER **")
		print("                           ***************")
		print("----------------------------------------------------------------------")

		##
		## Ask the player if they would like to play again
		print("Would you like to continue playing?")
		
		answer = input("[y/n]> ")
	
		if answer == "y":
			return 'Fluffy'
			
		else:
			print("Goodbye!")
			exit(1)
			return 'end'
			
##
## Game Over class that takes user back to Level 4
class DeathToChess(object):
	
	def enter(self):
	
		##
		## Tell player the game is over
		print("")
		print("                           ***************")
		print("                           ** GAME OVER **")
		print("                           ***************")
		print("")
		
		##
		## Ask the player if they would like to play again
		print("Would you like to continue playing?")
		
		answer = input("[y/n]> ")
	
		if answer == "y":
			return 'WizardsChess'
			
		else:
			print("Goodbye!")
			exit(1)
			return 'end'