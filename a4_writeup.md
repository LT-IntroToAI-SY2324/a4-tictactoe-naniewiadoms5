# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?

I think the most difficult part of tic-tac-toe was writing was the has_won function. This is because I was originally thinking about programming all the 8 possible winning scenarios, but then I realized when working with larger programs with more versatility like Sudoku, I would be stuck on how to program it for all the acceptable moves, but now I recognize how the tic-tac-tow game was used with "2d arrays" or slices.

2. Explain how you would add a computer player to the game.

A computer player would have to work by making the best decision after differentiating all the possible ones. The computer would have to use an algorithm that can find the best decision using the information from the player (like its moves, trends in placement of the X or the O, etc), which makes the computer usually really difficult to beat (unless easy or medium game modes are selected, if any).

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.

Like I stated in the 2nd question, I think there would need to be an algorithm that calculates all the possible moves (and the predictions of the moves after based on the trends of the player's placement in Xs and Os). The algorithm would be maximizing the probability of the win rate.