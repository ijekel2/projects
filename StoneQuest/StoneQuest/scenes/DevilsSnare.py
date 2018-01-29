class DevilsSnare(object):

	def enter(self):
	
		##
		## Print the introductory narrative for Level 2
		print("\n")
		print("                    ******************************")
		print("                    ** LEVEL TWO: DEVIL'S SNARE **")
		print("                    ******************************")
		print("----------------------------------------------------------------------")
		print("You all land on a large plant, which cushions your falls nicely.")
		print("However, the plant begins to wind its tendrils surreptitiously around")
		print("your legs. Hermione recognizes the danger and scampers out of reach of")
		print("the creeping limbs, while Harry and Ron are bound tightly and rendered")
		print("helpless. The tendrils slowly creep toward the boys' throats.\n")
		
		input("Press Enter to continue...")
		print("")
		
		print("You, Hermione, know from Herbology class that this disagreeable plant")
		print("is called Devil's Snare, and that it will shrink away in the presence")
		print("of fire. However, you cannot remember an incantation that would allow")
		print("you to produce fire magically! Just as you are beginning to panic, you")
		print("see a small chest in the corner of the room. You hasten toward it.\n")
		
		input("Press Enter to continue...")
		print("")
		
		print("You open the chest to reveal 3 canisters with the following labels:")
		print("(1) Chromium (VI) Trioxide, anhydrous")
		print("(2) Sodium Metal in Mineral Oil")		
		print("(3) Phenolphthalein 1% in Ethanol")
		print("\nIn addition to the canisters, the chest contains a petri dish,")
		print("a test tube, and a pair of rubber gloves.")
		print("----------------------------------------------------------------------\n")
		
		##
		## Get user input for the two chemicals that will be mixed.
		print("Mix the chemical reagents to achieve rapid oxidation (identify each")
		print("by the number preceeding its label).")
		
		
		reagent1 = input("[1st reagent]> ")
		reagent2 = input("[2nd reagent]> ")
		reagents = sorted([int(reagent1), int(reagent2)])
		reaction1 = [1, 2]
		reaction2 = [2, 3]
		reaction3 = [1, 3]
		
		##
		## Test the user input and respond accordingly.
		if reagents == reaction1:
			print("----------------------------------------------------------------------")
			print("You shake a number of dark red Chromium trioxide flakes into the petri")
			print("dish. You then hastily remove a small chunk of sodium metal from the")
			print("mineral oil and add it to the dish of flakes, but no noticable reaction")
			print("occurs. The room remains dark and gloomy and Ron and Harry are")
			print("strangled by the pernicious plant. You have no hope of completing the")
			print("upcoming challenges without them. ")
			print("----------------------------------------------------------------------")
			
			print("")
			input("Press Enter to continue...")
			
			return 'DeathToFluffy'
			
		if reagents == reaction2:
			print("----------------------------------------------------------------------")
			print("You decant 1 millileter of phenolphthalein ethanol solution into the")
			print("test tube, and drop a small chunk of sodium metal into the solution.")
			print("The contents of the tube turn a deep purple, but no combustion occurs.")
			print("The room remains dark and gloomy and Ron and Harry are strangled by the")
			print("pernicious plant. You have no hope of completing the upcoming")
			print("following challenges without them. ")
			print("----------------------------------------------------------------------")
			
			print("")
			input("Press Enter to continue...")
			
			return 'DeathToFluffy'
			
		if reagents == reaction3:
			print("----------------------------------------------------------------------")
			print("You deposit a sizeable portion of dark red Chromium Trixide flakes")
			print("into the petri dish and pour the ethanol solution into the dish as you")
			print("slide it across the room toward the merderous Devil's Snare. As soon")
			print("as the ethanol makes contact with the highly unstable Chromium Trioxide,")
			print("it is oxidized rapidly resulting in violent combustion. The plant recoils,")
			print("and Harry and Ron fight free of its tendrils. You all rush through the")
			print("chamber door and slam it in the plant's face. ")
			print("----------------------------------------------------------------------")
			
			print("")
			input("Press Enter to continue...")
			
			return 'FlyingKeys'
			
		else:
			print("----------------------------------------------------------------------")
			print("You fumble with the rubber gloves and spill the contents of the ")
			print("canisters on the floor. The room remains dark and gloomy and Ron and ")
			print("Harry are strangled by thepernicious plant. You have no hope of ")
			print("completing the upcoming challenges without them. ")
			print("----------------------------------------------------------------------")
			
			print("")
			input("Press Enter to continue...")
			
			return 'DeathToFluffy'