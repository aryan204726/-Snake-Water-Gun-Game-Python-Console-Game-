

# 🎮 Snake Water Gun Game (Python Console Game)

This is a simple Python implementation of the classic **"Snake, Water, Gun"** game — a fun variation of Rock, Paper, Scissors. The player competes against the computer in a console-based interactive game.

## 🐍 Game Rules

- 🐍 **Snake drinks Water** → Snake wins  
- 🔫 **Gun shoots Snake** → Gun wins  
- 💧 **Water damages Gun** → Water wins  
- If both choose the same → It's a **draw**

## 🚀 How to Play

1. Clone this repository or download the `.py` file.
2. Run the Python script:
   ```bash
   python snake_water_gun.py
When prompted, enter one of the following:

snake

gun

water

To exit the game, type:

nginx
Copy
Edit
quit

🧠 Game Logic
The computer makes a random choice.

The player inputs their choice.

A comparison is done using the check_win() function to determine the result.

The game continues in a loop until the user types quit.

💻 Sample Output
pgsql
Copy
Edit
Snake Water gun game
Type 'snake' , 'gun' , or 'water' to play game . Type 'quit' to stop game

your turn = snake
computer choice : water
you win

your turn = gun
computer choice : snake
you win

your turn = quit
Thanks for playing :
📁 File Structure
bash
Copy
Edit
main.py  # Main game script
README.md           # Project documentation



