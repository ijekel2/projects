class Voldemort(object):
	
	def enter(self):
	
		##
		## Print introductory narrative for level 7
		print("\n")
		print("                   *********************************")
		print("                   ** LEVEL SEVEN: VOLDEMORT FACE **")
		print("                   *********************************")
		print("----------------------------------------------------------------------")
		print("The sound of that voice chills your blood and you begin to back away")
		print("toward the exit; however, you cannot leave because fire continues to")
		print("block your path. You reach the steps as Quirrell begins to unwind his")
		print("turban. You are expecting to see him reveal a wizarding wireless, which ")
		print("is bewitched to proclaim intermittent phrases in a blood curdling voice.")
		print("But the truth is infinitely more dreadful. A hi'jyus face leers at you")
		print("from the gloom, its conspicious noselessness disconcerting you even more")
		print("than the fact that your teacher has a face on the back of his face.\n")
		print("\"Harrry Pottterr... the fool who lived! How pleasant it is for me to")
		print("gaze upon your insignificant complexion in these, your last moments!")
		print("Now why don't you give me that stone in your pocket.\"\n")
		print("For some reason you are unable to muster another stinging rebuke")
		print("to throw at Voldemort and content yourself with gulping wetly at him.")
		print("He chuckles evily in response.\n")
		print("\"As easy as stealing woodlice from a bowtruckle... Do you really think")
		print("you can resist ME? You utter fool; you know nothing of the world, and I")
		print("will prove it to you. If you answer this riddle, I will let you fight")
		print("Quirrell in hand to hand combat for the stone. If you should answer it")
		print("incorrectly, however... then Quirrell will destroy you from a distance")
		print("and take the stone from your lifeless body. Now on to the riddle...\"\n")
		
		input("Press Enter to continue...")
		print("")
		
		print("A bear walks south for one kilometer, then it walks west for one kilometer,")
		print("then it walks north for one kilometer and ends up at the same point from ")
		print("which it started. What color is the bear?")
		print("----------------------------------------------------------------------\n")
		
		##
		## Get user input for Voldemort's riddle'
		print("Answer Voldemort's riddle. If you get the answer correct perhaps you can")
		print("hold off Quirrell long enough for Hermione to bring help.")
		
		answer = input("[bear color]>")
		
		if answer.lower() == 'white':
			print("----------------------------------------------------------------------")
			print("You've answered correctly! Quirrel advances on you and, remembering your")
			print("self-defense classes, you grab his face. Inexplicably, his face begins to")
			print("burn at your touch. Amid raucous screams, you grab hold of him more firmly")
			print("and his face is reduced to ash. You see a dark shadow leaving his crumbling")
			print("body as you swoon with a high pitched cry of fatigue and horror.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")		
			
			return 'Victory'
			
		else:
			print("----------------------------------------------------------------------")
			print("\"Avada Kedavra!\"\n")
			print("You see a flash of green light and hear the rush of speeding death as")
			print("life is wiped humanely from your body. Quirrell retrieves the stone")
			print("from your corpse. Voldemort has won!")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")		
			
			return 'DeathToChess'
		