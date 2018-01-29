class Fluffy(object):
	
	def enter(self):
	
		##
		## Print the introductory narrative for Level 1
		print("\n")
		print("                    ******************************")
		print("                    ** LEVEL ONE: FLUFFY'S LAIR **")
		print("                    ******************************")
		print("----------------------------------------------------------------------")
		print("Approaching the end of the third-floor corridor, you find the door to")
		print("Fluffy's chamber left ajar. You enter and are faced with a dreadful")
		print("sight: the enormous three-headed dog is crouching with his teeth")
		print("bared ready to devour you.\n")
		
		input("Press Enter to continue...")
		print("")
		
		print("You, Harry, know from your conversation with Hagrid earlier that day")
		print("that Fluffy will fall asleep if he hears the first 14 notes of a ")
		print("skillfull rendition one of his favorite songs. You are equipped with ")
		print("the small wooden C-Major flute that Hagrid gave you for Christmas. But")
		print("what tune to play with it? You vaguely recall Hagrid letting slip that ")
		print("Fluffy's favorite composer is Mozart and that he prefers to dream of")
		print("the celestial dance.")
		print("----------------------------------------------------------------------\n")
		
		##
		## Get user input for the notes of the song.
		print("Play a song for Fluffy by inputting note names on the flute (e.g. edcegfec).")
		
		song = input("[flute]> ")
		
		if song == "ccggaagffeeddc":
			print("\n----------------------------------------------------------------------")
			print("You've played Fluffy's favorite song! The beast's growls subside into") 
			print("snores and he slumps to the floor. His sleep appears to be deeper than")
			print("Hagrid's pockets. Ron opens the trapdoor and each of you fling yourselves ")
			print("recklessy into the darkness below.")
			print("----------------------------------------------------------------------")
			
			print("")
			input("Press Enter to continue...")
			
			return 'DevilsSnare'
		
		else:
			print("\n----------------------------------------------------------------------")
			print("Fluffy finds your selection displeasing! He lets out a deafening growl and")
			print("devours you with the mythical voracity of Cerberus.")	
			print("----------------------------------------------------------------------")
			
			print("")
			input("Press Enter to continue...")
			
			return 'DeathToFluffy'