# Python-project-1
This is the my first python build.
This is an game similar to Rock paper sizer, 

Snake 🐍 drinks water → Snake beats Water

Water 💧 damages the gun → Water beats Gun

Gun 🔫 kills the snake → Gun beats Snake

This is a simple Python implementation of the Snake, Water, Gun game where the user plays against the computer. 
The computer randomly chooses its move using Python’s random module, represented by numbers: 1 for snake, -1 for water, and 0 for gun. 
The user inputs their move as s (snake), w (water), or g (gun), which is converted to the corresponding number using a dictionary. 
Both choices are printed in readable form using another dictionary that maps numbers back to names. 
The game then compares the moves: if both choose the same, it’s a draw; otherwise, the rules are applied snake beats water, water beats gun, and gun beats snake to determine if the user wins or loses. 
The code demonstrates basic Python concepts like dictionaries, user input, conditional statements, and randomness in an interactive way.
