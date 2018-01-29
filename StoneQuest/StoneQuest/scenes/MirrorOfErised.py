class MirrorOfErised(object):
	
	def enter(self):
	
		##
		## Print the introductory narrative for Level 6
		print("\n")
		print("                 *************************************")
		print("                 ** LEVEL SIX: THE MIRROR OF ERISED **")
		print("                 *************************************")
		print("----------------------------------------------------------------------")
		print("You, Harry, having passed through the flames, find yourself standing")
		print("at the top a staircase that runs around the small chamber as if  ")
		print("cajoling all potentional occupants to descend into the center of the ")
		print("room and toward the dangers that await. Indeed at the foot of the")
		print("stairs you see the profile of a full grown man standing transfixed")
		print("before a beautiful yet terrible full length mirror. However, moving")
		print("forward, you observe not the greasy visage of the long-expected Snape,")
		print("but the lanky form of Professor Quirrel, his eyes staring madly into")
		print("the mirror, and his turban quivering with frustration. \n")
		
		print("\"Ah! The ever-meddlesome Potter has arrived at last! Just as you")
		print("predicted, my master. But now... how to obtain the stone?!\"\n")
		
		print("You are not sure who Quirrell is talking to, but you are filled with")
		print("righteous indignation upon discoving the true identity of your enemy.\n")
		
		print("\"QUIRREL! You murderous snake,\" you begin as you descend the steps.")
		print("\"How I have desired to meet you face to face, to be the instrument ")
		print("of your comeuppance! Too long have you oppressed the weak and gorged")
		print("yourself on the fear of the powerless! Too long have you sipped the")
		print("blood of unicorns and wiped your lips with the lush velvet of your")
		print("sinister turban! TODAY THIS ENDS!\"\n")
		
		input("Press Enter to continue...")
		print("")
		
		print("Quirrell is temporarily stunned by your hitherto unsuspected fiery")
		print("eloquence. You take the opportunity to push him aside and plant")
		print("yourself firmly in front of the mirror.\n")
		
		print("You recognize this mirror from your previous nighttime jaunts around")
		print("the castle. It is the Mirror of Erised, and to those who gaze into")
		print("its depths it reflects visions of their hearts' deepest desires.")
		print("As you position yourself in front of the mirror, you see a reflected")
		print("Harry placing the Sorcerer's Stone into his pocket. You feel an")
		print("object in your own pocket that certainly was not there a moment")
		print("before.\n")
		
		print("Quirrell's face changes slowly from surprise to cunning curiosity.")
		print("You realize that you have obtained the stone, but now you must invent")
		print("a convincing lie to tell Quirrell when he asks you what you have seen.")
		print("Luckily, Dumbledore forsaw that the savior of the stone would need to")
		print("furnish a quality fib. You see writing appear in the mirror:\n")
		
		print("         LSMFYE OLEOWN FOAI COSSK HKCIT ESE LONGHDI IRAP\n")
		
		print("\"What do you see in the mirror, boy?\"")
		print("----------------------------------------------------------------------\n")
		
		##
		## Get the user's input in response to Quirrell's question.'
		print("Respond to Quirrell with a convincing lie. Make sure to use correct")
		print("punctuation so as not to arouse suspicion.")
		
		lie = input("[fib]>")
		
		if lie == "I see myself holding a pair of thick, woolen socks.":
			print("----------------------------------------------------------------------")
			print("Quirrell is entirely convinced, but suddenly you hear a high, cold")
			print("voice emanating from his turban.\n")
			
			print("\"He liieeeesss!\"")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'Voldemort'
			
		elif "," not in lie:
			print("----------------------------------------------------------------------")
			print("Quirrell is a stickler for punctuation, and your missing comma rouses")
			print("his suspicion.\n")
			
			print("\"Turn out your pockets, Potter!\"")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		elif "." not in lie:
			print("----------------------------------------------------------------------")
			print("Quirrell is a stickler for punctuation, and your missing period rouses")
			print("his suspicion.\n")
			
			print("\"Turn out your pockets, Potter!\"")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		else:
			print("----------------------------------------------------------------------")
			print("Quirrell does not find your lie plausible and his suspicion is roused.\n")
			
			print("\"Turn out your pockets, Potter!\"")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
		
		