import subprocess

from stories import *

def story():
	active = True
	while active:
		print("Introduction")
		intro_input = raw_input("If you choose the forest, type in 'left' or 'l' or to continue alongside the sea, type 'right' or 'r': ")
		if intro_input == "left" or intro_input == "l":
			print("Forest option text")
			forest_input = raw_input("Type 'reveal' or 'r' to reveal the shadow or 'walk' or 'w' to continue walking: ")
			if forest_input == "r" or forest_input == "reveal":
				print("reveal-shadow")
				wizard_input == raw_input("Type 'r'/'run' to run from the wizard or 'f'/'face' to face it: ")
				if wizard_input == "face" or "f":
					print("Face wizard text")
					riddle_input = raw_input("Type your answer here ")
					if riddle_input == "steps" or ridde_input == "footsteps":
						print("correct-answer-conclusion")
						active = False
					elif riddle_input = "h" or riddle_input == "hint"
						print("hint-riddle ")
						riddle_input = raw_input("Type your answer here ")
						if riddle_input == "steps" or ridde_input == "footsteps":
							print("correct-answer-conclusion")
							active = False
					else:
						print("Wizard attack")
						active = False
			else: 
				print("Shadow attack and die")
				active = False
		elif intro_input == "right" or intro_input == "r":
			print("Sea option text")
			sea_input = raw_input("Type 'w' or 'water' to go into the water or 'l' or 'land' to get out: ")
			if sea_input == "l" or sea_input == "land":
				print("run to land")
				wizard_input == raw_input("Type 'r'/'run' to run from the wizard or 'f'/'face' to face it: ")
				if wizard_input == "face" or "f":
					print("Face wizard text")
					riddle_input = raw_input("Type your answer here ")
					if riddle_input == "steps" or ridde_input == "footsteps":
						print("correct-answer-conclusion")
						active = False
					elif riddle_input = "h" or riddle_input == "hint"
						print("hint-riddle ")
						riddle_input = raw_input("Type your answer here ")
						if riddle_input == "steps" or ridde_input == "footsteps":
							print("correct-answer-conclusion")
							active = False
					else:
						print("Wizard attack")
						active = False
			else:
				print("Water demon attack")
				active = False
		else:
			active = False


def main():
	story_content = {"intro": "intro.txt",
					"forest": "enter-forest.txt",
					"reveal-shadow": "reveal-shadow.txt",
					"ignore-shadow": "ignore-shadow.txt",
					"face-wizard": "face-wizard.txt",
					"run-wizard": "run-from-wizard.txt",
					"incorrect-riddle": "incorrect-riddle-answer.txt",
					"hint-riddle": "hint-riddle.txt",
					"stay-sea": "stay-sea.txt",
					"into-the-water": "into-the-water.txt",
					"run-to-land": "run-to-land.txt",
					"conclusion": "correct-answer-conclusion"}

	with open('stories/intro.txt', 'r') as f:
     	story_content['intro'] = f.read()

    with open('stories/forest.txt', 'r') as f:
    	story_content['forest'] = f.read()

    with open('stories/reveal-shadow.txt', 'r') as f:
    	story_content['reveal-shadow'] = f.read()

    with open('stories/ignore-shadow.txt', 'r') as f:
    	story_content['ignore-shadow'] = f.read()

    with open('stories/face-wizard.txt', 'r') as f:
    	story_content['face-wizard'] = f.read()

    with open('stories/run-from-wizard.txt', 'r') as f:
    	story_content['run-wizard'] = f.read()

    with open('stories/incorrect-riddle-answer.txt', 'r') as f:
    	story_content['incorrect-riddle'] = f.read()

    with open('stories/hint-riddle.txt', 'r') as f:
    	story_content['hint-riddle'] = f.read()

    with open('stories/stay-sea.txt', 'r') as f:
    	story_content['stay-sea'] = f.read()

    with open('stories/into-the-water.txt', 'r') as f:
    	story_content['into-the-water'] = f.read()

    with open('stories/run-to-land.txt', 'r') as f:
    	story_content['run-to-land'] = f.read()

    with open('stories/correct-answer-conclusion.txt', 'r') as f:
    	story_content['conclusion'] = f.read()

	story()

if __name__ == '__main__':
	main()