##
## Import all the scenes.
from scenes.Introduction import Introduction
from scenes.Fluffy import Fluffy
from scenes.DevilsSnare import DevilsSnare
from scenes.FlyingKeys import FlyingKeys
from scenes.WizardsChess import WizardsChess
from scenes.PotionsRiddle import PotionsRiddle
from scenes.MirrorOfErised import MirrorOfErised
from scenes.Voldemort import Voldemort
from scenes.Victory import Victory
from scenes.Death import DeathToFluffy
from scenes.Death import DeathToChess

class Engine(object):

	##
	## Map the name of each scene to an instance of it.
	scenes = { 
		'Introduction': Introduction(),
		'Fluffy': Fluffy(),
		'DevilsSnare': DevilsSnare(),
		'FlyingKeys': FlyingKeys(),
		'WizardsChess': WizardsChess(),
		'PotionsRiddle': PotionsRiddle(),
		'MirrorOfErised': MirrorOfErised(),
		'Voldemort': Voldemort(),
		'Victory': Victory(),
		'DeathToFluffy': DeathToFluffy(),
		'DeathToChess': DeathToChess()
	}
	
	##
	## This is the method that initializes the game.
	def play(self):
	
		self.nextScene('Introduction')
	
	##
	## This is the method that moves the player to the next scene.
	def nextScene(self, scene_name):
	
		if scene_name != 'end':
			next_scene = self.scenes.get(scene_name)
			self.nextScene(next_scene.enter())
	
	
