#	Gabriel Summers ghs9@uw.edu
#	3/7/17
#	TCSS435
#	Assignment 2
#	pentago.py


#	node class that will be used as states
class node:
	def __init__(self):
		# self.children = []
		self.val = 0
		self.heur = 0

#################################################################
################## 		GLOBAL VARIABLES 	#####################
#################################################################


A0 = [[node(),node(),node()],
     [node(),node(),node()],
     [node(),node(),node()]]
A1 = [[node(),node(),node()],
     [node(),node(),node()],
     [node(),node(),node()]]
A2 = [[node(),node(),node()],
     [node(),node(),node()],
     [node(),node(),node()]]
A3 = [[node(),node(),node()],
     [node(),node(),node()],
     [node(),node(),node()]]
BOARD=[A0,A1,A2,A3]

PLAYER = 1;

GRIDS_TO_ROTATE = []

EXPANDED = 0

# All possible winning states on the board.
# Used to calculate heuristic as well as check
# for a winner.
WINNING_STATES = [
	[BOARD[0][0][0],BOARD[0][0][1],BOARD[0][0][2],BOARD[1][0][0],BOARD[1][0][1]],
	[BOARD[0][0][1],BOARD[0][0][2],BOARD[1][0][0],BOARD[1][0][1],BOARD[1][0][2]],
	[BOARD[0][1][0],BOARD[0][1][1],BOARD[0][1][2],BOARD[1][1][0],BOARD[1][1][1]],
	[BOARD[0][1][1],BOARD[0][1][2],BOARD[1][1][0],BOARD[1][1][1],BOARD[1][1][2]],
	[BOARD[0][2][0],BOARD[0][2][1],BOARD[0][2][2],BOARD[1][2][0],BOARD[1][2][1]],
	[BOARD[0][2][1],BOARD[0][2][2],BOARD[1][2][0],BOARD[1][2][1],BOARD[1][2][2]],

	[BOARD[2][0][0],BOARD[2][0][1],BOARD[2][0][2],BOARD[3][0][0],BOARD[3][0][1]],
	[BOARD[2][0][1],BOARD[2][0][2],BOARD[3][0][0],BOARD[3][0][1],BOARD[3][0][2]],
	[BOARD[2][1][0],BOARD[2][1][1],BOARD[2][1][2],BOARD[3][1][0],BOARD[3][1][1]],
	[BOARD[2][1][1],BOARD[2][1][2],BOARD[3][1][0],BOARD[3][1][1],BOARD[3][1][2]],
	[BOARD[2][2][0],BOARD[2][2][1],BOARD[2][2][2],BOARD[3][2][0],BOARD[3][2][1]],
	[BOARD[2][2][1],BOARD[2][2][2],BOARD[3][2][0],BOARD[3][2][1],BOARD[3][2][2]],

	[BOARD[0][0][0],BOARD[0][1][0],BOARD[0][2][0],BOARD[2][0][0],BOARD[2][1][0]],
	[BOARD[0][1][0],BOARD[0][2][0],BOARD[2][0][0],BOARD[2][1][0],BOARD[2][2][0]],
	[BOARD[0][0][1],BOARD[0][1][1],BOARD[0][2][1],BOARD[2][0][1],BOARD[2][1][1]],
	[BOARD[0][1][1],BOARD[0][2][1],BOARD[2][0][1],BOARD[2][1][1],BOARD[2][2][1]],
	[BOARD[0][0][2],BOARD[0][1][2],BOARD[0][2][2],BOARD[2][0][2],BOARD[2][1][2]],
	[BOARD[0][1][2],BOARD[0][2][2],BOARD[2][0][2],BOARD[2][1][2],BOARD[2][2][2]],

	[BOARD[1][0][0],BOARD[1][1][0],BOARD[1][2][0],BOARD[3][0][0],BOARD[3][1][0]],
	[BOARD[1][1][0],BOARD[1][2][0],BOARD[3][0][0],BOARD[3][1][0],BOARD[3][2][0]],
	[BOARD[1][0][1],BOARD[1][1][1],BOARD[1][2][1],BOARD[3][0][1],BOARD[3][1][1]],
	[BOARD[1][1][1],BOARD[1][2][1],BOARD[3][0][1],BOARD[3][1][1],BOARD[3][2][1]],
	[BOARD[1][0][2],BOARD[1][1][2],BOARD[1][2][2],BOARD[3][0][2],BOARD[3][1][2]],
	[BOARD[1][1][2],BOARD[1][2][2],BOARD[3][0][2],BOARD[3][1][2],BOARD[3][2][2]],

	[BOARD[0][1][0],BOARD[0][2][1],BOARD[2][0][2],BOARD[3][1][0],BOARD[3][2][1]],
	[BOARD[0][0][0],BOARD[0][1][1],BOARD[0][2][2],BOARD[3][0][0],BOARD[3][1][1]],
	[BOARD[0][1][1],BOARD[0][2][2],BOARD[3][0][0],BOARD[3][1][1],BOARD[3][2][2]],
	[BOARD[0][0][1],BOARD[0][1][2],BOARD[1][2][0],BOARD[3][0][1],BOARD[3][1][2]],

	[BOARD[2][1][0],BOARD[2][0][1],BOARD[0][2][2],BOARD[1][1][0],BOARD[1][0][1]],
	[BOARD[2][2][0],BOARD[2][1][1],BOARD[2][0][2],BOARD[1][2][0],BOARD[1][1][1]],
	[BOARD[2][1][1],BOARD[2][0][2],BOARD[1][2][0],BOARD[1][1][1],BOARD[1][0][2]],
	[BOARD[2][2][1],BOARD[2][1][2],BOARD[3][0][0],BOARD[1][2][1],BOARD[1][1][2]]
]

ME = 0
AI = 0

################################################################

################################################################
################## 			PRINTING 		####################
################################################################

# prints the actual part of the board that contains pieces.
def printBoardHelper(arr0, arr1):
	strn1 = ''
	strn2 = ''
	for row in arr0:
		for val in row:
			if val.val == 0:
				strn1+='{:2}'.format('.')
			elif val.val == 1:
				strn1+='{:2}'.format('W')
			elif val.val == 2:
				strn1+='{:2}'.format('B')
	for row in arr1:
		for val in row:
			if val.val == 0:
				strn2+='{:2}'.format('.')
			elif val.val == 1:
				strn2+='{:2}'.format('W')
			elif val.val == 2:
				strn2+='{:2}'.format('B')
	print '\t\t\t\t|', strn1[:5],'|',strn2[:5],'|'
	print '\t\t\t\t|', strn1[6:11],'|',strn2[6:11],'|'
	print '\t\t\t\t|', strn1[12:17],'|',strn2[12:17],'|'

# prints the general outline of the board
def printBoard(board):
	print '\n\n\t\t\t\t    Q1\t   Q2'
	print '\t\t\t\t+-------+-------+'
	printBoardHelper(board[0],board[1])
	print '\t\t\t\t+-------+-------+'
	printBoardHelper(board[2],board[3])
	print '\t\t\t\t+-------+-------+'
	print '\t\t\t\t    Q3\t   Q4'



################################################################

################################################################
################## 		MOVES AND ROTATIONS 	################
################################################################
def pickSpot(square, spot):
	global GRIDS_TO_ROTATE
	global LAST_NODE
	global BOARD
	global A0
	global A1
	global A2
	global A3
	completed = 0;
	while completed != 1:
		arr = BOARD[square-1]
		if arr[(spot-1)//3][(spot-1)%3].val != 0 and PLAYER != 0:
			square = input('\n\t\t\tSpot is already taken\n'
							'\t\t\tplease select a new one..\n'
							'\t\t\tSquare: ')
			spot = input('\t\t\ttile: ')
			continue
		if square-1 not in GRIDS_TO_ROTATE and spot - 1 != 5:
			if PLAYER != 0:
				GRIDS_TO_ROTATE.append(square-1)
		if square-1 in GRIDS_TO_ROTATE and spot-1 != 5 and PLAYER == 0:
			GRIDS_TO_ROTATE.remove(square-1)
		if PLAYER == ME:
			arr[(spot-1)//3][(spot-1)%3].val = ME
			completed = 1
		elif PLAYER == AI:
			arr[(spot-1)//3][(spot-1)%3].val = AI
			completed = 1
		else:
			arr[(spot-1)//3][(spot-1)%3].val = 0
			completed = 1

def rotateQuadrant(square, dire):
	global PLAYER
	global BOARD
	global A0
	global A1
	global A2
	global A3
	if(dire ==2):
		temp=[[node() for x in range(3)] for y in range(3)]
		for i in range(0,3):
			for j in range(0,3):
				temp[2-j][i].val = BOARD[square-1][i][j].val
		copyArray(BOARD[square-1],temp)
	else:
		temp=[[node() for x in range(3)] for y in range(3)]
		for i in range(0,3):
			for j in range(0,3):
				temp[j][2-i].val = BOARD[square-1][i][j].val
		copyArray(BOARD[square-1],temp)



################################################################

################################################################
################## 		ENDGAME HANDLERS 		################
################################################################

# Checks for a winner
def checkForWinner():
	# win = 1
	for possible in WINNING_STATES:
		win = 1
		color = possible[0].val
		for i in range(0,5):
			if possible[i].val != color or color == 0:
				win = 0
				break 
		if win == 1:
			return win
	return win

# exits the game. Completely unnecessary but sue me.
def flipThisShiz():
	exit()


################################################################

################################################################
################## 			AI STUFF 		####################
################################################################

# Calculates heuristic used by the AI.
# Looks at all groups of 5 positions that
# result in a win. If a player has a piece
# in one they get points as they could get
# a win from that piece, the more pieces in
# the row, the higher the heuristic. However
# if an enemy player also has a piece in the
# row, they will not get points as it cannot
# result in a win.
def calcHeur():
	j = 0
	heur = 0

	for possible in WINNING_STATES:
		color = possible[0].val
		for i in range(0,5):
			if color == 0:
				if possible[i].val != 0:
					color = possible[i].val
					j = 1
			elif color == ME:
				if possible[i].val == AI:
					j = 0
					break
				if possible[i].val == ME:
					j += 1
			else:
				if possible[i].val == ME:
					j = 0
					break
				if possible[i].val == AI:
					j += 1
		if color == ME:
			if j == 5:
				heur -= 10000
			elif j == 4:
				heur -= 1000
			else:
				heur -= j*j
		elif color == AI:
			if j == 5:
				heur += 10000
			elif j == 4:
				heur += 1000
			else:
				heur += j*j
		j = 0
		color = 0
	return heur

# Helper method, generally used by rotateQuadrant()
def copyArray(ar1,ar2):
	i=0
	j=0
	for row in ar2:
		for val in row:
			ar1[i][j].val=val.val
			j+=1
		i += 1
		j=0
	i=0
	j=0
	

# This method is how the AI picks its moves.
# Uses minimax with alpha-beta pruning, going
# to depth level 3.
#
# This is rediculously hardcoded by my standards
# but I am short on time. My apologies.
def findMoves(num, alpha, beta, first):
	global PLAYER
	global BOARD
	global A0
	global A1
	global A2
	global A3
	global EXPANDED
	EXPANDED += 1

	# This holds a list of steps (all possible moves)
	stepsFromHere=[]



	# fills the list with spots that havent been picked
	# Stored as a tuple(gridNum, rowNum, valNum) which
	# specifies what position the move is.
	rowNum=0
	valNum=0
	gridNum=0
	for grid in BOARD:
		for row in grid:
			for val in row:
				if val.val == 0:
					stepsFromHere.append((gridNum,rowNum,valNum))
				valNum += 1
			rowNum += 1
			valNum=0
		gridNum += 1
		rowNum=0
		valNum=0


	# This is what we do with each possible step.
	#used by recursion
	bestForAI1 = -999999
	bestForAI2 = 999999
	bestForAI3 = (-999999, stepsFromHere,1,1)

	# Base case, calculates heuristic
	if num == 1:
		PLAYER = AI
		for step in stepsFromHere:
			pickSpot(step[0] + 1, (step[1] * 3) + step[2] + 1)
			if len(GRIDS_TO_ROTATE) == 0:
				h = calcHeur()
				if h > bestForAI1:
					bestForAI1 = h
				if h > beta:
					PLAYER = 0
					pickSpot(step[0] + 1, (step[1] * 3) + step[2] + 1)
					PLAYER = ME
					return bestForAI1
			else:
				for gridToSpin in GRIDS_TO_ROTATE:
					for direToSpin in range(2):
						rotateQuadrant(gridToSpin+1,direToSpin+1)
						h = calcHeur()
						if direToSpin == 0:
							rotateQuadrant(gridToSpin+1,2)
						else:
							rotateQuadrant(gridToSpin+1,1)
						if h > bestForAI1:
							bestForAI1 = h
						if h > beta:
							PLAYER = 0
							pickSpot(step[0] + 1, (step[1] * 3) + step[2] + 1)
							PLAYER = ME
							return bestForAI1
			PLAYER = 0
			pickSpot(step[0] + 1, (step[1] * 3) + step[2] + 1)
			PLAYER = AI
		PLAYER = ME
		return bestForAI1
	if num == 2:
		PLAYER = ME
		for step in stepsFromHere:
			pickSpot(step[0] + 1, (step[1] * 3) + step[2] + 1)
			if len(GRIDS_TO_ROTATE) == 0:
				bestFrom1 = findMoves(1,alpha,beta,0)
				# h = calcHeur()
				# if h < bestForAI2:
				if type(bestFrom1) is int and bestFrom1 < bestForAI2:
					bestForAI2 = bestFrom1
					# bestForAI2 = h
					beta = bestFrom1
				# if bestForAI2 < alpha:
				if type(bestFrom1) is int and bestFrom1 < alpha:
					PLAYER = 0
					pickSpot(step[0] + 1, (step[1] * 3) + step[2] + 1)
					PLAYER = AI
					return bestForAI2
			else:
				for gridToSpin in GRIDS_TO_ROTATE:
					for direToSpin in range(2):
						rotateQuadrant(gridToSpin+1,direToSpin+1)
						bestFrom1 = findMoves(1,alpha,beta,0)
						# h = calcHeur()
						if direToSpin == 0:
							rotateQuadrant(gridToSpin+1,2)
						else:
							rotateQuadrant(gridToSpin+1,1)
						# if h < bestForAI2:
						if type(bestFrom1) is int and bestFrom1 < bestForAI2:
							bestForAI2 = bestFrom1
							# bestForAI2 = h
							beta = bestFrom1
						# if bestForAI2 < alpha:
						if type(bestFrom1) is int and bestFrom1 < alpha:
							PLAYER = 0
							pickSpot(step[0] + 1, (step[1] * 3) + step[2] + 1)
							PLAYER = AI
							return bestForAI2
			PLAYER = 0
			pickSpot(step[0] + 1, (step[1] * 3) + step[2] + 1)
			PLAYER = ME
		PLAYER = AI
		return bestForAI2
	if num == 3:
		PLAYER = AI
		trap = calcHeur()
		#Panic move if the user has 4 in a row
		if trap < -500 and first == 1:
			for step in stepsFromHere:
				pickSpot(step[0] + 1, (step[1] * 3) + step[2] + 1)
				if abs(trap) - abs(calcHeur()) > 500:
					for gridToSpin in GRIDS_TO_ROTATE:
						for direToSpin in range(2):
							rotateQuadrant(gridToSpin+1,direToSpin+1)
							h = calcHeur()
							if abs(trap) - abs(calcHeur()) > 500:
								print '\n\t\t\tNice! You had 4 in a row, so we\n'\
									   '\t\t\thave done this to try and block you.\n\n'
								printBoard(BOARD)
								return
							if direToSpin == 0:
								rotateQuadrant(gridToSpin+1,2)
							else:
								rotateQuadrant(gridToSpin+1,1)
				PLAYER = 0
				pickSpot(step[0] + 1, (step[1] * 3) + step[2] + 1)
				PLAYER = AI
			findMoves(3,alpha,beta,0)
		else:
			for step in stepsFromHere:
				pickSpot(step[0] + 1, (step[1] * 3) + step[2] + 1)
				if len(GRIDS_TO_ROTATE) == 0:
					bestFrom2 = findMoves(2,alpha,beta,0)
					if type(bestFrom2) is int and bestFrom2 > bestForAI3[0]:
						bestForAI3 = (bestFrom2,step,1,1)
						alpha = bestFrom2
				else:
					for gridToSpin in GRIDS_TO_ROTATE:
						for direToSpin in range(2):
							rotateQuadrant(gridToSpin+1,direToSpin+1)
							bestFrom2 = findMoves(2,alpha,beta,0)
							if direToSpin == 0:
								rotateQuadrant(gridToSpin+1,2)
							else:
								rotateQuadrant(gridToSpin+1,1)
							if type(bestFrom2) is int and bestFrom2 > bestForAI3[0]:
								bestForAI3 = (bestFrom2,step,gridToSpin+1,direToSpin+1)
								alpha = bestFrom2
				PLAYER = 0
				pickSpot(step[0] + 1, (step[1] * 3) + step[2] + 1)
				PLAYER = AI
	pickSpot(bestForAI3[1][0]+1,((bestForAI3[1][1]*3)+bestForAI3[1][2]+1))
	print '\n\t\t\tThis is the spot player ',str(PLAYER),' has chosen!\n'
	printBoard(BOARD)
	if checkForWinner() == 1:
		print '\n\n\t\t\tPlayer ',str(PLAYER),' you have won!\n'
		flipThisShiz()
	rotateQuadrant(bestForAI3[2],bestForAI3[3])
	print '\n\t\t\tAnd this is the the rotation they\n'\
		   '\t\t\thave chosen to make!\n'
	printBoard(BOARD) 
	# print '\n\n\t\t\tThis is how many nodes are expanded! ',EXPANDED,'\n'
	if checkForWinner() == 1:
		print '\n\n\t\t\tPlayer ',str(PLAYER),' you have won!\n'
		flipThisShiz()

def aiGOGOGO():
	findMoves(3,9999999,-9999999, 1)



	################################################################

	################################################################
	################## 		MAIN GAME HANDLERS		################
	################################################################


# Switches between human and AI player.
def gameTime():
	global LAST_POSI
	global LAST_QUAD
	global PLAYER
	if PLAYER == ME:
		strn = ''.join(['\n\n\t\t\tPlayer ',str(PLAYER),\
						', please pick a quadrant: '])
		completed = 0
		while completed != 1:
			try:
				quadrant = 0
				quadrant = int(raw_input(strn))
			except:
				print '\n\n\t\t\tThat is not even a number.'
			if type(quadrant) is not int or (quadrant <= 0 or quadrant > 4):
				print '\n\t\t\tThat is not a valid choice.\n'\
					  '\t\t\tPlease pick again.\n\n'
			else:
				completed = 1
		completed = 0
		while completed != 1:
			try:
				position = 0
				position = int(raw_input('\t\t\tNow pick a position, 1-9: '))
			except:
				print '\n\n\t\t\tThat is not even a number.'
			if type(position) is not int or (position <= 0 or position > 9):
				print '\n\t\t\tThat is not a valid choice.\n'\
					  '\t\t\tPlease pick again.\n\n'
			else:
				completed = 1
		pickSpot(quadrant, position)
		printBoard(BOARD)
		LAST_QUAD=quadrant
		LAST_POSI=position
		if checkForWinner() == 1:
			print '\n\n\t\t\tPlayer ',str(PLAYER),' you have won!\n'
			flipThisShiz()
		completed = 0
		while completed != 1:
			try:
				quadrant = 0
				quadrant = int(raw_input('\n\t\t\tSame player, '\
										 'Now pick a quadrant to rotate: '))
			except:
				print '\n\n\t\t\tThat is not even a number.'
			if type(quadrant) is not int or (quadrant <= 0 or quadrant > 4):
				print '\n\t\t\tThat is not a valid choice.\n'\
					  '\t\t\tPlease pick again.\n\n'
			else:
				completed = 1
		completed = 0
		while completed != 1:
			try:
				direction = 0
				direction = str(raw_input('\t\t\tAnd a direction, R for clockwise'\
				           		   '\n\t\t\tL for counter-clockwise: '))
			except:
				print '\n\n\t\t\tThat is not even a letter.'
			if type(direction) is not str or\
			       (direction.lower() != 'l' and direction.lower() != 'r'):
				print '\n\t\t\tThat is not a valid choice.\n'\
					  '\t\t\tPlease pick again.\n\n'
			else:
				completed = 1
		direToInt = 1
		if direction.lower() == 'l':
			direToInt = 2
		rotateQuadrant(quadrant, direToInt)
		printBoard(BOARD)
		if checkForWinner() == 1:
			print '\n\n\t\t\tPlayer ',str(PLAYER),' you have won!\n'
			flipThisShiz()
	else:
		aiGOGOGO()
	if PLAYER == ME:
		PLAYER = AI
	else:
		PLAYER = ME

# Introduces player and starts game
def welcome():
	global ME
	global AI
	print '\n\n\t\tWelcome to PENTAGO!\n\n'\
		  '\t\tThe rules are as follows:\n'\
		  '\t\t\t1: the board looks as follows:'
	printBoard(BOARD)
	print '\n\t\t\t2: The goal is to connect 5 of your\n'\
		  '\t\t\t    pieces in a row.\n\n'\
		  '\t\t\t3: Each player will take turns placing\n'\
		  '\t\t\t    a piece and then rotating a quadrant\n'\
		  '\t\t\t    of their choice in any direction by 90deg.\n\n'\
		  '\t\t\t4: To place a tile, you will first select\n'\
		  '\t\t\t    which quadrant you will place it in, the\n'\
		  '\t\t\t    choices are 1-4. Then you will select\n'\
		  '\t\t\t    which position to place it in. From\n'\
		  '\t\t\t    left to right, top to bottom in a quadrant,\n'\
		  '\t\t\t    the choices are 1-0\n\n'\
		  '\t\t\t5: To rotate a tile, you will be asked to\n'\
		  '\t\t\t    select which quadrant to rotate. Then\n'\
		  '\t\t\t    you will select L to rotate counter-clockwise\n'\
		  '\t\t\t    or R to rotate clockwise.\n\n'\
		  '\t\t\t5: Have fun!!\n\n'\
		  '\t\tNow, would you like to play as:\n\n'\
		  '\t\t\tPlayer 1\n'\
		  '\t\t\tPlayer 2\n'
	completed = 0
	while completed != 1:
		choice = 0
		try:
			choice = int(raw_input('\t\t\tSelect 1 for player 1,\n'\
						           '\t\t\t    or 2 for player 2: '))
		except:
			print '\n\n\t\t\tThat is not even a number.'
		if type(choice) is not int or (choice != 1 and choice != 2):
			print '\n\t\t\tThat is not a valid choice.\n'\
				  '\t\t\tPlease pick again.\n\n'
		else:
			completed = 1
			ME = choice
			if ME == 1:
				AI = 2
			else:
				AI = 1
	for i in range(50):
		print '\n'
	print '\t\t\t\tGAME BEGINS!\n\n'
	printBoard(BOARD)
	while 1:
		gameTime()

################################################################
# Begin
welcome()
