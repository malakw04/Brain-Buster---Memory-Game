import sys
import os
import time
import random
import string  

from grid import Grid


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    print("\n1. Let me select two elements")
    print("2. Uncover one element for me")
    print("3. I give up – reveal the grid")
    print("4. New game")
    print("5. Exit")
    print()


def get_valid_menu_option():
    while True:
        choice = input("Choose an option: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= 5:
            return int(choice)
        print("Invalid option. Choose a number between 1 and 5.")


def get_cell_input(size, used_cells=set()):
    while True:
        cell = input("Enter cell (e.g., A0, B2): ").strip().upper()
        if len(cell) >= 2 and cell[0] in string.ascii_uppercase and cell[1:].isdigit():
            col = ord(cell[0]) - 65  
            row = int(cell[1:])
            if 0 <= col < size and 0 <= row < size:
                if (row, col) not in used_cells:
                    return row, col
                print("You already selected that cell. Choose a different cell.")
            else:
                print(f"Invalid cell. Enter a letter (A-{chr(65 + size - 1)}) and a row number (0-{size - 1}).")
        else:
            print("Invalid format. Enter a cell like A0 or B2.")

def play_game(grid_size):
    grid = Grid(grid_size)
    guesses = 0
    used_guess_option = False  
    min_guesses = (grid_size * grid_size) // 2  

    while True:
        clear_screen()
        grid.display_grid()
        main_menu()
        choice = input("Select: ").strip()

        clear_screen()

        if choice == '1':
            used_guess_option = True  
            print("Select two elements:")
            first = get_cell_input(grid_size)
            second = get_cell_input(grid_size)
            if first and second and first != second:
                r1, c1 = first
                r2, c2 = second
                val1 = grid.reveal_cell(r1, c1)
                val2 = grid.reveal_cell(r2, c2)
                grid.display_grid()
                if val1 is not None and val2 is not None:
                    guesses += 1
                    if val1 != val2:
                        time.sleep(2)
                        grid.hide_cell(r1, c1)
                        grid.hide_cell(r2, c2)
                else:
                    print("Invalid cell selection.")
            else:
                print("Invalid input format or duplicate cells.")

        elif choice == '2':
            random_cell = random.choice(list(grid.pairs.keys() - grid.revealed_cells))
            grid.reveal_cell(*random_cell)
            grid.display_grid()
            guesses += 2  

        elif choice == '3':
            grid.reveal_grid()
            input("Press Enter to continue...")

        elif choice == '4':
            print("Starting a new game...")
            grid.reset_grid()
            guesses = 0
            used_guess_option = False 

        elif choice == '5':
            print("Thanks for playing!")
            break

        else:
            print("Invalid option. Choose again.")
            time.sleep(2)


        if grid.all_pairs_found():
            if used_guess_option:
                score = min(100, (min_guesses / guesses) * 100) if guesses else 0
                print(f"\nCongratulations! You found all pairs. Your score: {score:.1f}")
            else:
                print("\nYou cheated! Your score is 0.")
            break

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in {"2", "4", "6"}:
        print("Usage: python3 game.py <grid_size>")
        print("Grid size must be 2, 4, or 6.")
        sys.exit(1)

    grid_size = int(sys.argv[1])
    play_game(grid_size)
