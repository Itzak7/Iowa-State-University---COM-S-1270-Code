
# Isaac Aguilar            11/13/2025
# Assignment #5 ultimateTODO 

# In this Code users have access to the ultimate ToDo Planner, where they will have the 3 main options: View List, create a new list, or quit.
# Once in a list, users will have the option to input a todo they wish to accomplish. Once inputed the todo will be stored in the "Backlog".
# Once in the backlog users will be able to move it to decending catagories or delete it once they've completed said todo. Memory of List will be saved
# and carried across sessions. Hope you have fun!

import sys
import pickle

def printTitleMaterial():
    """Prints the title material for the game, including the student's name, class, and section number.
    """
    print("The Ultimate TODO List!")
    print()
    print("By: Isaac Aguilar")
    print("[COM S 127 (4)]")
    print()

def initList():
    """Create a Dictionary of Lists - this is the primary data structure for the script.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList

def checkIfListEmpty(todoList):
    """This function checks if there are any entries in the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean: If there is at least one item in the data structure, return False - it is not empty. Otherwise return True.
    """
    if (len(todoList["backlog"]) > 0 or 
        len(todoList["todo"]) > 0 or
        len(todoList["in_progress"]) > 0 or
        len(todoList["in_review"]) > 0 or
        len(todoList["done"]) > 0):
        return False
    return True

def saveList(todoList):
    """Allows the user to save their data to a binary file.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

def loadList():
    """Allows the user to load their data from a binary file.

    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    
    return todoList

def checkItem(item, todoList):
    """This function iterates through all the keys in the dictionary, and checks each list to see if a key is present.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, String, Integer: This function returns True/ False depending on whether the item was found, the String of the keyName, and the index in the list where the item was found.
    """
    itemFound = False
    keyName = ""
    index = -1
    for i in todoList:
        CurrenetList = todoList[i]
        if item in CurrenetList:
            itemFound = True
            keyName = i 
            index = CurrenetList.index(item)
            break
    return itemFound, keyName, index

def addItem(item, toList, todoList):
    """This function allows the user to add an item to a specific list in the todoList data structure.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    """
    itemFound, Keyname, Index = checkItem(item,todoList) 
    if itemFound == True:
            print(f"OOOPS! Your item: {item} is already in the list! it was found at {Keyname} and its position was {Index}")
    else:
        todoList[toList].append(item)
    return todoList


def deleteItem(item, todoList):
    """This function allows the user to delete an item in the todoList data structure.

    :param String item: The String to search for in each list.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Boolean, Dictionary of Lists: This function returns True/ False depending on whether the item was found, and the modified Dictionary of Lists data structure.
    """
    
    itemFound, Keyname, index = checkItem(item, todoList)
    if itemFound == False:
        print(f"OOOPS! Your task:{item} was nowhere to be found!")
    else:
        todoList[Keyname].remove(item)
    return itemFound, todoList



def moveItem(item, toList, todoList):
    """This function allows the user to move an item from one List in the Dictionary of Lists to another.

    :param String item: The String to search for in each list.
    :param String toList: The key in the dictionary whose list to add the item to.
    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
    itemFound, todoList = deleteItem(item, todoList)
    if itemFound == False:
        return todoList 
    else:
        todoList= addItem(item, toList, todoList)
    return todoList

def printTODOList(todoList):
    """This function prints out the contents of the Dictionary of Lists data structure.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return None: After printing out the contents of the Dictionary of Lists data structure, we are explicitly returning 'None.'
    """
    for keys in todoList: 
        X = todoList[keys]
        print(f"{keys}:{X}")
    return None

def runApplication(todoList):
    """This function provides the primary funcionality for the application. It allows the user to add items to the data structure, move items,
    delete items, save the data structure to a binary file, and return to the main menu.

    :param Dictionary of Lists todoList: A dictionary whose keys contain the various categories the user can access. The values are lists the user can modify.
    :return Dictionary of Lists: This function returns the modified Dictionary of Lists data structure.
    """
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()

        if choice == "a":
            item = input("What ToDo Task would you like to add to the list?: ")
            todoList = addItem(item,'backlog',todoList)
            printTODOList(todoList)

        elif choice == "m":
            X = checkIfListEmpty(todoList) 
            if X == True: 
                print("OOOPS! There is nothing in your list to move!") 
            
            else:
                item = input("What ToDo Item would you like to move?: ")
                itemFound, keyName, index = checkItem(item, todoList)
                
                while itemFound == False:
                    print("OOOPS! that task you entered does not exist anywhere! Please try again!")
                    item = input("What ToDo task would you like to move?: ")
                    itemFound, keyName, index = checkItem(item, todoList)
                toList = input("Which list would you like to move this ToDo to?: ")
                
                while toList not in todoList:
                    print("OOOPS! Your List does not exist! Please try again!")
                    toList = input("Please Enter a list!(a real one this time): ")
                todoList = moveItem(item, toList, todoList)
                printTODOList(todoList)

        elif choice == "d":
            Y = checkIfListEmpty(todoList)
            if Y == True:
                print("UH OH! There are no items to delete!")
            else:
                ItemDel= input("Which ToDo item do you wish to delete?: ")
                itemFound, todoList = deleteItem(ItemDel, todoList)
            printTODOList(todoList)
            
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList

def main():
    """This is the main() function for the program. It contains all of the initial choices the user can make. These choices include:
    - Starting a new Dictionary of Lists.
    - Loading a previously saved Dictionary of Lists.
    - Quitting the script altogether.
    """
    taskOver = False

    printTitleMaterial()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()