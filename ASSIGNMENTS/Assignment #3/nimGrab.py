#Isaac Aguilar        10-10-2025
#Assessment #3 
#
#This code progams a game that is called NimGrab where your goal is to not be the last one to take an item. Users will have the option to play the game against another human or computer! 
#They will also have the option to read the rules or quit! The program will not quit until the user chooses to quit.

import random
print()
print ("The Amazing Game Of NimGrab!!!")
print()
print("By:Isaac Aguilar")
print("[COMS 1270 4]")

def Rules():
    print()
    print("Your objective is to NOT be the last player to take an item, if you take the last one, you lose!")
    print()
    print("Rules/Gameplay:")
    print("1) A row of 20-25 items will be placed in the middle.")
    print ("2) Players will take turns removing the items from the row.")
    print("3) On said players turn they must remove at least X amount or at most Y amount of items.")
    print("4) Players cannot take more items than are left(Ex: if there are 2 items left, you can take either 1 or 2 but not 3, that would be an invalid move).")
    print("5) You win when you force your opponent to take the last item!")
    print()
    print("Thats it! Good Luck and Have fun!")
    print()
   

def main():
   while True:
    print()
    Choice = input ("What would you like to do? [P]lay the game, [R]ead the rules, or [Q]uit?:  ").upper()
    if Choice=="P":
      Gamemode = input("Would you like to play against another [H]uman or a [C]omputer?: ").upper()
      Row = random.randrange (20,25+1)
      currentPlayer= "Player 1"
      
      if Gamemode=="H":
            X = int(input("Please choose the lowest amount you would like to take during this game!: "))
            Y = int(input("Please choose the highest amount you would like to take during this game!: "))
            
            while Row > 0:
               print(f"Items left!: {Row}")
               print("|"* Row )
               if currentPlayer=="Player 1":
                while True:
                   Taken = int(input(f"How many items would you like to take Player 1?[{X}-{Y}]: "))
                   if Taken < X or Taken > Y:
                      print (f"UH OH!!! You chose an invalid option. Please choose a number between {X}-{Y}")   
                   elif Taken > Row:
                      print (f"LOL! Nice try taking more than whats left! Please try again, but dont take more than {Row} this time!")
                   else:
                      break   
                
                Row = Row - Taken 
                if Row == 0:
                   print("Player 1 took the final item! Player 2 wins!!!")
                   break
                currentPlayer= "Player 2" 

               else:
                  while True:
                     Taken = int(input(f"How many items would you like to take Player 2?[{X}-{Y}]: "))
                     if Taken < X or Taken > Y:
                        print(f"UH OH!!! You chose an invalid option. Please choose a number between {X}-{Y}")   
                     elif Taken > Row:
                        print (f"LOL! Nice try taking more than whats left! Please try again, but dont take more than {Row} this time!")
                     else:
                        break
                 
                  Row = Row - Taken 
                  if Row == 0:
                     print ("Player 2 took the final item! Player 1 wins!!!")
                     break 
                  currentPlayer = "Player 1"
               
      
      elif Gamemode=="C":
            X = int(input("Please choose the lowest amount you would like to take during this game!: "))
            Y = int(input("Please choose the highest amount you would like to take during this game!: "))
            
            while Row > 0:
               print(f"Items left!: {Row}")
               print("|"* Row )
               if currentPlayer=="Player 1":
                while True:
                   Taken = int(input(f"How many items would you like to take Player 1?[{X}-{Y}]: "))
                   if Taken < X or Taken > Y:
                      print (f"UH OH!!! You chose an invalid option. Please choose a number between {X}-{Y}")   
                   elif Taken > Row:
                      print (f"LOL! Nice try taking more than whats left! Please try again, but dont take more than {Row} this time!")
                   else:
                      break   
                Row = Row - Taken 
                if Row == 0:
                   print("Player 1 took the final item! Computer wins!!!")
                   break
                currentPlayer="Computer"
               
               else:
                  Taken = random.randint(X,min(Y,Row))
                  print(f"The computer has taken {Taken}!")
                  Row = Row - Taken 
                  if Row == 0:
                   print("Computer took the final item! Player 1 wins! GOOO HUMANS!!!")
                   break
                  currentPlayer="Player 1"
            
      else:
         print("OOOPS! you entered an invalid choice! Please try again!") 

   
    elif Choice=="R":
       Rules()
       
    
    elif Choice=="Q":
       print ("BYE BYE NOW! Hope to see you soon!")
       break

    else:
       print("OOOPS! Your option was invalid! Please try again")
       



if __name__=="__main__":
    main()

