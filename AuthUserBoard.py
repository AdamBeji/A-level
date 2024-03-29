class UserShips:
    def __init__(self, name, size):
        self.name=name
        self.size=size

    def SelectShip(self):
        if BoatInput == 'carrier':
            self.size = int(carrier.size)
            print("size = ",self.size)
            carrier.InputPosition()
        if BoatInput == 'battleship':
            self.size = int(battleship.size)
            print("size = ",self.size)
            battleship.InputPosition()
        if BoatInput == 'cruiser':
            self.size = int(cruiser.size)
            print("size = ",self.size)
            cruiser.InputPosition()
        if BoatInput == 'submarine':
            self.size = int(submarine.size)
            print("size = ",self.size)
            submarine.InputPosition()
        if BoatInput == 'destroyer':
            self.size = int(destroyer.size)
            print("size = ",self.size)
            destroyer.InputPosition()

class Position(UserShips):
    def __init__(self, name, size, RowHead, ColumnHead):
        super().__init__(name,size)
        self.RowHead = RowHead
        self.ColumnHead = ColumnHead

    def CA(self):
        carrier = UserShips('C','5')
        carrier.SelectShip()
    def BA(self):
        battleship = UserShips('B','4')
        battleship.SelectShip()
    def CR(self):
        cruiser = UserShips('R','3')
        cruiser.SelectShip()
    def SU(self):
        submarine = UserShips('S','3')
        submarine.SelectShip()
    def DE(self):
        destroyer = UserShips('D','2')
        destroyer.SelectShip()

    def InputPosition(self):
        def Coordinates():
            for row in Table:
                print('\n')
                for column in row:
                    print(column,end = " ")
            print('\n')            

        def AskDirections():
            Coordinates()
            rH = 0
            cH = 0
            while Table[rH][cH] != ".":
                rH = int(input("what is row head "))+1
                cH = int(input("what is column head "))+1

            Value = True
            while Value == True:
                try:
                    Value,Shape = AskShape(rH,cH)
                            
                except IndexError:
                    print("You cannot place a ship outside the board, try again")
            return rH,cH,Shape



        def AskShape(rH,cH):
            Shape = "x"
            Compass =["north","east","south","west","res"]
            print(Compass)
            print("To reselect your coordinate type RES")
            while Shape not in Compass:
                Shape = input("What direction do you want your ship to go? ").lower()
                if Shape in Compass:
                    if Shape == "res":
                        InputDirections()
                        
                    if Shape == "north":
                        for x in range(int(self.size)):
                            if Table[rH][cH] == ".":
                                rH=rH-1
                            if Table[rH][cH] != ".":
                                print("Cannot put ship here")
                                Shape = "x"
                                break                        
                        rH =rH + x + 1

                    if Shape == "south":
                        for x in range(int(self.size)):
                            if Table[rH][cH] == ".":
                                rH=rH+1
                            if Table[rH][cH] != ".":
                                print("Cannot put ship here")
                                Shape = "x"
                                break
                        rH =rH - x - 1

                    if Shape =="east":
                        for x in range(int(self.size)):
                            if Table[rH][cH] == ".":
                                cH=cH+1
                            if Table[rH][cH] != ".":
                                print("Cannot put ship here")
                                Shape = "x"
                                break
                        cH =cH - x - 1

                    if Shape =="west":
                        for x in range(int(self.size)):
                            if Table[rH][cH] == ".":
                                cH=cH-1
                            if Table[rH][cH] != ".":
                                print("Cannot put ship here")
                                Shape = "x"
                                break
                        cH =cH + x + 1
            Value = False
            return Value,Shape


        def InputDirections():
            rH,cH,Shape = AskDirections()
            PersonFile = open(AskName.Name +".txt","a")
            PersonFile.write(str(rH)+":"+str(cH)+",")
            if Shape == "north":
                for y in range(int(self.size)):
                    Table[rH][cH]= self.name
                    rH=rH-1
                    PersonFile.write(str(rH)+":"+str(cH)+",")
            if Shape == "south":
                for y in range(int(self.size)):
                    Table[rH][cH]= self.name
                    rH=rH+1
                    PersonFile.write(str(rH)+":"+str(cH)+",")
            if Shape =="east":
                for y in range(int(self.size)):
                    Table[rH][cH]= self.name
                    cH=cH+1
                    PersonFile.write(str(rH)+":"+str(cH)+",")

            if Shape =="west":
                for y in range(int(self.size)):
                    Table[rH][cH]= self.name
                    cH=cH-1
                    PersonFile.write(str(rH)+":"+str(cH)+",")
            PersonFile.close()
            Coordinates()
        InputDirections()

import AskName
import Authentification
Authentification.PlayerAuthentification()
rH = "rH"
cH = "cH"
Table =[[" ","0","1","2","3","4","5","6","7","8","9","10","11"],
        [" 0",".",".",".",".",".",".",".",".",".",".",".","."],
        [" 1",".",".",".",".",".",".",".",".",".",".",".","."],
        [" 2",".",".",".",".",".",".",".",".",".",".",".","."],
        [" 3",".",".",".",".",".",".",".",".",".",".",".","."],
        [" 4",".",".",".",".",".",".",".",".",".",".",".","."],
        [" 5",".",".",".",".",".",".",".",".",".",".",".","."],
        [" 6",".",".",".",".",".",".",".",".",".",".",".","."],
        [" 7",".",".",".",".",".",".",".",".",".",".",".","."],
        [" 8",".",".",".",".",".",".",".",".",".",".",".","."],
        [" 9",".",".",".",".",".",".",".",".",".",".",".","."],
        ["10",".",".",".",".",".",".",".",".",".",".",".","."],
        ["11",".",".",".",".",".",".",".",".",".",".",".","."]]
carrier = Position('C','5',rH,cH)
battleship = Position('B','4',rH,cH)
cruiser = Position('R','3',rH,cH)
submarine = Position('S','3',rH,cH)
destroyer = Position('D','2',rH,cH)

Vessel = ['carrier','battleship','cruiser','submarine','destroyer']
Enter = input("Press enter to start   ")
while len(Vessel) != 0:
    print(Vessel)
    BoatInput = "x"
    while BoatInput not in Vessel:
        BoatInput = input("What ship do you want? ").lower()
    Vessel.remove(BoatInput)
    print(BoatInput," selected")
    if BoatInput == 'carrier':
        carrier.CA()
    if BoatInput == 'battleship':
        battleship.BA()
    if BoatInput == 'cruiser':
        cruiser.CR()
    if BoatInput == 'submarine':
        submarine.SU()
    if BoatInput == 'destroyer':
        destroyer.DE()

