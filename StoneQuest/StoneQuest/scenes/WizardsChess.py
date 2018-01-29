class WizardsChess(object):

	def enter(self):
		
		##
		## Print introductory narrative for Level 4.
		print("\n")
		print("                   ********************************")
		print("                   ** LEVEL FOUR: WIZARDS' CHESS **")
		print("                   ********************************")
		print("----------------------------------------------------------------------")
		print("You enter a chamber filled with statues standing side by side. You")
		print("begin to move between them and find yourselves standing on a lifesize,")
		print("torch-lit chessboard, the checkered pattern extending to the other end of")
		print("the chamber where eight marble-white stone infantry men stand in rank ")
		print("barring your path. In the gloom behind the array of white chessmen you")
		print("can just make out a large archway leading into the flame-lit chamber beyond.\n")
		
		input("Press Enter to continue...")
		print("")
		
		print("You, Ron, realize that the only way to advance beyond the line of ")
		print("white pawns is to lead the black pieces to victory in battle, and it")
		print("is clear that you, the most experienced chess player, must act as ")
		print("commander. However, before gamplay can commence, you must choose which")
		print("black pieces each of you will replace. You think it wisest to assign ")
		print("each member of your party to a chess piece whose attributes align with")
		print("their own personal charactaristics. To help you with the decision, you")
		print("mentally construct an insighful profile for each member of the group.\n")
		
		input("Press Enter to continue...")
		print("")
		
		print("RON BILLIUS WEASLEY, Chess Master and Eternal Quidditch Captain:")
		print("You have long felt that your athleticism is underrated. You are confident")
		print("enough in this assessment that you have been hatching plans to try out for ")
		print("the Gryffindor Quidditch team in the next 4 years or so. At any rate, you ")
		print("know for a fact that you can jump higher than either Harry or Hermione.")
		
		print("")
		input("Press Enter to continue...")
		print("")
		
		print("HERMIONE JEAN GRANGER, Exotic Beauty and Dazzling Intellect:")
		print("Hermione is the most steadfast of anyone in the group and she has been")
		print("a rock-solid friend through many emotional times. Partly because of")
		print("this, you have begun to develop a secret admiration for her. Perhaps you")
		print("should position her far away from yourself so that you can keep your mind")
		print("focused on the game.")
		
		print("")
		input("Press Enter to continue...")
		print("")
		
		print("HARRY 'WHO CARES' POTTER, Lazy quaffle pusher who is famous for basically no reason and always gets all the attention and who is totally always trying to one-up me in front of Hermione and win her affections:")
		print("One thing you have noted in your objective observations of Harry is that he")
		print("is rather pessimistic. It seems like he can only ever see one side of an")
		print("issue, and it is always the darker side. He has also been known to act")
		print("rashly, so perhaps you should keep him close by you during this game in case")
		print("gets up to something.")
		print("----------------------------------------------------------------------\n")
		print("Assign each group member a position on the board using Standard Algebraic")
		print("Notation (e.g. the postion where file c and rank 4 intersect is denoted")
		print("as c4.")
		
		##
		## Get user input for Ron's position.
		ron = input("[Ron's position]>")
		
		if ron == 'g8':
			print("----------------------------------------------------------------------")
			print("You take the place of the king's knight. You look unspeakably magestic")
			print("mounted on your stony steed. No doubt your flowing and fiery locks will")
			print("strike fear into the hearts of the opposing army. Brilliant tactics!")
			print("----------------------------------------------------------------------\n")
			
		elif ron =='b8':
			print("----------------------------------------------------------------------")
			print("You have positioned yourself too close to Hermione's ideal square, and ")
			print("her nearness distracts you in the opening stages of the game. You ")
			print("overdevelop your pawn structure seeking to impress her, and consequently ")
			print("you are unable to defend your large territory in the middlegame. White ")
			print("wins and all hope of stopping Snape is lost.")
			print("----------------------------------------------------------------------\n")
			
		elif "8" in ron:
			print("----------------------------------------------------------------------")
			print("You have positioned yourself such that your jumping abilities will not")
			print("be utilized. Poor tactics! Having observed this classic blunder, your")
			print("army loses respect for you and refuses to submit to your command. Thus")
			print("you are unable to defeat the white army and cannot advance past their")
			print("defences.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		elif "7" in ron:
			print("----------------------------------------------------------------------")
			print("You have positioned yourself such that you cannot see all of the black")
			print("chess pieces. You constantly have to turn around to instruct them,")
			print("which causes you to crick your neck and fall, disoriented, to the ground")
			print("where you wallow in self pity. Seeing this shameful display, your army")
			print("loses respect for you and refuses to submit to your command. Thus you")
			print("are unable to defeat the white army and cannot advance past their")
			print("defences.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		elif "2" in ron or "1" in ron:
			print("----------------------------------------------------------------------")
			print("You strut confidently into enemy territory unprotected and receive")
			print("a terrible blow that inexplicably causes you to lose consciousness")
			print("without inflicting any form of bodily injury. By the time you wake up")
			print("it will be too late to save the stone.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		else:
			print("----------------------------------------------------------------------")
			print("You have attempted to arrange the black army into an illegal formation.")
			print("As a result, your army loses respect for you and refuses to submit to")
			print("your command. Thus you are unable to defeat the white army and cannot")
			print("advance past their defences.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
		
		##
		## Get user input for Hermione's position.
		hermione = input("[Hermione's position]>")
		
		if hermione == 'a8':
			print("----------------------------------------------------------------------")
			print("Hermione takes the place of the queen's rook, and thus you will not be")
			print("able to see her very well from your place on the board. Wise leadership!")
			print("----------------------------------------------------------------------\n")
			
		elif "8" in hermione:
			print("----------------------------------------------------------------------")
			print("You have positioned Hermione too close to you and her nearness")
			print("distracts you in the opening stages of the game. You overdevelop your")
			print("pawn structure seeking to impress her, and consequently you are unable")
			print("to defend your large territory in the middlegame. White wins and all")
			print("hope of stopping Snape is lost.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		elif "7" in hermione:
			print("----------------------------------------------------------------------")
			print("Hermione resents being positioned as infantry, as she feels devalued.")
			print("She loses trust in you and openly defies your orders, conviced she")
			print("knows better than you. Your disagreements confuse the other pieces")
			print("who begin to move randomly. Black is quickly defeated and you lose all")
			print("hope of advancing to the next challenge.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		elif "2" in hermione or "1" in hermione:
			print("----------------------------------------------------------------------")
			print("You have sent Hermione into enemy territory unprotected and she receives")
			print("a terrible blow that inexplicably causes her to lose consciousness")
			print("without inflicting any form of bodily injury. By the time she wakes up")
			print("it will be too late to save the stone.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		else:
			print("----------------------------------------------------------------------")
			print("You have attempted to arrange the black army into an illegal formation.")
			print("As a result, your chess pieces lose respect for you and refuse to submit")
			print("to your command. Thus you are unable to defeat the white army and")
			print("cannot advance past their defences.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		##
		## Get user input for Harry's position.
		harry = input("[Harry's position]>")
		
		if harry == 'f8':
			print("----------------------------------------------------------------------")
			print("Harry takes the place of the king's bishop and thus is relagated to")
			print("black squares for the duration of the game. Well placed!")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			print("")
			
		elif "8" in harry or "7" in harry:
			print("----------------------------------------------------------------------")
			print("Harry has been given the freedom to move to white squares and so passes")
			print("the entire game in a state of constant apprehension. As a result he")
			print("misinterprets several of your instructions and codemns you to a tragic")
			print("loss that is both literally and figuratively crushing.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		elif "2" in harry or "1" in harry:
			print("----------------------------------------------------------------------")
			print("You have sent Harry into enemy territory unprotected and he receives")
			print("a terrible blow that inexplicably causes him to lose consciousness")
			print("without inflicting any form of bodily injury. By the time he wakes up")
			print("it will be too late to save the stone.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'
			
		else:
			print("----------------------------------------------------------------------")
			print("You have attempted to arrange the black army into an illegal formation.")
			print("As a result, your chess pieces lose respect for you and refuse to submit")
			print("to your command. Thus you are unable to defeat the white army and")
			print("cannot advance past their defences.")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToChess'

		##
		## Move to the next Challenge
		print("----------------------------------------------------------------------")
		print("Buoyed by over-confidence in your own abilities, you command the black")
		print("army to a reckless but decisive victory, achieving the winning position")
		print("with that gaudy brand of self-sacrifice that is a popular redemption")
		print("narrative for the courageous egoist. Having identified strong vital")
		print("signs, Harry and Hermione leave you supine on the field of victory and")
		print("advance unhindered past enemy lines and through the stone archway")
		print("beyond.")
		print("----------------------------------------------------------------------\n")
		
		input("Press Enter to continue...")
		
		return 'PotionsRiddle'