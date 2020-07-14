# This is the module for intro to python's final project!

###################

# Class section

###################

class Welders:
    def __init__ (self, Name = 'Nameless', Type = "None", Wire_lbs = 0, Num_sticks = 0, Wire_type = 'None', Type_sticks = 'None'): 
        self.Welder_name = Name
        self.Welder_type = Type
        self.lbs_Wire = Wire_lbs
        self.Qty_Sticks = Num_sticks
        self.type_Wire = Wire_type
        self.Sticks_Type = Type_sticks
        if self.lbs_Wire < 0:
            raise ValueError ("\nLb's of weld wire must not be less than 0.")
        if self.Qty_Sticks < 0:
            raise ValueError ("\nNumber of welding rods must not be less than 0.")


    def __str__(self):
        return ("\n\nWelder name: " + self.Welder_name + "\nWelder type: " + self.Welder_type + "\nLbs of wire: " + str(self.lbs_Wire) + "\nType of wire: " + self.type_Wire + "\nNumber of Sticks: " + str(self.Qty_Sticks) + "\nType of sticks: " + self.Sticks_Type + "\n\n")

    def __repr__(self):
        return ("\n\nWelder name: " + self.Welder_name + "\nWelder type: " + self.Welder_type + "\nLbs of wire: " + str(self.lbs_Wire) + "\nType of wire: " + self.type_Wire + "\nNumber of Sticks: " + str(self.Qty_Sticks) + "\nType of sticks: " + self.Sticks_Type + "\n\n")

    def Add_Wire(self):
        try:
            wire_added = int(input('How many pounds of wire would you like to add? \n>'))
            if 1 <= wire_added:
                self.lbs_Wire = wire_added
                print('The spool has been changed. There is now ' + str(self.lbs_Wire) + ' lbs available!\n\n')
            else:
                print('At least 1 lb of wire must be added! \n\n')
        except:
            print('Only the numeric representation for how many pounds of wire you wish to add will be accepted.\nExample: 100\n\n')



    def Change_Wire(self):
        newWire = input('What type of wire would you like to use? Example: Flux-core, Dual-Sheild, Solid\n>')
        newWire = newWire.capitalize().strip()
        self.type_Wire = newWire
        self.lbs_Wire = 0
        print('The wire has been changed!\nPlease use the ADD WIRE feature to set the lbs of new wire added.\n\n')


    def Add_Sticks(self):
        try:
            sticks_added = int(input('How many stick electrodes would you like to add? \n>'))
            if 0 < sticks_added:
                self.Qty_Sticks = self.Qty_Sticks + sticks_added
                print('You now have ' + str(self.Qty_Sticks) + ' electrodes available. \n\n')
            else:
                print('At least 1 stick must be added! \n\n')
        except:
            print('Only the numeric representation for how many sticks you wish to add will be excepted.\nExample: 10\n\n')

    def Change_Sticks(self):
        newSticks = input("What type of stick electrodes are you using now? Example: E6011, E7018 \n>")
        newSticks = newSticks.capitalize()
        self.Sticks_Type = newSticks
        self.Qty_Sticks = 0
        print("The sticks have been changed!\nPlease use the ADD STICKS feature to set the number of new sticks you currently have.\n\n")

    def Remove_Wire(self):
        self.lbs_Wire = 0
        self.type_Wire = 'None'
        print('The wire has been removed from this machine! \n\n')

    def Return_sticks(self):
        self.Qty_Sticks = 0
        self.Sticks_Type = 'None'
        print("The sticks have been put back in the rod oven or there respective case! \n\n")


###############

# Other

###############


def main_menu():
    print('MAIN MENU')
    print('Please select an option:')
    print('NEW WELDER')
    print('REMOVE WELDER')
    print('ADD WIRE')
    print('CHANGE WIRE TYPE')
    print('REMOVE WIRE')
    print('ADD STICKS')
    print('CHANGE STICKS')
    print('RETURN STICKS')
    print('PRINT ALL')
    print('PRINT SELECTION')
    print('EXIT')
    return