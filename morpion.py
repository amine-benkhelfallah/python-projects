board = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
running = True

def board_display():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()

def victory1(player1):
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        print(user1+" est le grand gagnant!")
        return running == False
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        print(user1+" est le grand gagnant!")
        return running == False
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        print(user1+" est le grand gagnant!")
        return running == False
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print(user1+" est le grand gagnant!")
        return running == False
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print(user1+" est le grand gagnant!")
        return running == False
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print(user1+" est le grand gagnant!")
        return running == False
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print(user1+" est le grand gagnant!")
        return running == False
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print(user1+" est le grand gagnant!")
        return running == False

def victory2(player2): 
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        print(user2+" est le grand gagnant!")
        return running == False
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        print(user2+" est le grand gagnant!")
        return running == False
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        print(user2+" est le grand gagnant!")
        return running == False
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        print(user2+" est le grand gagnant!")
        return running == False
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        print(user2+" est le grand gagnant!")
        return running == False
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        print(user2+" est le grand gagnant!")
        return running == False
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print(user2+" est le grand gagnant!")
        return running == False
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        print(user2+" est le grand gagnant!")
        return running == False

def check_input(user):
    play= input(user+" joue (ligne puis colonne) : ")
    while len(play) > 3 or len(play) < 3 :
        print("Choisir un chiffre entre 1 et 3 pour la ligne, ainsi que la colonne, les deux séparés d'un espace\n")
        play= input(user+" joue (ligne puis colonne) : ")
    while play != "1 1" and play != "1 2" and play != "1 3" and play !=  "2 1" and play !=  "2 2" and play !=  "2 3" and play !=  "3 1" and play != "3 2" and play != "3 3":
        print("Choisir un chiffre entre 1 et 3 pour la ligne, ainsi que la colonne, les deux séparés d'un espace\n")
        play = input(user+" joue (ligne puis colonne) : ")
    return play


def ranking(winner):
    with open("score.txt", "w") as f:
            f.write(winner+" 1")


action=[]
while action != 1 and action != 2:
    action = int(input("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Bonjour et bienvenus sur le jeu du Morpion <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< , \nPour jouer tapez 1 :  \nPour afficher les scores tapez 2 : "))
    if action==2 :
        print("scores")
    elif action ==1 :
        user1 = input("Le nom du premier joueur? ")
        user2 = input("Le nom du second joueur? ")

    
        while running != False:
            
            board_display()
            
            play1, play2 = check_input(user1).split()
            ligne1 = int(play1)
            colonne1 = int(play2)
            check = 1  
            while check == 1:
                if board[ligne1-1][colonne1-1] != "-":
                    print("Ceci a déja été joué\n")
                    play1, play2 = check_input(user1).split()
                    ligne1 = int(play1)
                    colonne1 = int(play2)
                else:
                    board[ligne1-1][colonne1-1] = "X"
                    check = 2          
            board_display()
            running = victory1(board)
            if running == False:
                ranking(user1)
                break
            if "-" not in board[0][0] and "-" not in board[0][1] and "-" not in board[0][2] and "-" not in board[1][0] and "-" not in board[1][1] and "-" not in board[1][2] and "-" not in board[2][0] and "-" not in board[2][1] and "-" not in board[2][2]:
                print (">>>>>>>>>>>>>>>>>>>>>>>> Match nul ! <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                break

            play3, play4 = check_input(user2).split()
            ligne2 = int(play3)
            colonne2 = int(play4)
            check = 1  
            while check == 1:
                if board[ligne2-1][colonne2-1] != "-":
                    print("Ceci a déja été joué\n")
                    play3, play4 = check_input(user2).split()
                    ligne2 = int(play3)
                    colonne2 = int(play4)
                else:
                    board[ligne2-1][colonne2-1] = "O"
                    check = 2
            running = victory2(board)
            if running == False:
                ranking(user2)
                break
else:
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> choix invalide <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")