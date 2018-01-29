class Mastermind(object):

	##
	## Method to check if the guess is equal to the code
	def check(self, code, guess):		
		
		clicks = 0
		whistles = 0
		
		##
		## loop to determine number of clicks
		for x in xrange(4):
			if guess[x] == code[x]:
				guess[x] = 'click_guess'
				code[x] = 'click_code'
				clicks += 1
				
		##
		## loop to determine number of whistles
		for x in xrange(4):
			if guess[x] in code:
				position = code.index(guess[x])
				code[position] = 'whistle_code' 
				whistles += 1
				
		return [clicks, whistles]