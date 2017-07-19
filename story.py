def story():
	active = True
	while active:
		print("Introduction")
		intro_input = raw_input("If you choose the forest, type in 'left' or 'l' or to continue alongside the sea, type 'right' or 'r': ")
		if intro_input == "left" or intro_input == "l":
			print("Forest option text")
			forest_input = raw_input("Type 'reveal' or 'r' to reveal the shadow or 'walk' or 'w' to continue walking")
			if forest_input == "r" or forest_input == "reveal":
				print("Wizard option text")
				riddle_input = raw_input("What's the ridde?")
				if riddle_input == "honeybun":
					print("Fulfillment advice text")
					active = False
				else:
					print("Wizard attack and die")
					active = False
			else: 
				print("Shadow attack and die")
				active = False
		elif intro_input == "right" or intro_input == "r":
			print("Sea option text")
			sea_input = raw_input("Type 'w' or 'water' to go into the water or 'l' or 'land' to get out")
			if sea_input == "l" or sea_input == "land":
				print("Back to land text")
				riddle_input = raw_input("What's the riddle?")
				if riddle_input == "honeybun":
					print("Fulfillment advice text")
					active = False
				else:
					print("Wizard attack and die")
					active = False
			else:
				print("Water demon attack")
				active = False
		else:
			active = False


def main():
	story()


if __name__ == '__main__':
	main()