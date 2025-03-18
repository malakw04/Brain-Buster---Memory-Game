# Brain-Buster -- Memory Game
## Overview
Brain Buster is a simple memory-matching game implemented in Python. The game generates a grid with hidden pairs of numbers, and the player must uncover matching pairs by selecting grid cells. The goal is to find all pairs in the fewest possible moves.

## Features
- Supports grid sizes of **2x2**, **4x4**, and **6x6**.
- Randomly generates a grid with pairs of numbers.
- Interactive game menu with multiple options:
  - Select two elements to uncover.
  - Reveal one random element.
  - Reveal the entire grid.
  - Start a new game.
  - Exit the game.
- Score tracking based on efficiency.

## File Structure
```
├── game.py      # Main game logic and user interaction
├── grid.py      # Grid class that handles grid generation and display
```

## Installation and Requirements
### Prerequisites
- Python 3.x installed on your system

### Clone the Repository
```bash
git clone https://github.com/yourusername/brain-buster.git
cd brain-buster
```

## How to Run
Run the game with a chosen grid size:
```bash
python3 game.py <grid_size>
```
Where `<grid_size>` must be `2`, `4`, or `6`.

Example:
```bash
python3 game.py 4
```

## How to Play
1. **Start the game**: The grid is initialized with hidden numbers.
2. **Select cells**: Choose two cells to reveal.
3. **Match pairs**: If the numbers match, they remain visible.
4. **Use menu options**:
   - `1` - Select two elements.
   - `2` - Reveal one random element.
   - `3` - Reveal the entire grid.
   - `4` - Start a new game.
   - `5` - Exit the game.
5. **Win the game**: Find all pairs in the fewest moves.

## Scoring
- If all pairs are found using valid moves, the score is calculated as:
  ```
  Score = min(100, (optimal_moves / actual_moves) * 100)
  ```
- If the player cheats by revealing the grid, the score is set to `0`.

## Example Grid Display
```
----------------------
|    Brain Buster    |
----------------------
    [A]  [B]  [C]  [D]  

[0]  X    X    X    X  
[1]  X    X    X    X  
[2]  X    X    X    X  
[3]  X    X    X    X  
```

## Contributions
Feel free to fork the repository and submit pull requests with improvements!




