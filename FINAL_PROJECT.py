
# This is the final project for Intro to Python!

#######################

# MAIN PROGRAM BELOW

#######################

import FINAL_PROJECT_MODULE
import pickle

getList = input('Do you have a current list of welders? Type yes or no.\n>')
getList.lower().strip()

currentWelders = []

if getList == 'yes':
    try:
        currentWelders = pickle.load( open ("FINAL_PROJECT-pickle.p", "rb"))
        print('The list has been loaded!\n\n')
    except:
        print('File not found, the program will start with an empty list!')


inputs = ['NEW WELDER', 'REMOVE WELDER', 'ADD WIRE', 'CHANGE WIRE TYPE', 'REMOVE WIRE', 'ADD STICKS', 'CHANGE STICKS', 'RETURN STICKS', 'PRINT ALL', 'PRINT SELECTION', 'EXIT']

userChoice = 'None'

while userChoice != 'EXIT':
    FINAL_PROJECT_MODULE.main_menu()
    userChoice = input('What would you like to do? \n>')
    userChoice = userChoice.upper().strip()

    if userChoice in inputs:
        if userChoice == 'NEW WELDER':
            weldName = input('What is the name of this welding machine?\n>').capitalize().strip()
            weldType = input('What type of machine is this? Example: Stick, MIG\n>').capitalize().strip()
            numWire = int( input('How many lbs of welding wire does this machine have?\n>').strip() )
            numSticks = int( input('How many welding rods does this machine have?\n>').strip() )
            try:
                newWelder = FINAL_PROJECT_MODULE.Welders(weldName, weldType, numWire, numSticks)
                print(newWelder)
                currentWelders.append(newWelder)
                print('This welder has been added to the list!\n\n')
            except ValueError as err:
                print('\n', err)
                print('Unable to create this welder!\n\n')

        elif userChoice == 'REMOVE WELDER':
            userinput = input('Which welder would you liket to remove?\n>').capitalize().strip()
            found = False
            for i in range(len(currentWelders)):
                if currentWelders[i].Welder_name == userinput:
                    currentWelders.remove(currentWelders[i])
                    found = True
                    print('This welder has been removed from the list.\n\n')
                    break
            if found == False:
                print('This welder is not on the list.\n\n')

        elif userChoice == 'ADD WIRE':
            userinput = input('Which welder would you like to add wire to?\n>').capitalize().strip()
            found = False
            for i in range(len(currentWelders)):
                if currentWelders[i].Welder_name == userinput:
                    currentWelders[i].Add_Wire()
                    found = True
            if found == False:
                print('This welder is not on the list.\n\n')

        
        elif userChoice == 'CHANGE WIRE TYPE':
            userinput = input('Which welder would you like to change wire for?\n>').capitalize().strip()
            found = False
            for i in range(len(currentWelders)):
                if currentWelders[i].Welder_name == userinput:
                    currentWelders[i].Change_Wire()
                    found = True
            if found == False:
                print('This welder is not on the list.\n\n')
            
        
        elif userChoice == 'REMOVE WIRE':
            userinput = input('Which welder would you like to remove wire from?\n>').capitalize().strip()
            found = False
            for i in range(len(currentWelders)):
                if currentWelders[i].Welder_name == userinput:
                    currentWelders[i].Remove_Wire()
                    found = True
            if found == False:
                print('This welder is not on the list.\n\n')
        
        elif userChoice == 'ADD STICKS':
            userinput = input('Which welder are you adding sticks to?\n>').capitalize().strip()
            found = False
            for i in range(len(currentWelders)):
                if currentWelders[i].Welder_name == userinput:
                    currentWelders[i].Add_Sticks()
                    found = True
            if found == False:
                print('This welder is not on the list.\n\n')
        
        elif userChoice == 'CHANGE STICKS':
            userinput = input('Which welder would you like to change sticks for?\n>').capitalize().strip()
            found = False
            for i in range(len(currentWelders)):
                if currentWelders[i].Welder_name == userinput:
                    currentWelders[i].Change_Sticks()
                    found = True
            if found == False:
                print('This welder is not on the list.\n\n')
        
        elif userChoice == 'RETURN STICKS':
            userinput = input('Which welder are you returning sticks from?\n>').capitalize().strip()
            found = False
            for i in range(len(currentWelders)):
                if currentWelders[i].Welder_name == userinput:
                    currentWelders[i].Return_sticks()
                    found = True
            if found == False:
                print('This welder is not on the list.\n\n')
        
        elif userChoice == 'PRINT ALL':
            for i in range(len(currentWelders)):
                print(currentWelders[i])
        
        elif userChoice == 'PRINT SELECTION':
            userinput = input('Which welder would you like to print information on?\n>').capitalize().strip()
            found = False
            for i in range(len(currentWelders)):
                if currentWelders[i].Welder_name == userinput:
                    print(currentWelders[i])
                    found = True
            if found == False:
                print('This welder is not on the list.\n\n')
        
        else:
            continue
             


    else:
        print('Please select a valid option.\n\n')
        continue

exitList = ['yes', 'no']
saveList = 'None'

while saveList not in exitList:
    saveList = input('Would you like to save your list? Answer yes or no.\n>').lower().strip()

if saveList == 'yes':
    pickle.dump( currentWelders, open("FINAL_PROJECT-pickle.p", "wb"))
    print('The list has been saved! \nGood-bye!')

else:
    print('Good-bye!')