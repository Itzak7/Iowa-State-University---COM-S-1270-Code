#Isaac Aguilar               12/2/2025      
#Assignment Number 6(7) ;) 

# This is my final code for COMS 1270!!! HOPE YOU ENJOY!!! 
# This code is a code that produces the game of Candy LAND! The user will be able to choose 3 options and will be able to see    
# either the 1) instructions 2) quit the program or 3) play the game! If the user chooses to play they will have the option to play    
# against an 3 other AI's or with 3 other friends! The program will not quit unless directed by the user. Other than that hope you have fun! 

import random 
print("")
print("Welcome to the great realm of CANDY REALM!")
print("")
print("By Yours Truly: Isaac Aguilar [COMS 1270 (4)]")

def DaRules():
    print("")
    print("The Rules To Candy Realm!:")
    print("1) Your objective is to move through the candy realm by matching the card you draw to the board space." \
    " The first player to the end wins!")
    print("")
    print("2) Before each game, 4 total players will play and you will choose whether you play with AI or humans (you can mix and match like 2 humans and 2 AI!).")
    print("")
    print("3) Everyone will start at the start space (represented as a 'S' thats at the far left! ) and travel through the borad full of colored spaces. Each space has a color represented to it and players move " \
    "forward by matching the color of the card they draw to the color on the board until they reach the end (represented as a 'G')!!! ")
    print("")
    print("4) The deck will contain many cards, a majority of them being color cards. But the user chooses how many copies are included in the deck at the start (from 1 to 5 copies per color). " \
    "Per players turn they will be able to 1)draw a card or 2) Shuffle the deck!!! If you wish to draw, you will move your piece to the next space that matches the card's color. (If you are 1 space before the end, your next card matches the goal!)")
    print("")
    print("5) SPECIAL SPACES!!! 1)UNLUCKY RUBBER DUCKY: If a player lands on a 'X' they become stuck! this player must skip their NEXT TURN to be able to move on, if not they continue to be stuck!" \
    " 2)QUICK SLIDE!!! If a player lands on a 'S' space they will instantly jump forward to the 'E'!!!")
    print("")
    print("That's it for the rules!!! Hope that made sense and hope you have LOTS of fun playing!!!!")
    print("GOOD LUCK OUT THERE IN THE CRAZY REALM OF CANDY!!!")

def CreateBoard():
    Board = ["START!", "B", "R", "V", "X", "O", "S", "P", "Y", "B", "R", "V", "X", "O", "P", "E", "Y", "B", "R", "V", "X", "O", "P", "Y", "GOAL!"]
    return Board

def CreateDeck():
    Colors =["B", "R", "V", "O", "P", "Y", "X","S"]
    while True:
        Copies = input("How many copies of each card would you like? (1-5): ")
        try:
            CopiesINT = int(Copies)
        except:
            print("WOAH THERE PARTNER! please enter a NUMBER between 1 and 5!!!")
            continue
        if CopiesINT < 1 or CopiesINT > 5: 
            print(f"UMMM... you can only choose 1-5, not {CopiesINT}....")
            print("Please Try again...")
            continue
        else:
            Deck = []
            for color in Colors:
                for i in range(CopiesINT):
                    Deck.append(color)
            random.shuffle(Deck)
            return Deck

def Players():
    while True:
        Players = input("How many HUMAN players are going to play (1-4)?: ")
        try:
            PlayersINT = int(Players)
        except:
            print(f"PARTNER THATS WRONG! I said choose between 1 and 4! Not {Players}!!!")
            continue
        if PlayersINT < 1 or PlayersINT > 4:
            print(f"UMMM... you can only choose 1-4, not {PlayersINT}....")
            print("Please Try again...")
            continue
        else:
            break
    AllPlayers = []
    for i in range(PlayersINT):
            X = {}
            X["Player"] = f"Player {i +1}"
            X["Position"] = 0 
            X["Unlucky"] = False 
            X["Type"] = "HUMAN (LETS GOOO)"
            AllPlayers.append(X)
    AI = 4 - PlayersINT 
    for i in range(AI):
            Y = {}
            Y["Player"] = f"AI {i +1}"
            Y["Position"] = 0 
            Y["Unlucky"] = False 
            Y["Type"] = "AI (BOOOO)"
            AllPlayers.append(Y)
    
    return AllPlayers

def MakeBoard(Board, Allplayers):
    print("=" * 67)
    for i in range(len(Allplayers)):
        Row = ""
        for X in range(len(Board)):
            if Allplayers[i]["Position"] == X:
                Row += f"{i+1} "
            else:
                Row += "  "
        print(Row)

    print("-" * (len(Board) * 2))

    boardROW = ""
    for i in Board:
        boardROW  += i[0] + " "
    print(boardROW )

    print("=" * 67)


def FindNextColor(Board, Position, CardColor):
    for i in range(Position + 1, len(Board)):
        if Board[i] == CardColor:
            return i
    return -1

def PlayGame():
    TheBoard = CreateBoard()
    ThePlayers = Players()
    TheDeck = CreateDeck()
    
    Winner = None
    
    while Winner is None:
        
        for p in ThePlayers:
            MakeBoard(TheBoard, ThePlayers)
            print(f"It is {p['Player']}'s turn!")
            
            if p["Unlucky"] == True:
                print("You are stuck by the Unlucky Rubber Ducky! Skipping your turn (LOL).")
                p["Unlucky"] = False
                input("Press Enter to continue...")
                continue

            if len(TheDeck) == 0:
                print("UH OH! The deck is empty! LOOKS LIKE WE NEED A NEW DECK!")
                TheDeck = CreateDeck()

            if "HUMAN" in p["Type"]:
                choice = input("Do you want to [D]raw a card or [S]huffle the deck? ").upper()
                if choice == "S":
                    print("Shuffling the deck!")
                    random.shuffle(TheDeck)
                    input("Press Enter to continue...")
                    continue
            else:
                print(f"{p['Player']} (AI) is drawing a card...")

            current_pos = p["Position"]

            while True:
                if len(TheDeck) == 0:
                    print("The deck is empty! Building a new Candy Realm deck!")
                    TheDeck = CreateDeck()

                card = TheDeck.pop(0)
                print(f"{p['Player']} drew a {card} card!")

                next_pos = FindNextColor(TheBoard, current_pos, card)

                if next_pos == -1:
                    if current_pos == len(TheBoard) - 2:
                        print("You're right in front of the GOAL!!! FLYING TO THE GOAL!")
                        p["Position"] = len(TheBoard) - 1
                        break
                    else:
                        print("UH OH!!! No more of that color ahead... drawing another card!")
                        continue
                else:
                    p["Position"] = next_pos
                    break

            landed_on = TheBoard[p["Position"]]
            
            if landed_on == "X":
                print("UH OH! You landed on an Unlucky Rubber Ducky (X)! You'll be stuck next turn!(LOL)")
                p["Unlucky"] = True
            
            elif landed_on == "S":
                print("Quick Slide!!! Sliding all the way to 'E'!")
                for i in range(len(TheBoard)):
                    if TheBoard[i] == "E":
                        p["Position"] = i
                        break

            if p["Position"] == len(TheBoard) - 1:
                Winner = p
                break
                
            input("Press Enter to continue to the next turn...")

        if Winner is not None:
            break

    print("*"*67)
    print(f"CONGRATULATIONS, {Winner['Player']}!! YOU WIN THE CANDY REALM!!!")
    print("*"*67)


def main():
    while True:
        print("===================================================")
        print("This Is The MAIN MENU!")
        Choice = input("What Would You Like To Do?: [P]lay Candy Realm, [L]earn The Rules, or [Q]uit: ").upper()
        if Choice == "P":
            PlayGame()
        elif Choice == "L":
            DaRules()
        elif Choice =="Q":
            print("Your wish to quit is my command! Hope you had fun and come back soon!!!")
            break
        else: 
            print("UH OHHHH! Your input was an invaild one (LOL)! Please try again! This time a vaild choice!!! ")

if __name__=="__main__":
    main()