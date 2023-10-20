import os.path

def bubbleSort(w):
    for j in range(len(w)-1):
        for k in range(len(w)-1-j):
            if w[k]>w[k+1]:
                w[k],w[k+1]=w[k+1],w[k]

def hClub():
    while True:
        print("\n"+" \_*** We love hockey *** _/ " + "\n" +
            "Code for managing players of ice hockey team.")
        print("[1] Print names of the players in this team" + "\n" +
            "[2] Add a player to the team" + "\n" +
            "[3] Kick out a player from the team" + "\n" + "[4] Sort players" +
            "\n" + "[5] Save the list of players to the desktop" + "\n" +
            "[6] Load the list of players from desktop" + "\n" + "[0] Stop the code")
        o = input("Enter your choice: ")
        if o.isnumeric() == False:
            print("\n    ERROR:"+"Your choice must be a number."+"\n")
            
        else:
            option = int(o)
            print("\n")
            if option == 0:
                break
            elif option == 1:
                myFile = open(f"./players.txt", "r")
                fileRead = myFile.read()
                myFile.close()
            
                print(fileRead)
            
            elif option == 2:
                name = input("Write the name of the player you want to add (type ! to end the process): ")
                if name == "!":
                    break
                else:
                    myFile = open(f"./players.txt", "a+")
                    fileAppend= myFile.write(name+"\n")
                    myFile.close()

            elif option == 3:
                name = input("Write the name of the player you want to kick out (type ! to end the process): ")
                if name == "!":
                    break
                else:
                    myFile = open(f"./players.txt", "r+")
                    fileR1 = myFile.readlines()
                    myFile.close()
                    nn = name+"\n" not in fileR1
                    if nn!=True:
                        for i in range(len(fileR1)):
                            if fileR1[i] == name+"\n":
                                del fileR1[i]
                                myFile = open(f"./players.txt", "w")
                                fileR2 = myFile.writelines(fileR1)
                                myFile.close()
                    else:
                        print("    ERROR:"+"List of players doesn' t contain "+name+"."+"\n")
                    
                
                        
            elif option == 4:
                myFile = open(f"./players.txt", "r")
                fileL = myFile.readlines()
                myFile.close()

                bubbleSort(fileL)
                for i in range(len(fileL)):
                    print(fileL[i])
            
            elif option == 5:
                while True:
                    name = input("Enter the name of file that is to be created (type ! to end the process): ")
                    if name == "!":
                        break
                    else:
                        path= f"./../"+name+".txt" #name
                        
                        exist= os.path.exists(path)
                        print("\n")
                        if exist == False:
                            myFile = open(path, "x")
                            myFile.close()
                        
                            myFile = open(f"./players.txt", "r")
                            fileR = myFile.read()
                            myFile.close()

                            myFileA = open(path, "a")
                            for i in range(len(fileR)):
                                filea = myFileA.write(fileR[i])
                            myFile.close()
                            print("List was saved to the desktop.\n It will take a while before apearing on your desktop but you can already find it in files.\n And for you to be able to load the list using this code, you' ll have to restart this code.")
                            break
                        elif exist == True:
                            print("    ERROR:"+"File with that name does already exist."+"\n")

                
                
            elif option == 6:
                while True:
                    name = input("Enter the name of file that is to be loaded (type ! to end the process): ")
                    if name == "!":
                        break
                    else:
                        path= f"./../"+name+".txt" #name
                        
                        exist= os.path.exists(path)
                        print("\n")
                        if exist == True:
                            myFile = open(path, "r")
                            fileRead = myFile.read()
                            myFile.close()
                            print(fileRead)
                        elif exist == False:
                            print("    ERROR:"+"The file you want to open does not exist"+"\n")
                            
            
                
            else:
                print("You have chosen invalid option.")
            

hClub()
