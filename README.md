# Pentago
Terminal based AI game
@author Gabriel Summers ghs9@uw.edu

The rules are as follows:
    1: the board looks as follows:


                Q1     Q2
            +-------+-------+
            | . . . | . . . |
            | . . . | . . . |
            | . . . | . . . |
            +-------+-------+
            | . . . | . . . |
            | . . . | . . . |
            | . . . | . . . |
            +-------+-------+
                Q3     Q4

    2: The goal is to connect 5 of your
        pieces in a row.

    3: Each player will take turns placing
        a piece and then rotating a quadrant
        of their choice in any direction by 90deg.

    4: To place a tile, you will first select
        which quadrant you will place it in, the
        choices are 1-4. Then you will select
        which position to place it in. From
        left to right, top to bottom in a quadrant,
        the choices are 1-0

    5: To rotate a tile, you will be asked to
        select which quadrant to rotate. Then
        you will select L to rotate counter-clockwise
        or R to rotate clockwise.

    5: Have fun!!

To run the program:

    1: Make sure you have python 2.7 installed

    2: From terminal, navigate to the directory that
        you have saved the file to.

    3: Enter the following command to start the game:
            'python pentago.py'

    4: The game should begin. Follow the prompts and
        have fun! 

A demonstration of the minimax algorithm with alpha-beta pruning.
Written in python 2.7
