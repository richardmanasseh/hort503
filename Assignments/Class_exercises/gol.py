"""The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.
One interacts with the Game of Life by creating an initial configuration and observing how it evolves, or, for advanced players, by creating patterns with particular properties."""
"""The Rules
For a space that is 'populated':
Each cell with one or no neighbors dies, as if by solitude.
Each cell with four or more neighbors dies, as if by overpopulation.
Each cell with two or three neighbors survives.
For a space that is 'empty' or 'unpopulated'
Each cell with three neighbors becomes populated.

The Game of Life uses a grid of cells.
A cell is either on or off.
At each point of the game, every cell is checked to see if it needs to be turned off or on.
We will create two classes: one for a cell and one for the grid.
"""

class Cell(self, x, y, state):

        """This Class will model behavior of a collection of cells which,
        based on a few mathematical rules, can live, die or multiply.
        """

    def __init__(self, x, y, state): # to set up the initial attributes of a typical instance of the class
                                     # this function initializes the Cell. The x argument indicates the x-coordinate in the grid,
                                     # the y argument indicates the y coordinate in the grid, the state should be numeric
                                     # where 1 == on and 0 = off.
        self.x = x
        self.y = y
        self.state = state

    def get_state(self): # returns value stored in self.state; simply indicates if the cell is currently on or off
        return self.state

    def set_state(self, state): # receives an argument named state whose value is used to CHANGE the state of the cell (e.g. on or off).
                                # used to (re-)set state
                                # a cell is in one of two possible states, alive (on) or dead (off)
        if self.state == ON:
            if (neighbors < 2) and (neighbors == ON):
                newGrid[x, y] = OFF
            elif (neighbors == 2 or 3) and (neighbors == ON):
                newGrid[x, y] = ON


            elif (neighbors > 3) and (neighbors == ON):
                newGrid[x, y] = OFF

                if total == 3:
                    newGrid[i, j] = ON

        elif self.state == OFF:
            if (neighbors = 3) and (neighbors == ON):
                newGrid[x, y] = ON
            else:
                newGrid[x, y] = ON





1. If a cell is ON and has fewer than two neighbors that are ON, it turns OFF.
2. If a cell is ON and has either two or three neighbors that are ON, it remains ON.
3. If a cell is ON and has more than three neighbors that are ON, it turns OFF.
4. If a cell is OFF and has exactly three neighbors that are ON, it turns ON.




        self.balance = self.balance - withdrawal




        if self.state == 1:
            return off
        else:
            return on

        if self.state == 0:
            return on
        else:
            return off

test_cell(): # function is written outside of the class that lets you test each of the functions to make sure your class is working.

# Now let's create an Instance of class Cell....

test_cell = Cell(1, 0, 1)
# and test whether the methods defined in the class work when they're instances of the class:

print(test_cell.get_state(), 'has a state of ', test_cell.get_state())
test_cell.self.state(1)
test_cell.set_name()

class Grid(grid, rows, cols):

    def __init__(self, rows, cols):
                # this function sets the rows and column of the class variables and initializes the grid using those values.
                # Remember what you learned about initializing lists.
                # The grid is a 2D list and this takes some creativity.
                # This can get tricky (ask for help… don’t spend too much time on it).
        self.cols = cols
        self.rows = rows
 A given cell (i, j) in the simulation is accessed on a grid [i][j], where i and j are the row and column indices, respectively

    def print(self): # prints the grid to the terminal.  Prints a X if the cell is on and a - if it is off.

        pass


    def next_move(self): # currently, leave this function blank
        pass


    def set_cell(self, x, y, state): # set the cell at index (x, y) to a new state (e.g. ‘on’ or ‘off’)
        pass


    def play(self, ticks): # currently, leave this function blank
        pass
