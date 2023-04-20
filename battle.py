import argparse
import sys
import copy


class State:
    # This class is used to represent a battleground state.
    def __init__(self, board, row_constraints, column_constraints, num_ships):
        self.board = board
        self.row_constraints = row_constraints
        self.column_constraints = column_constraints
        self.num_ships = num_ships
        self.height = len(board)
        self.width = len(board)
        self.m_location = []

    def initialise(self):
        """
        using the hints given surrounding the given ship parts with water to narrow down the board.
        """
        for i in range(self.height):
            for j in range(self.width):
                piece = self.board[i][j]
                if piece == '.':
                    pass
                elif piece == '0':
                    pass
                else:
                    self.water_ship(i, j)

    def water_ship(self, loc_x, loc_y):
        """
        helper function to water the surroundings of the piece at given location.
        """
        i, j = loc_x, loc_y
        piece = self.board[i][j]
        if piece == 'S':
            self.board[i][j] = '1'
            # water left
            if j != 0:
                self.board[i][j - 1] = '.'

            # water right
            if j != self.height - 1:
                self.board[i][j + 1] = '.'

            # water up
            if i != 0:
                self.board[i - 1][j] = '.'

            # water up left
            if i != 0 and j != 0:
                self.board[i - 1][j - 1] = '.'

            # water up right
            if i != 0 and j != self.height - 1:
                self.board[i - 1][j + 1] = '.'

            # water down
            if i != self.height - 1:
                self.board[i + 1][j] = '.'

            # water down right
            if i != self.height - 1 and j != self.height - 1:
                self.board[i + 1][j + 1] = '.'

            # water down left
            if i != self.height - 1 and j != 0:
                self.board[i + 1][j - 1] = '.'


        elif piece == '<':
            self.board[i][j] = '1'
            self.board[i][j + 1] = '1'
            # water left
            if j != 0:
                self.board[i][j - 1] = '.'

            # water up
            if i != 0:
                self.board[i - 1][j] = '.'

            # water up left
            if i != 0 and j != 0:
                self.board[i - 1][j - 1] = '.'

            # water up right
            if i != 0 and j != self.height - 1:
                self.board[i - 1][j + 1] = '.'
            # water up double right
            if i != 0 and j != self.height - 1 and j + 1 != (self.height - 1):
                self.board[i - 1][j + 2] = '.'

            # water down
            if i != self.height - 1:
                self.board[i + 1][j] = '.'

            # water down right
            if i != self.height - 1 and j != self.height - 1:
                self.board[i + 1][j + 1] = '.'

            # water down left
            if i != self.height - 1 and j != 0:
                self.board[i + 1][j - 1] = '.'

            # water down right double
            if i != self.height - 1 and j != self.height - 1 and j + 1 != (self.height - 1):
                self.board[i + 1][j + 2] = '.'



        elif piece == '>':
            self.board[i][j] = '1'
            self.board[i][j - 1] = '1'
            # water right
            if j != self.height - 1:
                self.board[i][j + 1] = '.'

            # water up right
            if i != 0 and j != self.height - 1:
                self.board[i - 1][j + 1] = '.'

            # water down right
            if i != self.height - 1 and j != self.height - 1:
                self.board[i + 1][j + 1] = '.'


            # water up
            if i != 0:
                self.board[i - 1][j] = '.'

            # water down
            if i != self.height - 1:
                self.board[i + 1][j] = '.'

            # water up left
            if i != 0 and j != 0:
                self.board[i - 1][j - 1] = '.'

            # water up left double
            if j != 0 and j != 0 and j != 1:
                self.board[i - 1][j - 2] = '.'

            # water down left
            if i != self.height - 1 and j != 0:
                self.board[i + 1][j - 1] = '.'

            # water down left double
            if i != self.height - 1 and j != 0 and j != 1:
                self.board[i + 1][j - 2] = '.'


        elif piece == '^':
            self.board[i][j] = '1'
            self.board[i + 1][j] = '1'
            # water up
            if i != 0:
                self.board[i - 1][j] = '.'
            # water left
            if j != 0:
                self.board[i][j - 1] = '.'

            # water right
            if j != self.height - 1:
                self.board[i][j + 1] = '.'

            # water up left
            if i != 0 and j != 0:
                self.board[i - 1][j - 1] = '.'

            # water up right
            if i != 0 and j != self.height - 1:
                self.board[i - 1][j + 1] = '.'

            # water down right
            if i != self.height - 1 and j != self.height - 1:
                self.board[i + 1][j + 1] = '.'
            # water down left
            if i != self.height - 1 and j != 0:
                self.board[i + 1][j - 1] = '.'

            # water down right double
            if i != self.height - 1 and i + 1 != (self.height - 1) and j != self.height:
                self.board[i + 2][j + 1] = '.'

            # water down left double
            if i != self.height - 1 and i + 1 != (self.height - 1) and j != 0:
                self.board[i + 2][j - 1] = '.'


        elif piece == 'v':
            self.board[i][j] = '1'
            self.board[i - 1][j] = '1'
            # water left
            if j != 0:
                self.board[i][j - 1] = '.'

            # water right
            if j != self.height - 1:
                self.board[i][j + 1] = '.'

            # water up left
            if i != 0 and j != 0:
                self.board[i - 1][j - 1] = '.'

            # water up right
            if i != 0 and j != self.height - 1:
                self.board[i - 1][j + 1] = '.'
            # water up left double
            if i != 0 and i != 1 and j != 0:
                self.board[i - 2][j - 1] = '.'

            # water up right double
            if i != 0 and i != 1 and j != self.height - 1:
                self.board[i - 2][j + 1] = '.'

            # water down
            if i != self.height - 1:
                self.board[i + 1][j] = '.'

            # water down right
            if i != self.height - 1 and j != self.height - 1:
                self.board[i + 1][j + 1] = '.'

            # water down left
            if i != self.height - 1 and j != 0:
                self.board[i + 1][j - 1] = '.'

        elif piece == 'M' or piece == '1':
            # water up right

            if i != 0 and j != self.height - 1:
                self.board[i - 1][j + 1] = '.'

            # water up left
            if i != 0 and j != 0:
                self.board[i - 1][j - 1] = '.'

            # water down right
            if i != self.height - 1 and j != self.height - 1:
                self.board[i + 1][j + 1] = '.'

            # water down left
            if i != self.height - 1 and j != 0:
                self.board[i + 1][j - 1] = '.'

            if piece == 'M':
                self.m_location.append((i, j))


    def enforce_row_constraints(self):
        """
        helper function to enforce row constraints in forward checking to narrow down the board based on
        the row constraints
        """
        moved = None
        for i in range(self.height):
            space_occupied = 0
            space_empty = 0
            longest_ship = 0
            if self.row_constraints[i] == -1:
                continue
            for j in range(self.width):
                piece = self.board[i][j]
                if piece == "0":

                    space_empty += 1
                    longest_ship = 0
                elif piece == ".":
                    longest_ship = 0
                elif piece == "1" or piece == "M":
                    space_occupied += 1
                    longest_ship += 1
                    if longest_ship > 4:
                        return False

            if self.row_constraints[i] == space_occupied:
                self.row_constraints[i] = -1
                for j in range(self.width):
                    if self.board[i][j] == '0':
                        self.board[i][j] = '.'
                moved = True
            elif self.row_constraints[i] < space_occupied:
                return False
            elif self.row_constraints[i] == space_occupied + space_empty:
                self.row_constraints[i] = -1
                for j in range(self.width):
                    if self.board[i][j] == '0':
                        self.board[i][j] = '1'
                        self.water_ship(i, j)
                        moved = True
        return moved


    def enforce_col_constraints(self):
        """
        helper function to enforce row constraints in forward checking to narrow down the board based on
        the column constraints
        """
        moved = None
        for j in range(self.height):

            space_occupied = 0
            space_empty = 0
            longest_ship = 0
            if self.column_constraints[j] == -1:
                continue
            for i in range(self.width):
                piece = self.board[i][j]
                if piece == "0":
                    space_empty += 1
                    longest_ship = 0
                elif piece == ".":
                    longest_ship = 0
                elif piece == "1" or piece == "M":
                    space_occupied += 1
                    longest_ship += 1
                    if longest_ship > 4:
                        return False

            if self.column_constraints[j] == space_occupied:
                self.column_constraints[j] = -1
                for i in range(self.width):
                    if self.board[i][j] == '0':
                        self.board[i][j] = '.'
                moved = True
            elif self.column_constraints[j] < space_occupied:
                return False
            elif self.column_constraints[j] == space_occupied + space_empty:
                self.column_constraints[j] = -1
                for i in range(self.width):
                    if self.board[i][j] == '0':
                        self.board[i][j] = '1'
                        self.water_ship(i, j)
                        moved = True
        return moved


    def empty_positions(self):
        """
        helper function to find empty spots location on the board
        """
        pos = []
        for i in range(self.height):
            for j in range(self.width):
                if (self.board[i][j] == "0"):
                    pos.append((i, j))
        return pos

    def complete_m(self):
        """
        helper function needed when M's are given as hint and to make sure we use those location of M to build a ship
        surrounding it.
        """

        if len(self.m_location) == 0:
            return False
        for loc in self.m_location:
            i, j = loc
            # check if ship can be place up down
            # case when left or right is not possible hence we place the ship up and down of M
            if j == 0 or j == self.height - 1:
                if i != 0 and i != self.height - 1:
                    if (self.board[i + 1][j] == '0' or self.board[i + 1][j] == '1') and \
                            (self.board[i - 1][j] == '0' or self.board[i - 1][j] == '1'):
                        self.board[i + 1][j] = '1'
                        self.water_ship(i + 1, j)
                        self.board[i - 1][j] = '1'
                        self.water_ship(i - 1, j)
                        self.board[i][j] = '1'  # remove M
                        self.m_location.remove(loc)
                        return True

            # case when top and bottom is not possible so have to place ship left right
            if i == 0 or i == self.height - 1:
                if (self.board[i][j + 1] == '0' or self.board[i][j + 1] == '1') and \
                        (self.board[i][j - 1] == '0' or self.board[i][j - 1] == '1'):
                    self.board[i][j + 1] = '1'
                    self.water_ship(i, j + 1)
                    self.board[i][j - 1] = '1'
                    self.water_ship(i, j - 1)
                    self.board[i][j] = '1'  # remove M
                    self.m_location.remove(loc)
                    return True
            if i != 0 and i != self.height - 1:
                if self.board[i + 1][j] == '0' and self.board[i - 1][j] == '0':
                    if column_constraints[j] >= 3:
                        self.board[i + 1][j] = '1'
                        self.water_ship(i + 1, j)
                        self.board[i - 1][j] = '1'
                        self.water_ship(i - 1, j)
                        self.board[i][j] = '1'  # remove M
                        self.m_location.remove(loc)
                        return True
            # case when there already exists a ship piece on top of M hence we place one beneath it as well
            if j != 0 and j != self.height - 1:
                if (self.board[i][j + 1] == '0') and (self.board[i][j - 1] == '0'):
                    if row_constraints[i] >= 3:
                        self.board[i][j + 1] = '1'
                        self.water_ship(i, j + 1)
                        self.board[i][j - 1] = '1'
                        self.water_ship(i, j - 1)
                        self.board[i][j] = '1'  # remove M
                        self.m_location.remove(loc)
                        return True

            if self.board[i - 1][j] == "1" or self.board[i - 1][j] == "M":
                if self.board[i + 1][j] == '0':
                    self.board[i + 1][j] = '1'
                    self.water_ship(i + 1, j)
                    self.board[i][j] = '1'  # remove M
                    self.m_location.remove(loc)
                    return True
            # case when there already exists a ship piece bottom of M hence we place one on top of it as well
            elif self.board[i + 1][j] == "1" or self.board[i + 1][j] == "M":
                if self.board[i - 1][j] == '0':
                    self.board[i - 1][j] = '1'
                    self.water_ship(i - 1, j)
                    self.board[i][j] = '1'  # remove M
                    self.m_location.remove(loc)
                    return True
            # case when there already exists a ship piece left of M hence we place one on right of it as well
            if self.board[i][j-1] == "1" or self.board[i][j-1] == "M":
                if self.board[i][j+1] == '0':
                    self.board[i][j+1] = '1'
                    self.water_ship(i, j+1)
                    self.board[i][j] = '1'  # remove M
                    self.m_location.remove(loc)
                    return True
            # case when there already exists a ship piece right of M hence we place one on left of it as well
            elif self.board[i][j + 1] == "1" or self.board[i][j + 1] == "M":
                if self.board[i][j - 1] == '0':
                    self.board[i][j - 1] = '1'
                    self.water_ship(i, j - 1)
                    self.board[i][j] = '1'  # remove M
                    self.m_location.remove(loc)
                    return True

        return False


    def check_state(self):
        """
        main logic is that we go from top left first. so we only check sis ships is connected on the bottom or right.
        this function has two main functionalities.
        1. it checks if given board meets the number of ships given
        2. it keeps track of locations of the ship which we later use to convert our board to updated board with ships.
        """
        visited = [[False] * self.height for _ in range(self.height)]
        ships = [0, 0, 0, 0]
        one_one = []
        one_two = []
        one_three = []
        one_four = []
        for i in range(self.height):
            for j in range(self.width):
                if visited[i][j]:
                    continue
                if self.board[i][j] == '1':
                    # check down
                    if i != self.height - 1 and self.board[i + 1][j] == '1':
                        # this could be long ship
                        count, visited = self.count_down(i, j, visited)
                        if count == 1:
                            ships[0] += 1
                            one_one.append((i, j))
                        elif count == 2:
                            ships[1] += 1
                            one_two.append((i, j, 'down'))
                        elif count == 3:
                            ships[2] += 1
                            one_three.append((i, j, 'down'))
                        elif count == 4:
                            ships[3] += 1
                            one_four.append((i, j, 'down'))

                    # check right
                    elif j != self.height - 1 and self.board[i][j + 1] == '1':
                        count, visited = self.count_right(i, j, visited)
                        if count == 1:
                            ships[0] += 1
                            one_one.append((i, j))
                        elif count == 2:
                            ships[1] += 1
                            one_two.append((i, j, 'right'))
                        elif count == 3:
                            ships[2] += 1
                            one_three.append((i, j, 'right'))
                        elif count == 4:
                            ships[3] += 1
                            one_four.append((i, j, 'right'))
                    else:
                        ships[0] += 1
                        one_one.append((i, j))
                visited[i][j] = True
        answer = ships == self.num_ships
        locations = []
        if answer:
            locations.append(one_one)
            locations.append(one_two)
            locations.append(one_three)
            locations.append(one_four)
        return answer, locations

    def count_down(self, i, j, visited):
        """
        helper function to help the check_state function
        it counts the ship size at given location going up to down
        """
        count = 0
        for x in range(i, self.height):
            if self.board[x][j] == '1':
                count += 1
                visited[x][j] = True
            else:
                break
        return count, visited

    def count_right(self, i, j, visited):
        """
        helper function to help the check_state function
        it counts the ship size at given location going left to right
        """
        count = 0
        for y in range(j, self.height):
            if self.board[i][y] == '1':
                count += 1
                visited[i][y] = True
            else:
                break
        return count, visited


def forward_checking(state: State):
    """
    forward checking function that checks all possible states of the board keeping in mind the hints and constraints.
    """

    while (True):
        row_check = state.enforce_row_constraints()
        col_check = state.enforce_col_constraints()
        m_check = state.complete_m()
        if row_check is None and col_check is None and m_check is False:
            return True
        elif row_check is False or col_check is False:
            return False


def mrv(given, positions):
    """
    Minimum-Remaining-Values (MRV) heuristic: Choosing the variable with the fewest “legal” remaining
    values in its domain. In our case the one with the least constraint gets the priority.
    """
    def key_func(pos):
        i, j = pos
        return given.row_constraints[i] + given.column_constraints[j]

    return sorted(positions, key=key_func)


def backtracking_search(initial_state: State):
    """
    initiating the initial board with given hints, then forward checking to get the board ready for backtrack.
    """
    initial_state.initialise()
    forward_checking(initial_state)
    return backtrack(initial_state)


def backtrack(initial_state: State):
    """
    main backtracking function
    """
    empty_positions = initial_state.empty_positions()

    if (len(empty_positions) == 0):
        check, locs = initial_state.check_state()
        if check:
            return initial_state.board, locs
        else:
            return None, None
    else:
        empty_positions = mrv(initial_state, empty_positions)
        for pos in empty_positions:
            i, j = pos
            temp_state = copy.deepcopy(initial_state)
            temp_state.board[i][j] = '1'
            temp_state.water_ship(i, j)
            check = forward_checking(temp_state)
            if check:
                next_board, temp = backtrack(temp_state)
                if next_board is not None:
                    return next_board, temp
                else:
                    initial_state.board[i][j] = '.'
                    continue
            else:
                initial_state.board[i][j] = '.'
                if forward_checking(initial_state):
                    continue
                else:
                    return None, None
        return None, None

def update_board(board, locs):
    """
    helper function to use the locations of the ships to update and return the new board with all pieces placed.
    """
    for size in range(0,4):
        for ship_loc in locs[size]:
            if size == 0:
                i, j = ship_loc
                board[i][j] = 'S'
            elif size == 1:
                i,j,axis = ship_loc
                if axis == 'down':
                    board[i][j] = '^'
                    board[i+1][j] = 'v'
                if axis == 'right':
                    board[i][j] = '<'
                    board[i][j+1] = '>'
            elif size == 2:
                i, j, axis = ship_loc
                if axis == 'down':
                    board[i][j] = '^'
                    board[i + 1][j] = 'M'
                    board[i + 2][j] = 'v'
                if axis == 'right':
                    board[i][j] = '<'
                    board[i][j+1] = 'M'
                    board[i][j + 2] = '>'
            elif size == 3:
                i, j, axis = ship_loc
                if axis == 'down':
                    board[i][j] = '^'
                    board[i + 1][j] = 'M'
                    board[i + 2][j] = 'M'
                    board[i + 3][j] = 'v'
                if axis == 'right':
                    board[i][j] = '<'
                    board[i][j + 1] = 'M'
                    board[i][j + 2] = 'M'
                    board[i][j + 3] = '>'
    return board

def output_to_file(board):
    """
    helper function to output the solution board to text file
    """
    with open(args.outputfile, "w") as f:
        if board is None:
            f.write("No Solution Found.")
        else:
            for i, row in enumerate(board):
                f.write("".join(row))
                if i < len(board) - 1:
                    f.write("\n")


def read_from_file(filename):
    """
    helper function to read the file with constraints, number of ships and hints.
    """
    f = open(filename)
    row = f.readline().strip()
    row_con = [int(d) for d in row]
    col = f.readline().strip()
    col_con = [int(d) for d in col]
    ships = f.readline().strip()
    ship_con = [int(d) for d in ships]
    lines = f.readlines()
    board = [[str(x) for x in l.rstrip()] for l in lines]
    f.close()
    return row_con, col_con, ship_con, board


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--inputfile",
        type=str,
        required=True,
        help="The input file that contains the puzzles."
    )
    parser.add_argument(
        "--outputfile",
        type=str,
        required=True,
        help="The output file that contains the solution."
    )
    args = parser.parse_args()

    row_constraints, column_constraints, num_ships, initial_board = read_from_file(args.inputfile)
    initial = State(initial_board, row_constraints, column_constraints, num_ships)
    final, locations = backtracking_search(initial)
    if final is not None:
        final_board = update_board(final, locations)
        output_to_file(final_board)
    else:
        output_to_file(final)
