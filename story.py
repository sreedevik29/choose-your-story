import os

story_sections = ['intro', 'enter-forest', 'reveal-shadow',
                  'ignore-shadow', 'face-wizard', 'run-from-wizard',
                  'incorrect-riddle-answer', 'hint-riddle', 'stay-sea',
                  'into-the-water', 'run-to-land',
                  'correct-answer-conclusion']
story_content = {}
hint = False
for section in story_sections:
    file_path = "stories/" + section + ".txt"
    with open(file_path) as file_reader:
        story_content[section] = file_reader.read()


def queue_start_story():
    queue_logic(section="intro",
                prompt_text=("\nIf you choose the forest, type in 'left' "
                             "or 'l' or to continue alongside the sea, type "
                             "'right' or 'r':\n\n"),
                options=("left", "l"),
                path_a=queue_enter_forest,
                path_b=queue_stay_sea)


def queue_enter_forest():
    queue_logic(section="enter-forest",
                prompt_text=("\nType 'reveal' or 'r' to reveal the shadow or "
                             "'walk' or 'w' to continue walking:\n\n"),
                options=("reveal", "r"),
                path_a=queue_reveal_shadow,
                path_b=queue_ignore_shadow)


def queue_stay_sea():
    queue_logic(section="stay-sea",
                prompt_text=("\nType 'w' or 'water' to go into the water "
                             "or 'l' or 'land' to get out:\n\n"),
                options=("land", "l"),
                path_a=queue_run_to_land,
                path_b=queue_into_the_water)


def queue_reveal_shadow():
    queue_logic(section="reveal-shadow",
                prompt_text=("\nType 'r' or 'run' to run from the wizard or "
                             "'f' or 'face' to face it:\n\n"),
                options=("face", "f"),
                path_a=queue_riddle,
                path_b=queue_run_from_wizard)


def queue_ignore_shadow():
    clear_screen()
    print(story_content['ignore-shadow'])


def queue_into_the_water():
    clear_screen()
    print(story_content['into-the-water'])


def queue_run_to_land():
    queue_logic(section="run-to-land",
                prompt_text=("\nType 'r' or 'run' to run from the wizard or "
                             "'f' or 'face' to face it:\n\n"),
                options=("face", "f"),
                path_a=queue_riddle,
                path_b=queue_run_from_wizard)


def queue_run_from_wizard():
    clear_screen()
    print(story_content['run-from-wizard'])


def queue_riddle():
    global hint
    if hint is False:
        clear_screen()
        print(story_content['face-wizard'])
        user_input = raw_input("\nType your answer here or type 'h' "
                               "for a hint:\n\n")
    else:
        user_input = raw_input("\nType your answer here:\n\n")
    if user_input.lower() in ("footsteps", "steps", "footstep", "step", "footprints", "footprint", "prints"):
        clear_screen()
        print(story_content['correct-answer-conclusion'])
    elif user_input.lower() in ("hint", "h"):
        if hint is False:
            clear_screen()
            print(story_content["hint-riddle"])
            hint = True
            queue_riddle()
        else:
            print("\nSorry, no more hints...\n\n")
            queue_riddle()
    else:
        clear_screen()
        print(story_content['incorrect-riddle-answer'])


def queue_logic(section, prompt_text, options, path_a, path_b):
    clear_screen()
    print(story_content[section])
    user_input = raw_input(prompt_text)
    if user_input.lower() in options:
        path_a()
    else:
        path_b()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    queue_start_story()


if __name__ == '__main__':
    main()
