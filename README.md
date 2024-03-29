# Chess Helper


## Table of  Contents
1.  [Description](#description)
2.  [Chess Helper in action](#shown)
3.  [Automatically finding the chessboard](#autoChessboard)
4.  [Find the last move](#move)
5.  [The best move](#bestmove)
6.  [Log section](#logs)


<div id="description">

## Description
This project is helping players to play chess by getting tips on the best possible move in current to do. The program automatically finds a chessboard on your screen, checks your side of the game (white or black), and saved all moves which were made. Every single time returns the best possible move when it is your turn.

<div id="shown">
 
 ## Chess Helper in action
 
Click the image to see Chess Helper in action!
<a href="https://www.youtube.com/watch?v=wctaPNbzSCk&ab_channel=KacperDominiak" title="Chess Helper"><img src="readme_image.png" width="xxx" height="yyy"></a>

<div id="autoChessboard">

##  Automatically finding the chessboard
The program finds chessboard by computer-vision method from OpenCV. It is resistant to change the size of the chessboard, because variables that are responsible for the game logic are automatically changing.

<div id="move">

## Find the last move

Every time when the move is made, the program finds it. This feature performs by looking for the difference between the previous screen image with the current screen image. For that, the program checks every single field.

<div id="bestmove">

## The best move

The program returns tips about the best possible move by using stockfish and previously found moves that were spotted. You can easily win will players around 2000 points. 

<div id="logs">

## Log section

The program generates every single time log file which will help you to spot your mistakes with running the program. Remember Chess Helper working only on not started games.
