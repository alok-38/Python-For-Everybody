import random
import time
import os
import subprocess
 
def clear_screen():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
 
def show_instructions(game_type="rps"):
    if game_type == "rps":
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
    else:
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        print("Rock crushes Scissors")
 
game_map = {0: "rock", 1: "paper", 2: "scissors", 3: "lizard", 4: "Spock"}
rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]
rpsls_table = [[-1, 1, 0, 0, 4], [1, -1, 2, 3, 1],
               [0, 2, -1, 2, 4], [0, 3, 2, -1, 3],
               [4, 1, 4, 3, -1]]
 
def play_rps():
    while True:
        print("--- Rock-Paper-Scissors ---")
        inp = input("Enter move (rock/paper/scissors), 'help', or 'exit': ").lower().strip()
        if inp == "exit":
            break
        if inp == "help":
            show_instructions("rps")
            continue
        if inp == "rock":
            player_move = 0
        elif inp == "paper":
            player_move = 1
        elif inp == "scissors":
            player_move = 2
        else:
            print("Invalid move.")
            continue
 
        comp_move = random.randint(0, 2)
        print(f"Computer chooses: {game_map[comp_move].upper()}")
        result = rps_table[player_move][comp_move]
        if result == player_move:
            print("YOU WIN!")
        elif result == comp_move:
            print("COMPUTER WINS!")
        else:
            print("TIE GAME!")
        time.sleep(1)
        clear_screen()
 
def play_rpsls():
    while True:
        print("--- Rock-Paper-Scissors-Lizard-Spock ---")
        inp = input("Enter move, 'help', or 'exit': ").lower().strip()
        if inp == "exit":
            break
        if inp == "help":
            show_instructions("rpsls")
            continue
        move_map = {"rock": 0, "paper": 1, "scissors": 2, "lizard": 3, "spock": 4}
        if inp not in move_map:
            print("Invalid move.")
            continue
        player_move = move_map[inp]
        comp_move = random.randint(0, 4)
        print(f"Computer chooses: {game_map[comp_move].upper()}")
        result = rpsls_table[player_move][comp_move]
        if result == player_move:
            print("YOU WIN!")
        elif result == comp_move:
            print("COMPUTER WINS!")
        else:
            print("TIE GAME!")
        time.sleep(1)
        clear_screen()
 
def main_menu():
    while True:
        print("Which version?")
        print("1: Rock-Paper-Scissors")
        print("2: Rock-Paper-Scissors-Lizard-Spock")
        print("3: Quit")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Enter a number.")
            continue
        if choice == 1:
            play_rps()
        elif choice == 2:
            play_rpsls()
        elif choice == 3:
            print("Thanks for playing!")
            break
        else:
            print("Enter 1, 2, or 3.")
 
if __name__ == "__main__":
    main_menu()