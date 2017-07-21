import subprocess

def story():
    story_content = {}
    
    with open("stories/intro.txt", "r") as f:
        story_content["intro"] = f.read()

    with open("stories/enter-forest.txt", "r") as f:
        story_content["forest"] = f.read()

    with open("stories/reveal-shadow.txt", "r") as f:
        story_content["reveal-shadow"] = f.read()

    with open("stories/ignore-shadow.txt", "r") as f:
        story_content["ignore-shadow"] = f.read()

    with open("stories/face-wizard.txt", "r") as f:
        story_content["face-wizard"] = f.read()

    with open("stories/run-from-wizard.txt", "r") as f:
        story_content["run-wizard"] = f.read()

    with open("stories/incorrect-riddle-answer.txt", "r") as f:
        story_content["incorrect-riddle"] = f.read()

    with open("stories/hint-riddle.txt", "r") as f:
        story_content["hint-riddle"] = f.read()

    with open("stories/stay-sea.txt", "r") as f:
        story_content["stay-sea"] = f.read()

    with open("stories/into-the-water.txt", "r") as f:
        story_content["into-the-water"] = f.read()

    with open("stories/run-to-land.txt", "r") as f:
        story_content["run-to-land"] = f.read()

    with open("stories/correct-answer-conclusion.txt", "r") as f:
        story_content["conclusion"] = f.read()

    active = True
    print(story_content["intro"])
    while active:
        intro_input = raw_input("\nIf you choose the forest, type in 'left' or 'l' or to continue alongside the sea, type 'right' or 'r':\n\n")
        if intro_input == "left" or intro_input == "l":
            print(story_content["forest"])
            forest_input = raw_input("\nType 'reveal' or 'r' to reveal the shadow or 'walk' or 'w' to continue walking:\n\n")
            if forest_input == "r" or forest_input == "reveal":
                print(story_content["reveal-shadow"])
                wizard_input = raw_input("\nType 'r'/'run' to run from the wizard or 'f'/'face' to face it:\n\n")
                if wizard_input == "face" or "f":
                    print(story_content["face-wizard"])
                    riddle_input = raw_input("\nType your answer here:\n\n")
                    if riddle_input == "steps" or ridde_input == "footsteps":
                        print(story_content["conclusion"])
                        active = False
                    else:
                        print(story_content["incorrect-riddle"])
                        active = False
                else:
                    print(story_content["run-wizard"])
                    active = False
            else: 
                print(story_content["ignore-shadow"])
                active = False
        else:
            print(story_content["stay-sea"])
            sea_input = raw_input("\nType 'w' or 'water' to go into the water or 'l' or 'land' to get out:\n\n")
            if sea_input == "l" or sea_input == "land":
                print(story_content["run-to-land"])
                wizard_input = raw_input("\nType 'r'/'run' to run from the wizard or 'f'/'face' to face it:\n\n")
                if wizard_input == "face" or "f":
                    print(story_content["face-wizard"])
                    riddle_input = raw_input("\nType your answer here:\n\n")
                    if riddle_input == "steps" or ridde_input == "footsteps":
                        print(story_content["conclusion"])
                        active = False
                    else:
                        print(story_content["incorrect-riddle"])
                        active = False
                else:
                    print(story_content["run-wizard"])
                    active = False
            else:
                print(story_content["into-the-water"])
                active = False

def main():
    story()

if __name__ == '__main__':
    main()