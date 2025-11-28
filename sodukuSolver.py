class Soduku:
    def __init__(self,puzzle):
        self.puzzle = puzzle
    
    #this function return row and col if it find 0 otherwise None
    def find_empty_cell(self):
        #store the value and rows of cell that 0 exists.
        for row, values in enumerate(self.puzzle):
            #if 0 does not exist this will raise error so use try
            try:
                col = values.index(0)
                return row, col
            except ValueError: #meanning no 0
                pass
        return None #meaning no 0
    
    #we recive num from the final_fun(), then check wether that number already in that specific row.
    def check_in_row(self, row, num):
        #simple check the num in row, then return it
        return num not in self.puzzle[row]
    
    
    # check wether num already exist given col.
    def check_in_col(self, col, num):
        # I have to loop throuth all the rows, with that specific col to find this
        return all([self.puzzle[row][col] != num for row in range(9)])
        # or we can use
        # for each_row in range(0,9):
        #     if num == self.puzzle[each_row][col]:
        #         return False
        # return True
        # ----------
        
    # check num exist in 3 by 3 box
    def check_in_square(self,row, col, num):
        #find the start point of the row and column in 3*3 matrix
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        
        #loop throw row and find the number already exist
        #use nested loops
        for each_row in range(row_start, row_start + 3):
            for each_col in range(col_start, col_start + 3):
                if self.puzzle[each_row][each_col] == num:
                    return False
        return True #meaning num does not exist
        
        #check all the three condition are satisfied or not
    def is_valid(self, tuple_from_solver, num):
        # from the solver fun() or method we call num, row and col
        row, col = tuple_from_solver
        valid_in_row = self.check_in_row(row, num)
        valid_in_col = self.check_in_col(col, num)
        valid_in_sq = self.check_in_square(row,col, num)
        #check all must be true ,return T or F
        return all([valid_in_row, valid_in_col, valid_in_sq])
    
    # final function where we get num , row and cols
    def final_fun(self):
        # the first step is wether find_empty_cell return value or  or F , if f return true , done
        if (value_for_is_valid := self.find_empty_cell()) is None:
            #instead you can first asssign value_for_is_valid then check the condition
            return True 
        # we guess the number from 1,then 2...-9 and assign the value to num
        for guess in range(1,10):
            #call the function is valid with an argment value_for_is_valid and guess
           
            if self.is_valid(value_for_is_valid, guess):
                 # if it return true unpack the tuple that we get from the find_empty_cell and assign the value to that specific cell
                row, col = value_for_is_valid
                self.puzzle[row][col] = guess
                 
                 #we call the the function recusively , so that it start from the firts one call find_empty...and repreate the process
                if self.final_fun():
                     #if it return true we are done so we return true and finish the recursion
                    return True
                self.puzzle[row][col] = 0
        return False
                # else 
                     
# now print solved result
def solved(given_puzzle):
    puzzle_1 = Soduku(given_puzzle)
    print(f'Given puzzle: ')
    for v in puzzle_1.puzzle:
        k=[]
        for j in v:
            if j==0:
                j='#'
            k.append(str(j))
        print(' '.join(k))
        
    if puzzle_1.final_fun():
        print('\nSolved puzzle:\n'+'-'*30)
        for v in puzzle_1.puzzle:
            k=[]
            for j in v:
                k.append(str(j))
            print(' '.join(k))
        print('-'*30)
    else:
        print('This puzzle can not be solved!')
    return puzzle_1.puzzle

given = [
  [0, 9, 0, 4, 6, 0, 0, 0, 0],
  [0, 4, 0, 0, 0, 0, 0, 1, 6],
  [0, 0, 0, 0, 0, 0, 0, 5, 9],
  [0, 0, 0, 3, 0, 9, 2, 0, 7],
  [0, 0, 0, 0, 0, 0, 3, 0, 0],
  [3, 7, 0, 0, 8, 0, 0, 0, 0],
  [2, 0, 0, 0, 1, 8, 0, 0, 0],
  [0, 6, 0, 7, 0, 0, 0, 2, 0],
  [8, 0, 4, 6, 0, 0, 0, 0, 5]
]
solved(given)
            
            