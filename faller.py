from general_funcs import *
from jewel import *

class Faller:
    def __init__(self, top, mid, bot, col, board):
        self.col = col

        self.top = top
        self.mid = mid
        self.bot = bot
        self.status = '['
        self.board = board
        self.frozen = False

    def rotate(self):
        if self.status == "|" or self.status=="[":
            t = self.top.get_color()
            m = self.mid.get_color()
            b = self.bot.get_color()

            self.top.set_color(b)
            self.mid.set_color(t)
            self.bot.set_color(m)



            #print(self.top.get_color(), self.mid.get_color(), self.bot.get_color())

            bot_row = self.bot.get_row()
            mid_row = self.mid.get_row()
            top_row = self.top.get_row()

            #print(bot_row, mid_row, top_row)

            col = self.col
            if bot_row > -1:
                self.board.arr[bot_row][col] =  [self.status, self.bot.get_color(), status_dict[self.status]]
            if mid_row>-1:
                self.board.arr[mid_row][col] =  [self.status, self.mid.get_color(), status_dict[self.status]]
            if top_row>-1:
                self.board.arr[top_row][col] =  [self.status, self.top.get_color(), status_dict[self.status]]
        else:
            print("cannot rotate after frozen")

        

    def update_top(self, row, col):
        self.top.set_row(row)
        self.top.set_col(col)
    def update_mid(self, row, col):
        self.mid.set_row(row)
        self.mid.set_col(col)
    def update_bot(self, row, col):
        self.bot.set_row(row)
        self.bot.set_col(col)

    def freeze(self):
        if self.get_status() == "|":
            #self.frozen = True
            self.set_status(" ")
            #self.board.faller = None
            if has_vert_matches(self.board.arr)[0] == True:
                self.board.has_matches = True
                self.board.arr = has_vert_matches(self.board.arr)[1]
            #vert_matches = check_vert_matches(self.board.arr)
            """or row in vert_matches:
                print(row)"""
            #print(check_vert_matches(self.board.arr))
        else:
            print("You cannot freeze")
    def move_right(self):
        if not self.frozen:
            bot_row = self.bot.get_row()
            mid_row = self.mid.get_row()
            top_row = self.top.get_row()

            bot_cell_to_right = None
            mid_cell_to_right = None
            top_cell_to_right = None

            old_col = self.col
            if old_col+1 < len(self.board.arr[0]):
                right_col = old_col+1
                #bot
                bot_cell_to_right = self.board.arr[bot_row][right_col][1]
                mid_cell_to_right = self.board.arr[mid_row][right_col][1]

                top_cell_to_right = self.board.arr[top_row][right_col][1]
                if bot_cell_to_right == " " and mid_cell_to_right == " " and top_cell_to_right == " ":
                    #all of our cells are vacant to the left
                    #update the jewels with the new columns
                    self.update_bot(bot_row, right_col)
                    self.update_mid(mid_row, right_col)
                    self.update_top(top_row, right_col)
                    self.col = right_col
                    #update the grid
                    if bot_row>=0:
                        self.board.arr[bot_row][old_col] = [" ", " ", " "]
                        self.board.arr[bot_row][right_col] = [self.status,self.bot.get_color(), status_dict[self.status]]
                    if mid_row>=0:
                        self.board.arr[mid_row][old_col] = [" ", " ", " "]
                        self.board.arr[mid_row][right_col] = [self.status,self.mid.get_color(), status_dict[self.status]]
                    if top_row>=0:
                        self.board.arr[top_row][old_col] = [" ", " ", " "]
                        self.board.arr[top_row][right_col] = [self.status,self.top.get_color(), status_dict[self.status]]
                else:
                    print("cell is blocked")
            else:
                print("cannot move cell due to bounds")


    def move_left(self):
        if not self.frozen:
            bot_row = self.bot.get_row()
            mid_row = self.mid.get_row()
            top_row = self.top.get_row()

            bot_cell_to_left = None
            mid_cell_to_left = None
            top_cell_to_left = None

            old_col = self.col
            if old_col-1 >= 0:
                left_col = old_col-1
                #bot
                bot_cell_to_left = self.board.arr[bot_row][left_col][1]
                mid_cell_to_left = self.board.arr[mid_row][left_col][1]

                top_cell_to_left = self.board.arr[top_row][left_col][1]
                if bot_cell_to_left == " " and mid_cell_to_left == " " and top_cell_to_left == " ":
                    #all of our cells are vacant to the left
                    #update the jewels with the new columns
                    self.update_bot(bot_row, left_col)
                    self.update_mid(mid_row, left_col)
                    self.update_top(top_row, left_col)
                    self.col = left_col
                    #update the grid
                    if bot_row>=0:
                        self.board.arr[bot_row][old_col] = [" ", " ", " "]
                        self.board.arr[bot_row][left_col] = [self.status,self.bot.get_color(), status_dict[self.status]]
                    if mid_row>=0:
                        self.board.arr[mid_row][old_col] = [" ", " ", " "]
                        self.board.arr[mid_row][left_col] = [self.status,self.mid.get_color(), status_dict[self.status]]
                    if top_row>=0:
                        self.board.arr[top_row][old_col] = [" ", " ", " "]
                        self.board.arr[top_row][left_col] = [self.status,self.top.get_color(), status_dict[self.status]]
                else:
                    print("cell is blocked")
            else:
                print("out of bounds")

                


    def move_down(self):

        if not self.frozen:

            bot_row = self.bot.get_row()
            mid_row = self.mid.get_row()
            top_row = self.top.get_row()
            col = self.col
            self.update_bot(bot_row, col)
            self.update_mid(mid_row, col)
            self.update_top(top_row, col)
            col = self.bot.get_col()

            #check if bottom is inside bounds
            if fits_in_arr(self.board.arr, bot_row+1, col) and check_cell_empty(self.board.arr, bot_row+1, col):
                #print("fits")
                
                    
                self.update_bot(bot_row+1, col)
                self.update_mid(mid_row+1, col)
                self.update_top(top_row+1, col)

                bot_row = self.bot.get_row()
                mid_row = self.mid.get_row()
                top_row = self.top.get_row()
                if bot_row >-1:
                    self.board.arr[bot_row][col] =  [self.status, self.bot.get_color(), status_dict[self.status]]
                    if bot_row-1>=0:
                        self.board.arr[bot_row-1][col] =  [" ", " ", " "] 
                if mid_row > -1:
                    self.board.arr[mid_row][col] =  [self.status, self.mid.get_color(), status_dict[self.status]]
                    if mid_row-1>=0:
                        self.board.arr[mid_row-1][col] =  [" ", " ", " "]
                if top_row > -1:
                    self.board.arr[top_row][col] =  [self.status, self.top.get_color(), status_dict[self.status]]
                    if top_row-1>=0:
                        self.board.arr[top_row-1][col] =  [" ", " ", " "]  
                if not fits_in_arr(self.board.arr, bot_row+1, col) or not check_cell_empty(self.board.arr, bot_row+1, col):
                    self.set_status("|")
               
            
            
            

           

    def set_status(self, status):
        self.status = status
        col = self.bot.col
        top_row = self.top.get_row()
        mid_row = self.mid.get_row()
        bot_row = self.bot.get_row()
        print(top_row, mid_row, bot_row)
        arr = self.board.arr
        if top_row >=0:
            arr[top_row][col][0] = self.status
            arr[top_row][col][1] = self.top.get_color()
            arr[top_row][col][2] = status_dict[self.status]
        if mid_row>=0:
            arr[mid_row][col][0] = self.status
            arr[mid_row][col][1] = self.mid.get_color()
            arr[mid_row][col][2] = status_dict[self.status]
        if bot_row>=0:
            arr[bot_row][col][0] = self.status
            arr[bot_row][col][1] = self.bot.get_color()
            arr[bot_row][col][2] = status_dict[self.status]
        #edit the board too

    def get_status(self):
        return self.status
