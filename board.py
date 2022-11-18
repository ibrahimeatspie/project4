from general_funcs import *
from faller import *
from jewel import *
class Board:
    def __init__(self, arr, faller = None, has_matches = False):
        #state
        self.has_matches = False
        self.faller = None
        self.arr = arr
        self.rows = len(self.arr)
        self.cols = len(self.arr[0])
        
    def get_board(self):
        return self.arr

    def print_board(self):
        
        for i in range(len(self.arr)):
            print("|", end = "")
            for j in range(len(self.arr[i])):
                print(self.arr[i][j][0], end = "")
                print(self.arr[i][j][1], end = "")
                print(self.arr[i][j][2], end = "")
            print("|", end = "")
            print()
        print(" ", end = "")
        for i in range(3*self.cols):
            print("-", end="")
        print(" ", end = "")
        print()

    def insert_faller(self, faller):
        if self.faller == None:
            col = faller.col
            cell = self.get_board()[0][col][1]
            if cell == ' ':
                #it is empty
                curr_bot_row = faller.bot.get_row()
                #print(faller.bot.get_row(), faller.mid.get_row(), faller.top.get_row())
                #print(curr_bot_row)
                #curr_bot_col = None
                #faller.update_bot(curr_bot_row+1, col)
                self.faller = faller
                faller.move_down()
                #now our bot is set at 0, col
                #update the board to reflect this
                status = faller.get_status()
                #self.arr[curr_bot_row][col] = [status, faller.bot.get_color(), status_dict[status]]
                self.arr[curr_bot_row+1][col] = [status, faller.bot.get_color(), status_dict[status]]
                #print(self.get_board())
            else:
                print("cell is filled")
        else:
            print("already has faller")

        
    def iterate_time(self):
        print(self.has_matches)
        
        if self.faller.status == "|":
            
            self.faller.freeze()
            
            #check_vert_matches(self.arr)
        
        elif self.has_matches:
            print(self.faller.top.get_row())
            print(self.faller.mid.get_row())
            self.arr = remove_matches(self.arr)
        else:
            self.faller.move_down()
            #print("we have no faller")
        """
        If we have a faller, we move it down
        """
        """
        If we have a landed but not frozen, we freeze it. Then we check for matches. If matches,
        we make the matched characters "*"s
        """
        """
        If there are "*s", we remove them and check for stars again and again
        """
        pass    

            
            #move everything down
test = [
    [ [" ", " ", " "], [" ", "O", " "], [" ", " ", " "] ], #0
    [ [" ", " ", " "], [" ", "O", " "], [" ", "P", " "] ], #1
    [ [" ", " ", " "], [" ", "O", " "], [" ", "P", " "] ], #2
    [ [" ", "P", " "], [" ", "X", " "], [" ", "X", " "] ], #3
    [ [" ", "O", " "], [" ", "X", " "], [" ", "X", " "] ], #4
    [ [" ", "O", " "], [" ", "O", " "], [" ", "X", " "] ], #5
    [ [" ", "O", " "], [" ", "O", " "], [" ", "X", " "] ], #3
    [ [" ", "P", " "], [" ", "O", " "], [" ", "X", " "] ], #4
    [ [" ", "P", " "], [" ", "X", " "], [" ", "P", " "] ], #5
    
]
"""test = create_predef_arr(test)

#print(test)
test = check_vert_matches(test)
for row in test:
    print(row)"""



arr = create_predef_arr([
    [ [" ", "B", " "], [" ", " ", " "], [" ", " ", " "] ],
    [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ],
    [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ],
    [ [" ", "B", " "], [" ", " ", " "], [" ", " ", " "] ],
    [ [" ", "P", " "], [" ", " ", " "], [" ", " ", " "] ],
    
])


b = Board(arr)
b.print_board()
"""top = Jewel("Y", -3)
mid = Jewel("R", -2)
bot = Jewel("B", -1)
f2 = Faller(top, mid, bot, 0, b)"""

bot = Jewel("B", -1)


mid = Jewel("P", bot.get_row()-1)


top = Jewel("P", mid.get_row()-1)

f = Faller(top, mid, bot, 0, b)
b.insert_faller(f)
b.print_board()
b.iterate_time()
b.print_board()
b.iterate_time()
b.print_board()
b.iterate_time()
b.print_board()
b.iterate_time()










