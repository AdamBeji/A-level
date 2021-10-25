def PlayerAuthentification():
    New = 'New'
    while New != "n" or New != "y" or New != "yes" or New != "no":
        New = input("Are you a new user? - ").lower()
        if New == "n" or New == "no":
            ExistingPlayer()
            break
        if New == "y" or New == "yes":
            NewPlayer()
            break
    
def ExistingPlayer():
    UserFound = False
    while UserFound == False:           
        import AskName
        AskName.Name =input("What is your Username? - ")
        
        with open('Usernames.txt') as UsernameFile:
            UserNoOfLines = -1  
            lines = UsernameFile.readlines()
            for line in lines:
                UserNoOfLines = UserNoOfLines + 1
                Splitting = line.split(",")
                if Splitting[0] == AskName.Name:
                    print("Your Username has been found")
                    UserFound = True
                    ExistingPassword(Splitting,UserNoOfLines)
        if UserFound == False:
            print("It seems we cannot find that Username or you entered it incorrectly, please try again.")

    class Person:
        def __init__(self,User,line):
            self.User=User
            self.__line=line
    with open(AskName.Name +".txt") as ExistPlayerFile:
        lines = ExistPlayerFile.readlines()
        for line in lines:
            Person1 = Person(User,line)
    try:
        print(Person1.__line)
    except:
        print("You cannot see your previous attempts just yet")

def ExistingPassword(Splitting,UserNoOfLines):
    def FindsPasswordKey():
        with open('Usernames.txt') as UsernameFile:
            lines = UsernameFile.readlines()
            lines = lines[UserNoOfLines]
        NoOfCharacters = 0
        KeyNoOfLines=-1
        with open("key.txt") as HashFile:
            lines2 = HashFile.readlines()                  
            lines2 = lines2[UserNoOfLines]    
            for x in range(len(lines2)):
                if lines2[x] == ",":
                    NoOfCharacters = NoOfCharacters+1       
        with open('key.txt') as HashFile:
            lines2 = HashFile.readlines()
            for line in lines2:
                KeyNoOfLines = KeyNoOfLines+1
                if UserNoOfLines == KeyNoOfLines:
                    Splitting2 = line.split(",")
        FindsProperPassword(NoOfCharacters,Splitting2)
    def FindsProperPassword(NoOfCharacters,Splitting2):
        BlankSpace = []
        separator=""
        for y in range(NoOfCharacters):
            Splitting[y+1]=int(Splitting[y+1])/int(Splitting2[y])  
            BlankSpace.append(chr(int(Splitting[y+1])))                                
            Idation = (separator.join(BlankSpace))
        ChecksUserPassword(Idation)
    def ChecksUserPassword(Idation):
        Valid = False
        while Valid == False:
            Password = input("What is your Password? - ")
            if Idation == Password:
                print("You have been validated")
                Valid = True
            if Valid == False:
                print("Incorrect Password, please try again.") 
                BlankSpace = []
    FindsPasswordKey()
def NewPlayer():
    UserTaken = False
    import os
    while UserTaken == False:
        import AskName
        AskName.Name =input("What is your Username? - ")
        with open('Usernames.txt') as UsernameFile:
            Empty = os.path.getsize("Usernames.txt")
            if Empty ==0:
                UserTaken = True
                break
            lines = UsernameFile.readlines()
            for line in lines:
                Splitting = line.split(",")
                if Splitting[0] == AskName.Name:
                    print("Sorry, this Username has already been tacken, try again")
                    UserTaken = False
                    break
                else:
                    UserTaken = True
        if UserTaken == True :
            print("Hello- ", AskName.Name, " , -this will be saved as your new Username")


    if UserTaken == True:
        UsernameFile=open("Usernames.txt","a")
        UsernameFile.write(AskName.Name)
        UsernameFile.close()
        NewPlayerFile = open(AskName.Name + ".txt","a+")
        NewPassword()



def NewPassword():
    def SatisfactoryPassword():

        def ZeroValues():
            SatisCap = 0
            SatisLow = 0
            SatisNum = 0
            SatisLength = 0
            return SatisCap,SatisLow,SatisNum,SatisLength

        def CheckCharacters(length,Password):
            Password.split()
            SatisCap,SatisLow,SatisNum,SatisLength = ZeroValues()
            for x in range (length):
                if ord(Password[x])>=65 and ord(Password[x])<=90:
                    SatisCap = SatisCap+1
                if ord(Password[x])>=97 and ord(Password[x])<=122:
                    SatisLow = SatisLow+1
                if ord(Password[x])>=48 and ord(Password[x])<=57:
                    SatisNum = SatisNum+1
                if len(Password)>=8:
                    SatisLength = SatisLength+1
            return SatisCap,SatisLow,SatisNum,SatisLength

        def InputPassword():
            SatisCap,SatisLow,SatisNum,SatisLength = ZeroValues()
            while SatisCap == 0 or SatisLow == 0 or SatisNum ==0 or SatisLength ==0:
                print("Password must include at least one capital, one lowercase and a number and be more than eight characters")
                Password = input("Please enter a satifactory Password? - ")
                length = len(Password)
                SatisCap,SatisLow,SatisNum,SatisLength = CheckCharacters(length,Password)
            return length,Password
            
        length,Password = InputPassword()
        return length,Password
        
                
    def CreateHashAndKey():
        length,Password = SatisfactoryPassword()
        import random
        UsernameFile=open("Usernames.txt","a")
        KeyFile=open("key.txt","a")
        for Repeat in range (0,length):
            RandomNumber = random.randint(1,100)
            Position = random.randint(0,length-1)
            RandomCharacter = int(ord(Password[Position]))
            RandomKey = (RandomNumber) * (RandomCharacter)
            Hash = (RandomKey)*(ord(Password[Repeat]))
            KeyFile.write(str(RandomKey) + ",")
            UsernameFile.write("," + str(Hash))
        KeyFile.write("\n")
        UsernameFile.write("\n")
        KeyFile.close()
        UsernameFile.close()
    CreateHashAndKey()






