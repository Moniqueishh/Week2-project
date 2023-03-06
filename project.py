# Your parking gargage class should have the following methods:
# - takeTicket***METHOD***
# - This should decrease the amount of tickets available by 1

#CREATING A CLASS

class parkingGarage():
    def __init__(self,tickets,parkingSpaces,currentTicket): #Self refers back to the class up there
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

#CREATING A METHOD-

# -1 ticket/space from list
    def takeTicket(self): 
        self.tickets.pop()
        self.parkingSpaces.pop()
           

    def payForParking(self):
        # x = input("Please enter the amount you would like to pay >> ")
        # while x == "":
        #     input("Please enter an amount>>> ")
        #     if x != "":
        print("Your ticket has been paid and you have 15 mins to leave")
        # self.tickets.append()
        self.currentTicket["paid"] = True

    def leaveGarage(self):

        # print("Thank you, have a nice day!")
        # self.currentTicket["paid"] = True
        # print("Thank you, have a nice day!")
        if self.currentTicket["paid"] == True:
                self.parkingSpaces.append("space")
                self.tickets.append("ticket")
                print("Thank you, have a nice day!")
        else: 
            while True:
                x = input("Please enter amount for unpaid ticket >> ")
                if x != "":
                    self.currentTicket["paid"] == True
                    self.parkingSpaces.append("space")
                    self.tickets.append("ticket")
                    print("Thank you, have a nice day!")
                    break
       


        # while True:
        #         x = input("Please enter amount for unpaid ticket >> ")
        #         if x:
        #             self.currentTicket["paid"] == True
        #         else:
        #         # spaces.currentTicket["paid"] #accessing the correct thing!!***
        #             print("Thank You, have a nice day")
        #             break
        # Check if ticket has been paid--- elf.currentTicket
        #     If True print("Thank You, have a nice day")
        # if False LOOP input("Please enter amount for unpaid ticket") then once paid, print("Thank You, have a nice day!")
        #     self.tickets.append("space")
        #     self.parkingSpaces.append("ticket")
        


#Show spaces available-
    def showSpaces(self):
        print("Available spaces: ")
        for i in self.parkingSpaces:
            print(i) 


#CALLING

spaces = parkingGarage(["ticket","ticket","ticket"], ["space","space","space"],{"paid":False})

def take():  
     while True:
             
        resp = input("What would you like to do? 'S' to show available spaces, 'G' to get a ticket, 'L' to leave, 'Q' to quit. >> ")
        if resp.lower() == "q":
            # spaces.showSpaces() #to show the available spaces when they q- optional 
            print("Later alligator!!!")
            break
            
        elif resp.lower() == "s":
            spaces.showSpaces()

        elif resp.lower() == "g":
            while True:
                x = input("Please enter the amount you would like to pay >> ")
                if x:
                    spaces.payForParking() #Prints they've paid & changes paid = True
                    spaces.takeTicket() #removes space/ticket- unavailable 
                    break

        elif resp.lower() == "l":
            # while True:
            #     x = input("Please enter amount for unpaid ticket >>  ")
            #     if x:
            #         spaces.leaveGarage()
            #         break
            # break
            # if spaces.currentTicket["paid"] == True:
            #     print("Thank you, have a nice day!")
            # else: 
            #     while True:
            #        x = input("Please enter amount for unpaid ticket >> ")
            #        if x != "":
            #         spaces.currentTicket["paid"] == True
                    spaces.leaveGarage()
                    print(spaces.parkingSpaces) #Check if it adds a space back to list
                    print(spaces.tickets) #Check if it adds a ticket back to list 
                    break

                    # print("Thank you, have a nice day!")
                    # spaces.parkingSpaces.append("space")
                    # spaces.tickets.append("ticket")
                    

            # while True:
            #     if spaces.currentTicket["paid"] == False:
            #        x = input("Please enter amount for unpaid ticket >> ")
            #        if x == "":
            #         spaces.currentTicket["paid"] == True
            #         # spaces.currentTicket["paid"] #accessing the correct thing!!***
            #         print("Thank You, have a nice day")
        # break
        print(spaces.currentTicket) #Checks paid status T/F          
take()


# -leaveGarage***METHOD***
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary


