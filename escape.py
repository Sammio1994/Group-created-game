import sys
from time import sleep
import random
import locale

class game_art:
    game_title = """
 _______     _______.  ______     ___      .______    _______
|   ____|   /       | /      |   /   \     |   _  \  |   ____|
|  |__     |   (----`|  ,----'  /  ^  \    |  |_)  | |  |__
|   __|     \   \    |  |      /  /_\  \   |   ___/  |   __|
|  |____.----)   |   |  `----./  _____  \  |  |      |  |____
|_______|_______/     \______/__/     \__\ | _|      |_______|
"""
    lion = """
       \|\||
       -' |||/
      /7   |||/
     /    |||||/
     \-' |||||||/`-.____________
      -|||||||||           /    `.
        |/||||             \      |
 _______/    /_       ______\      |__________-
(,__________/  `-.___(,_____________----------_)
"""
    knight = """
|\             //
 \\\\           _!_
  \\\\         /___\\
   \\\\        [+++]
    \\\\    _ _\^^^/_ _
     \\\\/ (    '-'  ( )
     /( \/ | {&}   /\ \\
       \  / \     / _> )
        "`   >:::;-'`""'-.
            /:::/         \\
           /  /||   {&}   |
          (  / (\         /
          / /   \\'-.___.-'
       _/ /     \ \\
       /___|    /___|
"""

    fire = """
            (  .      )
    )           (              )
            .  '   .   '  .  '  .
(    , )       (.   )  (   ',    )
    .' ) ( . )    ,  ( ,     )   ( .
). , ( .   (  ) ( , ')  .' (  ,    )
(_,) . ), ) _) _,')  (, ) '. )  ,. (' )
"""

    demon_beast = """
`;-.          ___,
  `.`\_...._/`.-"`
    \        /      ,
    /()   () \    .' `-._
   |)  .    ()\  /   _.'
   \  -'-     ,; '. <
    ;.__     ,;|   > \\
   / ,    / ,  |.-'.-'
  (_/    (_/ ,;|.<`
    \    ,     ;-`
     >   \    /
    (_,-'`> .'
         (_,'
"""
    totally_not_gandalf = """
                       ,---.
                       /    |
                      /     |
                     /      |
                    /       |
               ___,'        |
             <  -'          :
              `-.__..--'``-,_\_
                 |o/ ` :,.)_`>
                 :/ `     ||/)
                 (_.).__,-` |\\
                 /( `.``   `| :
                 \\'`-.)  `  ; ;
                 | `       /-<
                 |     `  /   `.
 ,-_-..____     /|  `    :__..-'\\
/,'-.__\\  ``-./ :`      ;       \\
`\ `\  `\\  \ :  (   `  /  ,   `. \\
  \` \   \\   |  | `   :  :     .\ \\
   \ `\_  ))  :  ;     |  |      ): :
  (`-.-'\ ||  |\ \   ` ;  ;       | |
   \-_   `;;._   ( `  /  /_       | |
    `-.-.// ,'`-._\__/_,'         ; |
       \:: :     /     `     ,   /  |
        || |    (        ,' /   /   |
        ||                ,'   /    |
"""
    congrats = """
   ___                            _         _       _   _                    _
  / __\___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___   / \\
 / /  / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __| /  /
/ /__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \/\_/
\____/\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/\/
                  |___/
"""
    bear = """
    .--.              .--.
   : (\ ". _......_ ." /) :
    '.    `        `    .'
     /'   _        _   `\\
    /     0}      {0     \\
   |       /      \       |
   |     /'        `\     |
    \   | .  .==.  . |   /
     '._ \.' \__/ './ _.'
     /  ``'._-''-_.'``  \\
"""

class text_formatting:
    purple = '\033[95m'
    yellow = '\033[1;33;40m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    orange = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    reset = '\033[0m'
# permissive responses for doors
doors = {
    "door_1": ["door one", "door 1", "one", "1"],
    "door_2": ["door two", "door 2", "two", "2"],
    "door_3": ["door three", "door 3", "three", "3"],
}
# Basic player data
player = {
    "name": "",
    "rps": {
        "wins": 0,
        "losses": 0,
        "draws": 0
    },
    "riddles": 0,
    "points": 0
}

def reset_player(replay=False):
    global player
    if replay == False:
        player["name"] = ""
    player["riddles"] = 0
    player["points"] = 0
    rps_reset()

def award_points(amnt = 10):
    global player
    player["points"] += amnt

def dock_points(amnt = 5):
    global player
    player["points"] -= amnt

def number_format(num, places=0):
    return locale.format_string("%.*f", (places, num), True)

def invalid_option_given():
    print(f"{text_formatting.red}That's not a valid option{text_formatting.reset}")

def rock_paper_scissors():
    global player

    # Return an "s" (or "es") if num != 1
    def pluralize(num, with_e=False):
        return "" if num == 1 else ("es" if with_e == True else "s")

    # Output the current scores
    def get_rps_score():
        # PHP's sprintf() -> Python equivalent, output scores as formatted
        return "%s%s%d win%s%s :: %s%d loss%s%s :: %s%d draw%s%s" % (
            text_formatting.green,
            text_formatting.bold,
            player["rps"]["wins"],
            pluralize(player["rps"]["wins"]),
            text_formatting.reset,
            text_formatting.red,
            player["rps"]["losses"],
            pluralize(player["rps"]["losses"], True),
            text_formatting.reset,
            text_formatting.cyan,
            player["rps"]["draws"],
            pluralize(player["rps"]["draws"]),
            text_formatting.reset,
        )

    # We support short-form guesses! So, relate them to what they represent
    def get_formatted_answer(guess):
        conv = {
            "r": "rock",
            "p": "paper",
            "s": "scissors",
        }
        # Return relative response if short-form, or the full guess if given
        return conv[guess] if guess not in ["rock", "paper", "scissors"] and guess in conv else guess

    def display_rps_round_outcome(guess, outcome, verb = ""):
        # Move args round if only 2 are given
        if verb == "":
            verb = outcome
            outcome = guess
        if verb == "win":
            color = text_formatting.green
        elif verb == "lose":
            color = text_formatting.red
        else:
            color = text_formatting.blue
        print(
            "You chose %s%s%s and your opponent has played %s%s%s · you %s%s%s this round.\n%s" % (
                text_formatting.blue,
                get_formatted_answer(guess),
                text_formatting.reset,
                text_formatting.orange,
                get_formatted_answer(outcome),
                text_formatting.reset,
                color,
                verb,
                text_formatting.reset,
                get_rps_score()
            )
        )

    # If the round was won
    def rps_win(guess, outcome):
        global player
        player["rps"]["wins"] += 1
        display_rps_round_outcome(guess, outcome, "win")
        award_points(5)

    # If the round was lost
    def rps_lose(guess, outcome):
        global player
        player["rps"]["losses"] += 1
        display_rps_round_outcome(guess, outcome, "lose")
        dock_points(5)

    # If the round was a draw
    def rps_draw(guess):
        global player
        player["rps"]["draws"] += 1
        display_rps_round_outcome(guess, "", "draw")
        award_points(1)

    def rock_paper_scissors_main(guess):
        opts = ["rock", "paper", "scissors"]
        if guess.lower().strip() not in (opt.lower() for opt in opts) and guess.lower().strip() not in ["r", "p", "s"]:
            # tell 'em!
            invalid_option_given()
        else:
            # Pick a random opt
            rand_opt = random.choice(opts)
            guess = guess.lower().strip()
            # GUESS: PAPER
            if guess in ["paper", "p"]:
                if rand_opt == "rock":
                    # paper beats rock
                    rps_win(guess, rand_opt)
                elif rand_opt == "scissors":
                    # scissors beats paper
                    rps_lose(guess, rand_opt)
                else:
                    # paper draws against paper
                    rps_draw(guess)
            # GUESS: ROCK
            elif guess in ["rock", "r"]:
                if rand_opt == "scissors":
                    # rock beats scissors
                    rps_win(guess, rand_opt)
                elif rand_opt == "paper":
                    # paper beats rock
                    rps_lose(guess, rand_opt)
                else:
                    # rock draws against rock
                    rps_draw(guess)
            # GUESS: SCISSORS
            elif guess in ["scissors", "s"]:
                if rand_opt == "paper":
                    # scissors beats paper
                    rps_win(guess, rand_opt)
                elif rand_opt == "rock":
                    # rock beats scissors
                    rps_lose(guess, rand_opt)
                else:
                    # scissors draws against scissors
                    rps_draw(guess)
            else:
                # Oi! Put somethin' right or don't bother!
                print(f"{text_formatting.red}You have not selected a valid option.{text_formatting.reset}")
    # If the player hasn't won or lost yet
    # Best of 3
    total = player["rps"]["wins"] + player["rps"]["losses"]
    # If the total (wins + losses) is less than 3, or if we have less than 2 wins; run
    while total < 3 and player["rps"]["wins"] < 2 and player["rps"]["losses"] < 2:
        # Take a guess!
        guess = input("Rock [r], Paper [p], or Scissors [s]?\n")
        # Call the game and pass the guess as an argument
        rock_paper_scissors_main(guess)
    return True if player["rps"]["wins"] >= 2 else False

# Reset the player metrics
def rps_reset():
    global player
    player["rps"]["wins"] = player["rps"]["losses"] = player["rps"]["draws"] = 0

def input_int(message):
  while True:
    try:
       user_input = int(input(message))
    except ValueError:
       print(f"{text_formatting.red}Not an integer! Try again.{text_formatting.reset}")
       continue
    else:
       return user_input

def do_maths_quiz():
    def display_menu():
        menu_list = [
            "1. Addition",
            "2. Subtraction",
            "3. Multiplication",
        ]
        for i in menu_list:
            print(i)


    def display_separator():
        print("-" * 24)


    def get_user_input():
        user_input = input_int("Enter your choice: ")
        if str(user_input).strip() == "":
            user_input = input_int("Enter your choice: ")
        while user_input > 3 or user_input <= 0:
            print("Invalid menu option.")
            user_input = input("Please try again: ")
        else:
            return user_input

    def get_user_solution(problem):
        print(f"Enter your answer\n{problem}")
        result = input_int(" = ")
        if str(result).strip() == "":
            get_user_solution(problem)
        return result


    def check_solution(user_solution, solution, count):
        if user_solution == solution:
            count += 1
            award_points(5)
            print("Correct.")
        else:
            print("Incorrect.")
        return count


    def menu_option(index, count):
        number_one = random.randrange(1, 21)
        number_two = random.randrange(1, 21)
        if index == 1:
            problem = str(number_one) + " + " + str(number_two)
            solution = number_one + number_two
            user_solution = get_user_solution(problem)
        elif index == 2:
            problem = str(number_one) + " - " + str(number_two)
            solution = number_one - number_two
            user_solution = get_user_solution(problem)
        else:
            problem = str(number_one) + " * " + str(number_two)
            solution = number_one * number_two
            user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count


    def display_result(total, correct):
        if total > 0:
            result = correct / total
            percentage = round((result * 100), 2)
        if total == 0:
            percentage = 0
        print(f"You answered {total} questions with {correct} correct. Your score is {percentage}%.")


    def maths_quiz():
        display_menu()
        display_separator()

        option = get_user_input()
        total = 0
        correct = 0
        while option <= 3 and correct < 3:
            total += 1
            correct = menu_option(option, correct)
            if correct >= 3:
                pass
            else:
                option = get_user_input()
        display_separator()
        display_result(total, correct)
        return True if correct >= 3 else False
    maths_quiz()


def typing_effect(words, time_delay = 0.005):
    for char in words:
        sleep(time_delay)
        sys.stdout.write(char)
        sys.stdout.flush()


def open_the_door(door_number):
    typing_effect(f"{text_formatting.red}{game_art.knight}{text_formatting.reset}")
    print(f"\nAfter you open door {door_number}, you see a dark knight. You've gotta play rock, paper, scissors.\n")
    rps_reset()
    outcome = rock_paper_scissors()
    if outcome == True:
        award_points()
        typing_effect("You have bested me!\n")
        quarter_final()
    elif outcome == False:
        print("You lost!\n")
        game_over()
    else:
        rock_paper_scissors()

def door_choice():
    global doors
    given = input("You use the door and enter a corridor. Looking around you see 3 more doors. Do you choose door number 1, 2 or 3?\n[door one] | [door two] | [door three]\n")
    given = given.lower()
    door = random.randint(1, 3)
    if door == 1:
        keys = ["door_2", "door_3"]
    elif door == 2:
        keys = ["door_1", "door_3"]
    else:
        keys = ["door_1", "door_2"]
    if given in doors["door_" + str(door)]:
        open_the_door(door)
    elif given in doors[keys[0]] or given in doors[keys[1]]:
        game_over()
    else:
        invalid_option_given()
        door_choice()


def game_over():
    global player
    dock_points()
    print(f"Game over. Bad luck, bub! Total score: {number_format(player['points'])}\n")
    run_credits()
    choice = input("\nWould you like to play again?\n")
    if choice.lower().strip() in ["yes", "y"]:
        main()
    else:
        print("See you next time")
        quit()


def run_credits():
    typing_effect(f"{text_formatting.cyan}{game_art.game_title}{text_formatting.reset}")
    typing_effect(f"\n\n{text_formatting.bold}Created by {text_formatting.red}Bear{text_formatting.reset}, {text_formatting.green}Davy{text_formatting.reset}, {text_formatting.blue}Katherine{text_formatting.reset}, {text_formatting.orange}Samm{text_formatting.reset} and {text_formatting.purple}Sean{text_formatting.reset}\n\n")


def introduction(name):
    action = "What do you choose to do?\n[walk toward the light] | [look around]\n"
    given = input(f"Welcome, {name}!\n\nYou wake up in an extremely dark and cold room. In the corner, you see a flickering light.\n{action}")
    given = given.lower().strip()
    if given in ["walk toward the light", "walk", "w"]:
        walk_toward_the_light()
    elif given in ["look around", "look", "around", "l"]:
        look_around()
    else:
        invalid_option_given()
        introduction(name)


def walk_toward_the_light():
    dock_points()
    print(f"You walk towards the light\nA laser hits you and you burst into flames.\n{text_formatting.orange}")
    typing_effect(game_art.fire)
    print(f"{text_formatting.reset}\n")
    game_over()


def look_around():
    print("You look around the room and find a torchlight.\n")
    door_or_vent()


def main(replay=False):
    reset_player(replay)
    print(text_formatting.reset)
    typing_effect(f"{text_formatting.cyan}{game_art.game_title}{text_formatting.reset}")
    choice = input("Do you want to play?\n[yes] | [no]\n")
    if choice.lower().strip() in ["y", "yes"]:
        print("Welcome to escape!")
        player_name()
    elif choice.lower().strip() in ["n", "no"]:
        confirm = input("Are you sure you want to leave Escape?\n")
        if confirm.lower() in ["y", "yes"]:
            print("Alright, see you later")
            run_credits()
        else:
            main()
    else:
        invalid_option_given()
        choice = input("Do you want to play?\n[yes] | [no]\n")
        main()


def player_name():
    global player
    if player["name"] == "":
        my_name = input("Please enter your name:\n")
        if my_name.strip() == "":
            invalid_option_given()
            my_name = input("Please enter your name:\n")
            player_name()
        name = my_name.lower()
        player["name"] = name
    else:
        name = player["name"]
    introduction(name.capitalize())


def door_or_vent():
    to_where = input("What do you do use? The rusty vent or gleaming shiny door?\n[Use vent] | [Use door]\n")
    if to_where.lower().strip() in ["door", "shiny door", "gleaming door", "gleaming shiny door", "use door", "use shiny door", "use gleaming door", "use gleaming shiny door"]:
        use_door()
    elif to_where.lower().strip() in ["vent", "use vent", "rusty", "use rusty", "use rusty vent"]:
        use_vent()
    else:
        print(f"{text_formatting.red}Invalid response{text_formatting.reset}")
        door_or_vent()

def do_open_the_door(door):
    award_points()
    open_the_door(door)
    print(
        f"After you open door {door}, you see a dark knight. You have to play rock. paper, scissors"
    )
    rps_reset()
    outcome = rock_paper_scissors()
    if outcome == True:
        typing_effect("You have bested me!\n")
        quarter_final()
    elif outcome == False:
        print("You lost!\n")
        game_over()
    else:
        rock_paper_scissors()

def use_door():
    global doors
    award_points(5)
    # Get the user's input
    choice = input("You use the door and enter a corridor. Looking around you see 3 more doors. Do you choose door number 1, 2 or 3?\n")
    # If the choice given is in the list
    door = random.randint(1, 3)
    if door == 1:
        keys = ["door_2", "door_3"]
    elif door == 2:
        keys = ["door_1", "door_3"]
    else:
        keys = ["door_1", "door_2"]
    if choice.lower().strip() in doors["door_" + str(door)]:
        do_open_the_door(door)
    elif choice in doors[keys[0]] or choice in doors[keys[1]]:
        game_over()
    else:
        invalid_option_given()
        use_door()


def use_vent():
    print(
        "You use the vent and end up in the first room with light, hence, you burst into flames\n"
    )
    typing_effect(f"{text_formatting.orange}{game_art.fire}{text_formatting.reset}")
    game_over()

def riddles():
    global player
    riddles = {
        0: {
            "question": "I go around in circles, but always straight ahead. I never complain no matter where I am led. What am I?",
            "answers": ["a wheel", "wheel", "wheels", "horse", "a mule", "mule", "donkey", "a donkey"]
        },
        1: {
            "question": "What has hands, but cannot clap?",
            "answers": ["a clock", "clock", "clocks", "the clock", "the clocks", "butt cheeks"]
        },
        2: {
            "question": "What has a head and a tail, but no body?",
            "answers": ["a coin", "coin", "coins"]
        },
        3: {
            "question": "What has many keys, but can't open a single lock?",
            "answers": ["a piano", "piano", "a keyboard", "keyboard"]
        },
        4: {
            "question": "What can you break, even if you never pick it up or touch it?",
            "answers": ["a promise", "promise", "a heart", "heart", "your heart", "trust", "sanity", "word", "your word"]
        },
        5: {
            "question": "What goes up, but never comes down?",
            "answers": ["your age", "age"]
        }
    }
    index = 0
    while player["riddles"] < 3:
        riddle = riddles.get(index)
        typing_effect(riddle["question"])
        response = input("\nResponse:\n")
        if response.lower().strip() in riddle["answers"]:
            player["riddles"] += 1
            award_points()
            typing_effect("Very good. The next riddle is..\n")
        else:
            dock_points()
            typing_effect("Incorrect!\n")
        index += 1
        if index > 5:
            break
    return True if player["riddles"] >= 3 else False


def semi_final():
    choice = input("You meet the dark knight. He says \"Hahaha! Do you really think you can take me?\"\n[yes] | [no]\n")
    if choice in ["yes", "y"]:
        rps_reset()
        outcome = rock_paper_scissors()
        if outcome == True:
            award_points()
            typing_effect("You have bested me!\n")
            zombie_lion_prep()
        else:
            dock_points()
            print("You lost!\n")
            game_over()
    elif choice in ["no", "n"]:
        dock_points()
        print("The Dark Knight takes out his sward and with a splash the speed of light he hits you. You get send back to start the quarter-final again.");
        quarter_final()
    else:
        invalid_option_given()
        semi_final()


def quarter_final():
    print(f"You won! You take the knights sword and his armour\n\n")
    typing_effect(f"{text_formatting.red}{game_art.knight}{text_formatting.reset}\nYou have bested me!\n")
    choice = input("You leave the room. Do you go left or right?\n")
    if choice.lower() in ["left", "left turn"]:
        award_points()
        print("Congratulations! You have entered another tournament!\n")
        outcome = do_maths_quiz()
        if outcome == True:
            semi_final()
        else:
            quarter_final()
    elif choice.lower() in ["right", "right turn", "turn right"]:
        dock_points()
        typing_effect(game_art.demon_beast)
        print("\nYou went right. You faced a demon beast! You lost.")
        game_over()
    else:
        invalid_option_given()
        quarter_final()


def zombie_lion_prep():
    choice = input("What way do you walk?\n[left] | [right]\n")
    if choice.lower() in ["l", "left", "r", "right"]:
        zombie_lion_encounter()
    else:
        invalid_option_given()
        zombie_lion_prep()

def zombie_lion_encounter():
    typing_effect(f"{text_formatting.yellow}{game_art.lion}{text_formatting.reset}")
    print("You encounter a sleeping zombie lion. It notices your arrival, but remains still. Without moving, the lion tells you:\n")
    typing_effect("You must correctly answer 3 riddles and I will allow you to pass. If not, then you're supper!\n\n")
    outcome = riddles()
    if outcome == True:
        game_won()
    else:
        game_over()

def game_won():
    global player
    award_points(100)
    print("After defeating the zombie lion, you wake up in a cold wet with a envelope next to you. You open the envelope and it reads: ")
    typing_effect("You have earned your freedom this time but next time;\n\n");
    typing_effect(f"{text_formatting.orange} YOU SHALL NOT PASS!{text_formatting.reset}", 0.2)
    typing_effect(game_art.totally_not_gandalf)
    typing_effect(game_art.congrats)
    print(f"\n{text_formatting.green}You have successfully completed all the levels of \"Escape\". Well done!{text_formatting.reset}\n")
    print(f"{text_formatting.yellow}Your total score: {number_format(player['points'])}{text_formatting.reset}")
    run_credits()
    restart = input("Would you like to play again?\n")
    if restart.lower().strip() in ["y", "yes"]:
        main(True)
    else:
        print(f"{text_formatting.blue}See you next time{text_formatting.reset}")
        quit()

main()


