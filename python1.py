from tkinter import *
import os
import random
import string
import tkinter

print("The database")

database = []

def addPerson():
    text_file = open("database.txt" , "a")
    personID = (random.choice(string.ascii_letters)) + str(random.randint(1,999))
    personID.upper()
    print("The ID is:", personID.upper())
    firstName = input("\nPlease enter your first name: ")
    lastName = input("\nPlease enter your last name: ")
    phoneNumber = input("\nPlease enter your phone number: ")
    hourlyWage = float(input("\nPlease enter your hourly wage: "))
    database.append(personID)
    database.append(firstName)
    database.append(lastName)
    database.append(phoneNumber)
    database.append(hourlyWage)
    text_file.write(personID + "," + firstName + "," + lastName + "," + phoneNumber + "," + str(hourlyWage) + "\n")
    text_file.close

def listRecords():
    print ("PersonID" + "\t\t" + "First Name" + "\t\t" + "Last Name" + "\t\t" + "Phone Number"+ "\t\t" + "Hourly Wage" + "\t\t")
    text_file = open("database.txt", "r")
    
    text = " "
    while(text):
        text = text_file.readline()
        text2 = text.split(",")
        if len(text) > 0:
            print(text2[0]+ "\t\t"+ "\t"+ text2[1]+ "\t\t\t"+ text2[2]+ "\t\t\t"+ text2[3] + "\t\t\t"+ text2[4])
    
    text_file.close
        
def searchRecord():
     record = input("Please enter the ID of person: ")
     print ("PersonID" + "\t\t" + "First Name" + "\t\t" + "Last Name" + "\t\t" + "Phone Number"+ "\t\t" + "Hourly Wage" + "\t\t")
     text_file = open("database.txt", "r")
     
     text = " "
     while(text):
        text = text_file.readline()
        text2 = text.split(",")
        if len(text) > 0:
            if record == text2[0]:
                print(text2[0]+ "\t\t"+ "\t"+ text2[1]+ "\t\t\t"+ text2[2]+ "\t\t\t"+ text2[3] + "\t\t\t"+ text2[4])

def deleteRecord():
    record = input("Please enter the ID of the person: ")
    text_file = open("database.txt", "r")
    text_file2 = open("temp.txt", "w")
    
    text = " "
    while(text):
        text = text_file.readline()
        text2 = text.split(",")
        if len(text) > 0:
            if record != text2[0]:
                text_file2.write(text2[0]+ "," + text2[1] +","+ text2[2] +"," + text2[3]+ ","+ text2[4])
     
    text_file.close()
    text_file2.close() 
    os.remove("database.txt")
    os.rename("temp.txt", "database.txt")
    
def updateRecord():
    record = input("Please enter the ID of the person: ")
    text_file = open("database.txt", "r")
    text_file2 = open("temp.txt", "w")
    
    text = " "
    while(text):
        text = text_file.readline()
        text2 = text.split(",")
        if len(text) > 0:
            if record != text2[0]:
                text_file2.write(text2[0]+ "," + text2[1] +","+ text2[2] +"," + text2[3] + ","+ text2[4])
                
            else:
                personID = text2[0] 
                firstName = input("\nPlease enter your first name: ")
                lastName = input("\nPlease enter your last name: ")
                phoneNumber = input("\nPlease enter your phone number: ")
                hourlyWage = float(input("\nPlease enter your hourly wage: "))
                database.append(firstName)
                database.append(lastName)
                database.append(phoneNumber)
                database.append(hourlyWage)
                text_file2.write(personID +","+ firstName + "," + lastName + "," + phoneNumber + "," + str(hourlyWage) + "\n")
    
    text_file.close()
    text_file2.close() 
    os.remove("database.txt")
    os.rename("temp.txt", "database.txt")
    
                
                
             
choice = None
while choice != '0':
    print("""
    Member Menu
    0 - Quit
    1- Add record
    2- Display records
    3- Search for a record
    4- Delete a record
    5- Update a record
    """)

    choice = input("Choice: ")
    print()

    if choice == "0":
        print("\nThe records have been saved")

    elif choice == "1":
        addPerson()
    
    elif choice == "2":
        listRecords()
    
    elif choice == "3":
        searchRecord()
    
    elif choice == "4":
        deleteRecord()
    
    elif choice == "5":
        updateRecord()
