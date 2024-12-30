from typing import List
import doctest

def initialize_board(n: int) -> List[List[str]]:
    """
    Initialize an n x n game board as a nested list, where each cell is initially filled with a space.

    Parameters:
         n (int): dimensions of n x n game board

    Returns:
        (List[List[str]]): game board with empty spaces, as nested list

    >>> initialize_board(3)
    [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    >>> initialize_board(4)
    [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    """

    # initializing outer list object (board) which will contain inner list objects (cells)
    starting_board = []

    # looping to create board rows
    for row in range(n):
        starting_board.append([])
        # looping to create board columns
        for col in range(n):
            starting_board[row].append(' ')

    return starting_board

def print_board(board: List[List[str]]) -> None:
    """
    Print the current state of the game board.

    Parameters:
        board (List[List[str]]): list of length n with n nested lists containing board contents, spaces and pieces

    >>> print_board([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
    -------------
    |   |   |   |
    -------------
    |   |   |   |
    -------------
    |   |   |   |
    -------------
    >>> print_board([[' ', 'X', ' '], [' ', ' ', ' '], [' ', ' ', 'O']])
    -------------
    |   | X |   |
    -------------
    |   |   |   |
    -------------
    |   |   | O |
    -------------
    """
    # ad hoc expression to print horizontal lines which separate board rows
    print('-' * (4 * len(board[0]) + 1))
    # loop to print left side of column delimiters
    for row in board:
        # need end argument, otherwise prints every delimiter on a separate line
        print('|', end='')
        # loop to print contents of cell (empty space or piece) and right column delimiter
        for cell in row:
            print(f" {cell} |", end="")
        # print horizontal row delimiter
        print('\n' + '-' * (4 * len(row) + 1))

    # function returns nothing, board printed whenever updated

def drop_piece(board: List[List[str]], row: int, col: int, player: str) -> bool:
    """
    On their turn, allows player to drop their piece into their chosen cell on the board, provided that the cell is not already occupied.

    Parameters:
        board (List[List[str]]): current board with all pieces placed from previous turns, if any
        row (int): row of board chosen by player to position piece
        col (int): column of board chosen by player to position piece
        player (str): current piece being placed on the board

    Returns:
        (bool): whether piece can be placed at desired position on board

    >>> drop_piece([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 1, 2, 'X')
    True
    >>> drop_piece([[' ', ' ', ' '], [' ', ' ', 'X'], [' ', ' ', ' ']], 1, 2, 'O')
    False
    >>> drop_piece([['X', 'X', 'O'], ['X', 'O', 'O'], [' ', 'X', ' ']], 0, 2, 'O')
    False
    >>> drop_piece([['X', 'X', ' '], ['X', 'O', 'O'], ['O', 'X', 'O']], 0, 2, 'X')
    True
    """
    # checking if cell chosen to place piece is empty
    if board[row][col] == ' ':
        # update cell with player piece
        board[row][col] = player
        return True

    return False

def is_winner(board: List[List[str]], player: str) -> bool:
    """
    Checks if a player has won the game by connecting a row, a column
    or a corner-to-corner diagonal.

    Parameters:
        board (List[List[str]]): current board with all pieces placed from previous turns, if any
        player (str): current piece being placed on the board

    Returns:
        (bool): whether a player has formed a winning connection on the board

    >>> is_winner([['O', 'O', ' '], [' ', ' ', ' '], ['X', 'X', 'X']], 'X')
    True
    >>> is_winner([[' ', 'O', 'X'], [' ', 'O', 'X'], [' ', ' ', 'X']], 'X')
    True
    >>> is_winner([['X', ' ', 'O'], [' ', 'X', 'O'], [' ', ' ', 'X']], 'X')
    True
    >>> is_winner([[' ', ' ', 'X'], [' ', 'X', 'O'], ['X', ' ', 'O']], 'X')
    True
    >>> is_winner([['O', 'X', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']], 'X')
    False
    """
    # checking for winning rows
    for row in board:
        # turning row into a set, to eliminate duplicated cell entries
        condensed_row = set(row)
        # winning row will have unique cell entry that is winning piece (i.e. no spaces or opposing pieces), where player is the winning piece
        if len(condensed_row) == 1 and condensed_row == {player}:
            return True

    # using index since cells in different list objects, each number represents a column
    for col in range(len(board)):
        # using range too in order to keep count of rows, to find final row
        for row in range(len(board)):
            if board[row][col] != player:
                # exit inner loop and move to next column, after checking if at last iteration
                break
            # reaching last row implies a winning column
            if row == len(board) - 1:
                return True

    # not using double loop since always same values for row and column, along diagonal
    for row_col in range(len(board)):
        # using double indices for loops, since on the diagonal, iterating from 0 to n, so top left of board to bottom right
        if board[row_col][row_col] != player:
            break
        if row_col == len(board) - 1:
            return True

    # using variable to update column value, since iterates in the opposite direction as row (reverse diagonal)
    col = len(board) - 1
    for row in range(len(board)):
        # row and column not synchronized like before, so need to adjust column value
        if board[row][col] != player:
            break
        # updating index for column before next loop
        col -= 1
        if row == len(board) - 1:
            return True

    return False

def is_board_full(board: List[List[str]]) -> bool:
    """
    Check if the game board is full, resulting in a tie game.

    Parameters:
        board (List[List[str]]): current board with all pieces placed from previous turns, if any

    Returns:
        (bool): whether game board is full of pieces, so no possible moves remaining

    >>> is_board_full([['O', 'O', ' '], [' ', ' ', ' '], ['X', 'X', 'X']])
    False
    >>> is_board_full([['O', 'X', 'X'], ['O', 'O', 'X'], ['O', 'X', 'X']])
    True
    """
    for row in board:
        # finding a single space implies an incomplete board
        if ' ' in row:
            return False

    return True

def play_tic_tac_toe() -> None:
    """ Orchestrate the game, allowing two players to take turns."""
    print("Welcome to Tic-Tac-Toe!")

    # Initialize the game board
    n = 0
    # getting answer from user until board size is at least 3
    while n < 3:
        try:
            n = int(input("What is the size of the board (minimum size is 3)? "))
        # if user input is not a digit, ValueError is raised, so this is the specific type of exception to catch (so program does not halt)
        except ValueError:
            continue

    # argument passed to this function is validated above, so no need to validate within function
    board = initialize_board(n)

    # Define players according to their piece, no choice to be made so no validation needed
    pieces = ['X', 'O']
    # track which player is moving, or moves next
    current_player = 0

    player_1_name = input("What is the name of player 1? ").strip()
    player_2_name = input("What is the name of player 2? ").strip()
    # default names given if user provides empty input
    if not player_1_name:
        player_1_name = '1'
    if not player_2_name:
        player_2_name = '2'

    # for user interface, when naming player for their turn
    player_names = [player_1_name, player_2_name]

    # condition for game to continue
    continue_game = True

    while continue_game:
        # showing board, but updated after every player move, no argument validation since validated in challenges functions
        print_board(board)

        # Get player input
        # As we are facing regular players, the row and col start 1 so that they don't get confused, below is string output to user
        row_col_examples = '/'.join([str(i + 1) for i in range(n)])
        # taking user input for chosen cell to place their piece, using empty strings to make disjunction true and trigger first loops
        row = ""
        col = ""
        '''
        continues asking user for input until receiving a number within the given range
        first disjunct checks that string contains only digits (not converted yet so as to not trigger value error)
        second disjunct checks that integer version of string, when converted, is within the given range
        '''
        while not row.isdigit() or (int(row) < 1 or int(row) > n):
            row = input(f"Player {player_names[current_player]}, choose a row ({row_col_examples}): ").strip()
        while not col.isdigit() or (int(col) < 1 or int(col) > n):
            col = input(f"Player {player_names[current_player]}, choose a column ({row_col_examples}): ").strip()

        # user inputs have been validated, now convert to integer objects to place in matrix, and add one to correct indices
        row = int(row) - 1
        col = int(col) - 1

        # Drop the player's piece into the chosen cell, but conditional since function returns boolean, whether chosen cell is occupied
        if drop_piece(board, row, col, pieces[current_player]):
            # Check for a winner
            if is_winner(board, pieces[current_player]):
                print_board(board)
                print(f"Player {player_names[current_player]} wins!")
                continue_game = False

            # Check for a tie
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                continue_game = False

            # Switch to the challenges player, since current_player value is either 0 or 1
            current_player = 1 - current_player

        # failed conditional above, so cell is occupied
        else:
            print("Cell is already occupied. Choose another cell.")


play_tic_tac_toe()

doctest.testmod()