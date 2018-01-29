##
## Import tools to be used in this class.
from random import randint
from copy import deepcopy
from .Mastermind import Mastermind

class FlyingKeys(object):

	def enter(self):
		
		##
		## Print the introductory narrative for Level 3
		print("\n")
		print("                    ******************************")
		print("                    ** LEVEL THREE: FLYING KEYS **")
		print("                    ******************************")
		print("----------------------------------------------------------------------")
		print("You enter a long cavernous room reminiscent of the great Gothic cathedrals")
		print("of Medieval Western Europe, whose high ceiling is supported by pillars")
		print("that run along the sides of the room. The pillars create shadowy recesses")
		print("along the walls, which your minds fill with three-headed dogs, gardens of ")
		print("Devil's snare, and other shapeless and nameless horrors. The voluminous")
		print("room is empty but for a broomstick hovering patiently in the middle of the")
		print("open floor and a cloud of colorful birds, which flit about in flashes black,")
		print("white, yellow, red, blue, and green up near the vaulted ceiling. You walk")
		print("past the broomstick to the opposite wall in which reposes an ornately carved")
		print("door. As you near the door you realize that the carvings depict muggles")
		print("in various positions that indicate intense neural recreation. The door is")
		print("sealed with a mysterious lock that contains 4 keyholes.\n")
		
		input("Press Enter to continue...")
		print("")
		
		print("You, Ron, have heard about this type of lock from your dad. It's called")
		print("a 'MindLock', and it takes its inspiration from a certain muggle ")
		print("board game, the name of which has escaped your memory. The lock will")
		print("open only when the 4 keyholes are filled with the correct pattern of")
		print("colored keys. After each attempt, it will emit a click for each correct")
		print("color in the correct position and a whistle for each correct color in")
		print("an incorrect position. You realize that what you all assumed to be birds")
		print("is actually a flock of winged keys. You estimate that Harry, the only one ")
		print("of your party with the sprecialized ability to snatch evasive winged ")
		print("objects out of the air while mounted on a flying broomstick, has enough ")
		print("stamina to collect 10 sets of 4 keys.")
		print("----------------------------------------------------------------------\n")
		
		input("Press Enter to continue...")
		print("")
		
		##
		## Prompt user to input the colors of the 4 keys to be collected.
		print("Enter the colors of the keys you wish Harry to collect. It appears there")
		print("are at least 4 keys of each color flying above.")
		
		colors = {
			1: 'black',
			2: 'white',
			3: 'yellow',
			4: 'red',
			5: 'blue',
			6: 'green'
		}
		
		##
		## Create the code.
		masterlock = Mastermind()
		code = [colors.get(randint(1,6)), colors.get(randint(1,6)), colors.get(randint(1,6)), colors.get(randint(1,6))]
		
		##
		## Get user input for the colors of the 4 keys to be collected.
		color1 = input("[1st color]>")
		color2 = input("[2nd color]>")
		color3 = input("[3rd color]>")
		color4 = input("[4th color]>")
		
		guess = [color1, color2, color3, color4]
		guesses = 1
		
		##
		## Bypass mindlock with cheat code
		if guess[0] == "newt-chage":
		
			return 'WizardsChess'
			
		##
		## Evaluate the user input and prompt further guesses.
		while guess != code and guesses < 10:
			guess_copy = deepcopy(guess)
			code_copy = deepcopy(code)
			feedback = masterlock.check(code_copy, guess_copy)	
			print("----------------------------------------------------------------------")
			print("The MindLock produces {} click{:s} and {} whistle{:s}.".format(feedback[0], "s"[feedback[0]==1:], feedback[1], "s"[feedback[1]==1:]))	
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			print("")
			
			print ("Try another pattern. You have {} guess{:s} remaining.".format(10-guesses, "s"[(10-guesses)==1:]))
			
			color1 = input("[1st color]>")
			color2 = input("[2nd color]>")
			color3 = input("[3rd color]>")
			color4 = input("[4th color]>")
			guess = [color1, color2, color3, color4]
			guesses += 1		
		
		##
		## Provide feedback for ultimate success or failure.
		if guess == code:
			print("----------------------------------------------------------------------")
			print("Click! Click! Click! Click! The lock surrenders to your powers of")
			print("deduction and the door swings open. You step through it with growing")
			print("trepidation.")
			print("----------------------------------------------------------------------")
			
			print("")
			input("Press Enter to continue...")
			print("")
			
			print("**********************************************************************")
			print("                          CONGRATULATIONS!\n")
			print("Each member of your party has taken the lead in solving a challenge. As")
			print("a result you have developed the skill:\n")
			print("                            'Teamwork'\n")
			print("This will allow you to restart at Level Four if you fail a challenge.")
			print("**********************************************************************\n")
			
			input("Press Enter to continue...")
			
			return 'WizardsChess'
			
		else:
			print("----------------------------------------------------------------------")
			print("As you ruthlessly command Harry to collect yet another selection of ")
			print("keys, he swoons with a high-pitched sigh of fatigue. By the time he")
			print("wakes up, it will be too late to save the stone. You are disapointed")
			print("about your failure to stop Snape from obtaining the stone, but you")
			print("you must admit a certain amount of satisfaction at seeing Harry's")
			print("unnatractive display of weakness. You hope Hermione was watching...")
			print("----------------------------------------------------------------------\n")
			
			input("Press Enter to continue...")
			
			return 'DeathToFluffy'