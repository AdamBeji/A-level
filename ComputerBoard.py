#import AskName
#import AuthUserBoard
#PlayerFile = open(AskName.Name + ".txt","r")



CPUTable =[[" "," 0","1","2","3","4","5","6","7","8","9","10"],
        [" 0",".",".",".",".",".",".",".",".",".",".","."],
        [" 1",".",".",".",".",".",".",".",".",".",".","."],
        [" 2",".",".",".",".",".",".",".",".",".",".","."],
        [" 3",".",".",".",".",".",".",".",".",".",".","."],
        [" 4",".",".",".",".",".",".",".",".",".",".","."],
        [" 5",".",".",".",".",".",".",".",".",".",".","."],
        [" 6",".",".",".",".",".",".",".",".",".",".","."],
        [" 7",".",".",".",".",".",".",".",".",".",".","."],
        [" 8",".",".",".",".",".",".",".",".",".",".","."],
        [" 9",".",".",".",".",".",".",".",".",".",".","."],
        ["10",".",".",".",".",".",".",".",".",".",".","."]]




#PersonFile = open(AskName.Name+".txt","r")


import random
def CPUCoordinates():
    for row in CPUTable:
        print('\n')
        for column in row:
            print(column,end = " ")
    print('\n')
CPUShips = ['C','B','R','S','D']
CPUSize = [5,4,3,3,2]
Direction = ["north","west"]



length=len(CPUShips)
x=0
while x != length:
    RandomDirection = Direction[random.randint(0,1)]
    if RandomDirection == "north":
        Row =random.randint(6,11)
        Column = random.randint(1,11)
        counter = 0
        counter = Row+counter
        for z in range(CPUSize[x]):
            if CPUTable[counter][Column] == ".":
                counter = counter - 1
                if counter == (Row - CPUSize[x]):
                    for y in range(CPUSize[x]):
                        CPUTable[Row][Column] = CPUShips[x]
                        Row = Row-1
            if CPUTable[counter][Column] != ".":
                x=x-1
                break
        x=x+1
              


    if RandomDirection == "west":
        Row =random.randint(1,11)
        Column = random.randint(6,11)
        counter = 0
        counter = Column+counter
        for z in range(CPUSize[x]):
            if CPUTable[Row][counter] == ".":
                counter = counter - 1
                if counter == (Column - CPUSize[x]):
                    for y in range(CPUSize[x]):
                        CPUTable[Row][Column] = CPUShips[x]
                        Column = Column-1
            if CPUTable[Row][counter] != ".":
                x=x-1
                break
        x=x+1




CPUCoordinates()



#os.path.getsize(AskName.Name+".txt")
#if Empty ==0:
#    print("File is empty")
#if Empty != 0:
#    print("User has already played")

