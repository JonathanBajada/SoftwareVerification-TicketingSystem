#!/usr/bin/env python3  #Setting interpreter


#Jonathan Bajada 500798771
#Ryan Woodworth 500752821
#Manuel Oshana   500699021

## This is the frontend of the TIX ticketing system.
## This program when started will read input from AccountFile.txt and eventFile.txt in order to
#  collect the necessary information for the session.
## Once a logout transaction is processed, the program will write the session's transaction history to the file transactionFile.txt 
#  for the backend to further process

## *IMPORTANT*
## Before running, please ensure your environment has python 3.7.5 installed
## This program uses the Numpy Library, which must be installed prior to start. This can be done with the following command in a terminal:
## pip3 install numpy

##To Run: 
# python3 main.py



import numpy as np
from decimal import *
import sys
import os

#TODO: EVENT FILE

#This method takes in a username designated by the user and writes it to the AccountFile.text
def createUser():
    global users
    global dailyTransactions

    code = "01 "
    defaultcredit = "000000.00"
    userAdded = False

    #TODO: Check if current user is admin

    if currentUserInfo["accountType"] == "AA" and currentLogin == True:
        newUser = input("Please enter your desired username: \n")
        if len(newUser) > 15:
            print("Username cannot exceed 15 characters.")
        elif newUser in users:
            print("Sorry, this username is already taken.")
        elif newUser not in users:
            atype = input("Please enter the account type for this user: \n")
            if(atype == "AA"):
                atype = "AA"
                print("Successfully created the user, " + newUser)
                new = np.array([[newUser,atype,defaultcredit]])
                users = np.concatenate((new,users),axis=0)
                userAdded = True
            elif(atype == "FS"):
                type = "FS"
                print("Successfully created the user, " + newUser)
                new = np.array([[newUser,atype,defaultcredit]])
                users = np.concatenate((new,users),axis=0)
                userAdded = True
            elif(atype == "BS"):
                type = "BS"
                print("Successfully created the user, " + newUser)
                new = np.array([[newUser,atype,defaultcredit]])
                users = np.concatenate((new,users),axis=0)
                userAdded = True
            elif(atype == "SS"):
                type = "SS"
                print("Successfully created the user, " + newUser)
                new = np.array([[newUser,atype,defaultcredit]])
                users = np.concatenate((new,users),axis=0)
                userAdded = True
            else:
                print("Sorry that is not a valid option, user creation cancelled")
        
        if userAdded:   #If successfully added, add transaction to daily transaction list
            transaction = str(code + newUser.ljust(15) + " " + atype + " " + defaultcredit)
            dailyTransactions = np.append(dailyTransactions,transaction)
            userAdded = False
    elif currentUserInfo["accountType"] == "BS" and currentLogin == True:
            print("Must be an admin to create an account.")
    elif currentUserInfo["accountType"] == "FS" and currentLogin == True:
            print("Must be an admin to create an account.")
    elif currentUserInfo["accountType"] == "SS" and currentLogin == True:
            print("Must be an admin to create an account.")
    else:
        if currentLogin == False:
            print("Please login!")


#This method verifies the users login credentials
def login():    
    global currentLogin
    global users
    global currentUserInfo

    currentUser = input('Please enter your username to login \n') #Prompt for user to input username *need to add error handling*
    if currentLogin == True:
        print("A user is already logged in, logout before next login")
    elif len(currentUser) > 15:
        print("Username cannot exceed 15 characters.")
    elif currentUser in users:
        print("Successfully logged in as: " + currentUser)
        currentLogin = True

        matching = [s for s in users if currentUser in s]
        currentUserInfo = {
            "username":currentUser,
            "accountType": matching[0][1],
            "credit": matching[0][2]
            }
    elif currentUser not in users:
        print("User does not exist in the system.")

#This function initiates the transaction history to be written to file (transactionFile.txt)
def logout():
    code = "00"
    global currentLogin
    global logo
    if currentLogin == True:
        currentLogin = False
        print("You have successfully logged out")
        logo = 2
        writeTransactions()
    else:
        print("You must first login")
    
    #TODO: Update currentuserinfo

    #TODO: End frontend session
    #TODO: Have backend process all sessions transactions
    #TODO: Read in new account file and event file in preperation for next login

    
#This method deletes users from the system
def delete():
    global users
    global dailyTransactions
    global currentUserInfo
    code = "02 "
    if currentLogin == True and currentUserInfo["accountType"] == "AA":
        deleteUser = input("Enter the username to delete: \n(Warning, deleted accounts cannot be recovered)\n")
        if deleteUser == currentUserInfo["username"]:
            print("Can not delete self")
        elif deleteUser in users:                     #If selected user is real account
            for i in range(len(users) - 1):           
                if users[i,0] == deleteUser:
                   
                    #TODO: Erase events with this user as seller
                    credit = float(users[i,2]) #Format users credit for transaction line
                    credit = '{:0>9}'.format(str("{:.2f}".format(credit)))
                    transaction = str(code + deleteUser.ljust(15) + " " + users[i,1] + " " + credit) #Add transaction to daily transactions list
                    dailyTransactions = np.append(dailyTransactions,transaction)
                    users = np.delete(users, i, 0) #Delete user from users array
            print("Successfully deleted the user," + deleteUser + " \n -------------------------------")
        elif deleteUser not in users:               #If selected user is not real account
            print("User does not exist in the system.") 
    else:
        print("Please login as an admin to use the delete function.")


#This function adds credit to a user
def addCredit():
    code = "06 "
    global users
    global dailyTransactions
    global currentUserInfo
    global creditedTotal
    if currentLogin == True and currentUserInfo["accountType"] == "AA":
        user = input("Enter the name of user to add credit to: \n")
        amount = input("Enter the amount of credit to add: \n")
        if user != "" and amount != "":
            value = int(amount)
            if user in users:  # Check if selected user is a real account
                #TODO: Add check against previous addcredit this session

                if value <= 1000 and value > 0:  # Check if desired credit ammount is within daily add limit
                    if (creditedTotal + value) < 1000:
                        # Iterate through usernames
                        for i in range(len(users[:, :])):
                            if users[i, 0] == user:
                                # Credit stored as string, must convert to manipulate
                                userCredit = float(users[i, 2])
                                userCredit += value
                                # Format and reassign to users array
                                users[i, 2] = str("{:.2f}".format(userCredit))
                                print("Credit added to " + user)

                                transaction = str(
                                    code + user.ljust(15) + " " + users[i, 1] + " " + '{:0>9}'.format(users[i, 2]))
                                dailyTransactions = np.append(
                                    dailyTransactions, transaction)
                                creditedTotal = creditedTotal + value
                    else:
                        print("Amount credited in one session cannot exceed 1000.")
                else:
                    print("Amount of credit cannot exceed 1000 and cannot be negative.")
            else:
                print("User does not exist in the system.")
        else:
            print("Username and/or credit cannot be blank.")

    # Addcredit for standard user adds to their own credit only
    elif currentLogin == True and currentUserInfo["accountType"] != "AA":
        amount = int(input("Enter the amount of credit to add: \n"))

        #TODO: Add check against previous addcredit this session

        amount = int(input("Enter the amount of credit to add: \n"))
        if amount > 0:
            if user in users:  # Check if selected user is a real account
                #TODO: Add check against previous addcredit this session

                if amount <= 1000:  # Check if desired credit ammount is within daily add limit
                    # Iterate through usernames
                    for i in range(len(users[:, :])):
                        if users[i, 0] == user:
                            # Credit stored as string, must convert to manipulate
                            userCredit = float(users[i, 2])
                            userCredit += amount
                            # Format and reassign to users array
                            users[i, 2] = str("{:.2f}".format(userCredit))
                            print("Credit added to " + user)

                            transaction = str(
                                code + user.ljust(15) + " " + users[i, 1] + " " + '{:0>9}'.format(users[i, 2]))
                            dailyTransactions = np.append(
                                dailyTransactions, transaction)
        else:
            print("Username and/or credit cannot be blank.")
    else:
        print("Sorry, you must be logged in to use this function.")

#This method refunds credit to the buyer account and debits the seller account
def refund():
    code = "05 "
    global users
    global dailyTransactions
    global currentUserInfo

    if currentLogin == True and currentUserInfo["accountType"] == "AA":
        buyer = input("Please enter buyer's account name. \n")
        if buyer in users:
            for i in range(len(users)):
                if users[i,0] == buyer:
                    buyerCredit = float(users[i,2])

                    refund = int(input("Please enter refund amount. \n"))
                    if(refund <= 999999) and (refund > 0):
                        
                        
                #TODO: Check that adding the refund to account doesn't exceed credit limit 999999
                        

                        seller = input("Please enter seller's account name. \n")
                        if (buyerCredit + refund) <= 999999:
                            if seller in users:
                                for j in range(len(users)):
                                    if users[j,0] == seller:
                                        if float(users[j,2]) > refund:
                                            credit = str("{:.2f}".format(refund))
                                            buyerCredit += float(refund)
                                            users[i, 2] = str("{:.2f}".format(buyerCredit))
                                            print(buyer + " has been refunded")
                                            print(buyer + " now has " + users[i, 2] + " in their account")

                                            sellerCredit = float(users[j,2])
                                            sellerCredit -= float(refund)
                                            users[j, 2] = str("{:.2f}".format(sellerCredit))
                                            print(seller + " has been debited")
                                            print(seller + " now has " + users[j, 2] + " in their account")

                                            transaction = str(code + buyer.ljust(15) + seller.ljust(15) + '{:0>9}'.format(credit))
                                            dailyTransactions = np.append(dailyTransactions, transaction)
                                        else:
                                            print("Seller does not have enough credit to refund buyer!")
                            else:
                                print("Seller does not exist!")
                        else:
                            print("Buyer has an amount of credit that would be greater than 999,999 after refund completes!")
                    elif refund < 0 or refund == None:
                        print("Refund cannot be a negative number!")
                    else:
                        print("Refund exceeds the maximum amount")
        else:
            print("Buyer does not exist!")
    else:
        print("Please login as an admin to use the refund function.")

#This function allows a user to create a new event
def sell():
    code = "03 "
    global currentLogin
    global currentUserInfo
    global dailyTransactions
    if currentLogin == True and currentUserInfo["accountType"] != "BS":
        eventName = input("Enter the name of the event:\n")
        if type(eventName) != str:
            print("Must be a string")
        elif eventName in events:
            print("Event already exists")
        else:
            try:
                salePrice = float(input("Enter the sale price of each ticket:\n"))
                ticketsAmount = int(input("Please enter the amount of tickets:\n"))

                if eventName == "" or salePrice == "" or ticketsAmount == "":
                    print("There can be no empty fields!")
                elif len(eventName) > 18 or float(salePrice) > 999.99 or float(salePrice) <= 0 or int(ticketsAmount) > 100 or int(ticketsAmount) <= 0:
                    print("Improper input")
                else:
                    transaction = str(code + eventName.ljust(18) + " " + (currentUserInfo["username"]).ljust(16) + '{:0>3}'.format(ticketsAmount) + " " + '{:0>9}'.format(salePrice))
                    dailyTransactions = np.append(dailyTransactions, transaction)
            except ValueError:
                print("Sorry, one of those was not a number")

            

        #TODO: Update event array
    else:
        print("Sorry, but you do not have permission to sell!")


#This function allows a user to buy tickets to an existing event
def buy():
    code = "04 "
    global users
    global currentLogin
    global currentUserInfo
    global dailyTransactions
    global events
    yes = 1

    if currentUserInfo["accountType"] == "SS":
        print("Sellers can not buy")
    elif currentLogin == True:
        eventName = input("Enter the name of the event you wish to purchase tickets to:\n")
        ticketQuantity = input("How many tickets would you like to buy?\n")
        sellerName = input("Please enter the name of the seller:\n")
    
        for i in range(len(events)):
            if (eventName == events[i,0]) and (sellerName == events[i,1]):
                yes = 0
                if int(ticketQuantity) <= int(events[i,2]):
                    if int(ticketQuantity) <= 0:
                        print("Ticket amount must be greater than 0")
                    elif (float(currentUserInfo["credit"]) - (float(events[i,3])*int(ticketQuantity))) < 0:
                        print("Not enough credit")
                    elif currentUserInfo["accountType"] != "AA" and int(ticketQuantity) <= 4:
                        #eventInfo = events[i,0] # [Title, Seller, amount of tickets, price of tickets]
                        confirmation = input("You are purchasing, " + ticketQuantity + " ticket(s) at the price of " + events[i,3] + " per ticket. Type 'yes' if this is correct.\n")
                        if confirmation == "yes":
                            events[i,2] = str( float(events[i,2]) - float(ticketQuantity))
                            print("Thank you for your purchase.")
                            transaction = str(code + eventName.ljust(19) + (events[i,1]).ljust(16) + '{:0>3}'.format(ticketQuantity) + " " + '{:0>9}'.format(events[i, 3]))
                            dailyTransactions = np.append(dailyTransactions, transaction)
                        else:
                            print("Purchase declined.")
                    elif currentUserInfo["accountType"] == "AA":
                        confirmation = input("You are purchasing, " + ticketQuantity + " ticket(s) at the price of " + events[i,3] + " per ticket. Type 'yes' if this is correct.\n")
                        if confirmation == "yes":
                            events[i,2] = str( float(events[i,2]) - float(ticketQuantity))
                            print("Thank you for your purchase.")
                            transaction = str(code + eventName.ljust(19) + (events[i,1]).ljust(16) + '{:0>3}'.format(ticketQuantity) + " " + '{:0>9}'.format(events[i, 3]))
                            dailyTransactions = np.append(dailyTransactions, transaction)
                        else:
                            print("Purchase declined.")
                    else:
                        print("Max tickets you may purchase is 4")
                else:
                    print("Not enough tickets remaining.")
            elif eventName == events[i,0] or sellerName == events[i,1]:
                yes = 0
                print("Error: Invalid seller name.")
        if yes > 0:
            print("Error: Invalid event or seller name.")
    else:
        print("Not logged in")

#Triggers the main menu UI which displays the user options
def mainMenu():
    print("Welcome to the Tix ticketing system, please enter one of the following options.")
    selection = input(" 1. create \n 2. login \n 3. logout \n 4. delete \n 5. sell \n 6. buy \n 7. refund \n 8. addcredit \n 9. quit\n")
    if selection == "create":
        createUser()
    elif selection == "login":
        login()
    elif selection == "logout":
        logout()
    elif selection == "delete":
        delete()
    elif selection == "addcredit":
        addCredit()
    elif selection == "refund":
        refund()
    elif selection == "sell":
        sell()
    elif selection == "buy":
        buy()
    elif selection == "quit":
       global run
       run = False
    elif selection == "r":
        print(users)
    else:
        print("\nSorry but that is not a valid option\n")



#Read current account file; triggered at startup and after backend is finished changes
def readAccounts():         
    file = open(AccountF,"r")
    lines = file.readlines()
    file.close()
    global users

    for i in range(len(lines)):
        line = lines[i]
        username = line[0:15].rstrip(" ")
        status = line[16:18]
        credit = line[19:28].lstrip("0")
        user = [username, status, credit]
        users.append(user)

#Read current events file; triggered at startup and after backend is finished changes
def readEvents():               
    file = open(EventF, "r")
    lines = file.readlines()
    file.close()

    global events
    for i in range(len(lines)):
        line = lines[i]
        title = line[0:18].rstrip(" ")
        seller = line[19:34].rstrip(" ")
        amount = line[35:38].lstrip("0")
        price = line[39:45].lstrip("0")
        event = [title, seller, amount, price]
        events.append(event)


#Write daily transactions; triggered upon logout function
def writeTransactions():        
    global currentUserInfo
    global dailyTransactions
    global logo

    user = currentUserInfo["username"]
    type = currentUserInfo["accountType"]
    credit = currentUserInfo["credit"]
    endLine = str("00 " + user.ljust(15) + " " + type + " " + '{:0>9}'.format(credit))

    f = open(os.getcwd()+TransactionF, "w+")
    for i in range(len(dailyTransactions)):
        f.write(dailyTransactions[i] + "\n")
    if logo == 2:
        f.write(endLine)
    f.close()
    logo = 1


#Global variables
logo = 1
run = True                      #Ensures main program keeps running
currentLogin = False            #Signifies if user is logged in
dailyTransactions = []          #List of transactions during session
users = []                      #Matrix of current sessions user info
events = []                     #Matrix of current sessions events
currentUserInfo = {             #Dictionary of logged in user details
    "username":"",
    "accountType":"",
    "credit":""
}
creditedTotal = 0
if len(sys.argv) < 3:
    AccountF = "AccountFile.txt"
    EventF = "eventFile.txt"
    TransactionF = "transactionFile.txt"
else:
    AccountF = sys.argv[1]
    EventF = sys.argv[2]
    TransactionF = sys.argv[3]

readAccounts()  #Read in account file at start
users = np.asarray(users)

readEvents()    #Read in events file at start
events = np.asarray(events)

while run:  #   Main program loop
    mainMenu()

