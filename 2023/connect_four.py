# connect_four.py

def display_board(b):
    print("   A   B   C   D   E   F   G  ")
    print("||",b[5],"|",b[11],"|",b[17],"|",b[23],"|",b[29],"|",b[35],"|",b[41],"||")
    print("||---+---+---+---+---+---+---||")
    print("||",b[4],"|",b[10],"|",b[16],"|",b[22],"|",b[28],"|",b[34],"|",b[40],"||")
    print("||---+---+---+---+---+---+---||")
    print("||",b[3],"|",b[9],"|",b[15],"|",b[21],"|",b[27],"|",b[33],"|",b[39],"||")
    print("||---+---+---+---+---+---+---||")
    print("||",b[2],"|",b[8],"|",b[14],"|",b[20],"|",b[26],"|",b[32],"|",b[38],"||")
    print("||---+---+---+---+---+---+---||")
    print("||",b[1],"|",b[7],"|",b[13],"|",b[19],"|",b[25],"|",b[31],"|",b[37],"||")
    print("||---+---+---+---+---+---+---||")
    print("||",b[0],"|",b[6],"|",b[12],"|",b[18],"|",b[24],"|",b[30],"|",b[36],"||")
    print("===============================")
    print("II                           II")

def check_winner(board):
    

def main():
    board = [] # [' ', ' ', ' ', ]
    for i in range(42):
        board.append(" ")
    for i in range(4):
        board[i] = "O"
    # for i in range(4):
    #     board[i*6+2] = "x"


    display_board(board)

    


if __name__=="__main__":
    main()
    
    
    
# abstraction is my_function
# data is the param
def my_function(data):
	# iteration aka loop
	for element in data:
        # selection aka cond. st8ment
        if element > 10:
            # do something
        else:
            # do something different

        return # some calculated value

        # optionally it could print something
        #intead of returning a value
