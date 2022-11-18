status_dict = {"[": "]", "|": "|", "*": "*", " ": " "}


def create_size_arr(rows, cols):
    arr = []
    for i in range(rows):
        arr.append([])
        for j in range(cols):
            arr[i].append([])
            arr[i][j].append(" ")
            arr[i][j].append(" ")
            arr[i][j].append(" ")
    return arr


def create_predef_arr(arr):
    for i in range(len(arr)-2, -1, -1):
        # print(arr[i])
        for j in range(len(arr[i])):
            curr_row = i
            curr_col = j

            curr_char = arr[curr_row][curr_col][1]

            if curr_char == " ":
                continue
            else:
                if curr_row == len(arr)-1:
                    continue
                else:

                    while curr_row+1 < len(arr) and arr[curr_row+1][curr_col][1] == " ":
                        arr[curr_row+1][curr_col][1] = arr[curr_row][curr_col][1]
                        arr[curr_row][curr_col][1] = " "
                        curr_row += 1

    return arr


"""a = [
    [ [" ", "B", " "], [" ", " ", " "], [" ", " ", " "] ],
    [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ],
    [ [" ", "Y", " "], [" ", " ", " "], [" ", " ", " "] ],
    [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ],
    [ [" ", "R", " "], [" ", " ", " "], [" ", " ", " "] ],
    
]"""


"""
[
    [ [" ", "B", " "] [" ", " ", " "] [" ", " ", " "] ]
    [ [" ", " ", " "] [" ", "A", " "] [" ", " ", " "] ]
    [ [" ", "C", " "] [" ", " ", " "] [" ", "B", " "] ]
    
]


"""


def fits_in_arr(arr, row, col):
    #print(len(arr), row)
    if row >= len(arr) or col >= len(arr[0]):
        return False

    else:
        return True


def check_cell_empty(arr, row, col):
    # print(len(arr),row)

    if arr[row][col][1] == " ":
        return True
    else:
        return False


def has_vert_matches(arr):
    checked_points = set()
    matching_tuples_arr = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            char = arr[i][j][1]
            coords = []
            if char == " " or (i,j) in checked_points:
                continue
            else:
                tuple_arr = []
                tuple_arr.append((i, j))
                row = i
                while row < len(arr):
                    if row+1 >= len(arr):
                        break
                    else:
                        row += 1
                        curr_char = arr[row][j][1]
                        if curr_char == char:
                            tuple_arr.append((row, j))
                        else:
                            break
                if len(tuple_arr) >= 3:
                    for point in tuple_arr:
                        curr_color = arr[point[0]][point[1]][1]
                        arr[point[0]][point[1]] = ["*", curr_color,"*"]
                    return (True,arr)
    return (False, arr)           



def check_matches(arr):
    checked_points = set()
    matching_tuples_arr = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            char = arr[i][j][1]
            coords = []
            if char == " " or (i,j) in checked_points:
                continue
            else:
                tuple_arr = []
                tuple_arr.append((i, j))
                row = i
                while row < len(arr):
                    if row+1 >= len(arr):
                        break
                    else:
                        row += 1
                        curr_char = arr[row][j][1]
                        if curr_char == char:
                            tuple_arr.append((row, j))
                        else:
                            break
                if len(tuple_arr) >= 3:
                    for point in tuple_arr:
                        checked_points.add(point)
                    matching_tuples_arr.append(tuple_arr)
    #print(len(matching_tuples_arr))
    if len(matching_tuples_arr) > 0:
        for tuple_arr in matching_tuples_arr:
            for coord in tuple_arr:
                arr[coord[0]][coord[1]][1] = " "
        arr = create_predef_arr(arr)
        
        return check_matches(arr)
    else:
        return(arr)

def remove_matches(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            curr_char_status = arr[i][j][0]
            if curr_char_status == "*":
                arr[i][j] = [" ", " ", " "]
                
    arr = create_predef_arr(arr)
    return arr
