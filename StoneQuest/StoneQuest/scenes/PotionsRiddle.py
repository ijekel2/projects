class PotionsRiddle(object):
	
	def enter(self):
		
		##
		## Print the introductory narrative for Level 5
		print("\n")
		print("                   ********************************")
		print("                   ** LEVEL FIVE: POTIONS RIDDLE **")
		print("                   ********************************")
		print("----------------------------------------------------------------------")
		print("As soon as both of you have passed through the archway, flames leap up")
		print("behind you, barring your retreat. Similarly, flames stand guard in an")
		print("archway on the opposite side of the chamber. The only notable feature of")
		print("the room you now occupy is a wooden table that stands between you and the")
		print("opposite wall. On this table have been placed a scroll of parchment")
		print("and a line of seven bottles of various shapes and sizes, containing liquids")
		print("of varying color and viscosity. Hermione reaches out, picks up the")
		print("scroll, and reads aloud...\n")
		
		input("Press Enter to continue...")
		print("")
		
		print("Danger lies before you, while safety lies behind,")
		print("Two of us will help you, whichever you would find,")
		print("One among us seven will let you move ahead,")
		print("Another will transport the drinker back instead,")
		print("Two among our number hold only nettle wine,")
		print("Three of us are killers, waiting hidden in line.")
		print("Choose, unless you wish to stay here forevermore,")
		print("To help you in your choice, we give you these clues four:")
		print("First, however slyly the poison tries to hide")
		print("You will always find some on nettle wine's left side;")
		print("Second, different are those who stand at either end,")
		print("But if you would move onward, neither is your friend;")
		print("Third, as you see clearly, all are different size,")
		print("Neither dwarf nor giant holds death in their insides;")
		print("Fourth, the second left and the second on the right")
		print("Are twins once you taste them, though different at first sight.\n")
		
		input("Press Enter to continue...")
		print("")
		
		print("You, Hermione, realize that Harry will be of no use with this challenge,")
		print("but nevertheless, he must be the one to go forward. To help you solve the ") 
		print("riddle you take out your trusty pocket tape measure and measure the height")
		print("of the bottles from left to right. You obtain the following measurements:")
		print("(1) 4.5 in.")
		print("(2) 6.5 in.")
		print("(3) 4.25 in.")
		print("(4) 8 in.")
		print("(5) 4.75 in.")
		print("(6) 9.25 in.")
		print("(7) 4.5 in.\n")
		print("----------------------------------------------------------------------\n")
		
		##
		## Prompt the user to input the answers to the riddle.
		print("Choose which draught to give to Harry and which to drink yourself (Choose")
		print("a bottle by inputting its place in line from left to right).")
		
		##
		## Get user input for the position of Hermione's bottle.
		hermione = input("[Hermione's draught]>")
		
		if hermione == "7":
			print("----------------------------------------------------------------------")
			print("You choose the bottle on the far right, confident that it will allow")
			print("you to return to the previous room.")
			print("----------------------------------------------------------------------")
			
		elif hermione == "3":
			print("You believe you can face the coming challenges better than Harry, who")
			print("clearly has an inferior intellect. You drink from the smallest bottle")
			print("and plow into the next chamber. Unfortunately you do not possess the ")
			print("the requisite amount of moral fiber to complete the coming challenges")
			print("without Harry. Your mission is doomed, and Snape will prevail. ")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		elif hermione == "2" or hermione == "6":
			print("----------------------------------------------------------------------")
			print("Delicious! Delighted by the taste of the drink, you down the rest of")
			print("it quickly. Your head begins swimming pleasantly and you stop overthinking")
			print("the riddle. The answer becomes obvious to you and, forgetting to tell")
			print("Harry which potion to drink, you swallow a mouthful from the appropriate")
			print("bottle walk through the flames and back into the Chess room. The effects")
			print("of the potion wear off immediately and you are unable to return and help")
			print("Harry. He cannot solve the riddle without you. All hope is lost. ")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		else:
			print("----------------------------------------------------------------------")
			print("Poison! You keel over and lie motionless. Harry cannot solve the")
			print("riddle without you. All hope is lost.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
		
		##
		## Get input for the position of Harry's bottle.
		harry = input("[Harry's draught]>")
		
		if harry == "3":
			print("----------------------------------------------------------------------")
			print("You hand Harry the smallest bottle and he drinks it down with relish")
			print("before sauntering through the flames into the unknown. You drink from")
			print("your own bottle and make your way back to Ron's limp form, which is")
			print("resting conspiciously in the former chamber.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'MirrorOfErised'
			
		elif harry == "7":
			print("----------------------------------------------------------------------")
			print("Harry, a tortured and impatient soul, snatches the bottle from your")
			print("hand, drinks from it, and runs into the flames, which consume him. You")
			print("cannot hope tocomplete the upcoming challenges without him. All is lost.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		elif harry == "2" or harry == "6":
			print("----------------------------------------------------------------------")
			print("Delicious! Delighted by the taste of the drink, Harry downs the rest of")
			print("it quickly. His head begins swimming pleasantly and he feels invincible!")
			print("He charges toward the flames and is consumed by the fire.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		else:
			print("----------------------------------------------------------------------")
			print("Poison! Harry keels over and lies motionless. All hope is lost.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		
		
		
		