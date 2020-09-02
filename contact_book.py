# this is program of contact book

#this function will display the choices user will have
def menu():
    print("\n1-Add new contact\n2-Delete contact\n3-Update info to existing contact\n4-Info of eisting contact\n5-Show all contacts\n6-Exit\n")

def add_new():                               # This function will ahelp the user to add a new contact
     
    file = open("contactbook.txt", "a")
    contact_name = input("Contact name:-")
    file.write(contact_name+" ")
    phn_no = input("Phone number:-")
    file.write(phn_no+" ")
    email_ = input("Email id:-")
    file.write(email_+"\n")
    file.close()
    print("Contact added sucessfully!!\n")

def del_contact():                                 # This function will delete the contact from contact book
    
    name = input("Enter name of the contact:-")
    flag = 0
    file = open("contactbook.txt", "r")
    data = file.readlines()
    file = open("contactbook.txt","w")
    for line in data:
        word = line.split()
        if word[0] != name:
            file.write(line)
        else:
            flag = 1

            # Flag unit will decide whether contact exist in contact book or not
            
    if flag == 1:
        print("Deleted sucessfully!!")
    else:
        print("Contact not found")
    file.close()
        
""" This function will update the information
        inti existing contact """

def update_contact():
    
    name = input("Enter the name of contact:-")
    file = open("contactbook.txt","r")
    data = file.readlines()                       # assigining all the contents line by line into data from file
    file = open("contactbook.txt","w")
    flag = 0
    for line in data:
        word = line.split()                             # Splitting every line into list name word
        if word[0] != name:
            file.write(line)
        else:
            flag = 1
            edit = input("0 for edit name, 1 for edit number and 2 for edit email:-")
            if edit == "0":
                word[0] = input("Enter new name:-")
            elif edit == "1":
                word[1] = input("Enter new number:-")
            elif edit == "2":
                word[2] = input("Enter new email id:-")
            else:
                print("Invalid option, Try again....!!")
                update_contact()
            print(word)
            line = " ".join(word)
            print(line)
            file.write(line)
        print("updated sucessfully") if flag == 1 else print("Contact not found")
    file.close()

def info():                                             # This function will show the information of existing contact
    
    name = input("Enter name of the contact:-")
    file = open("contactbook.txt","r")
    data = file.readlines()
    flag = 0
    for line in data:
        word = line.split()
        if word[0] == name:
            flag = 1
            print("Contact name:- ",word[0])
            print("Contact number:- ", word[1])
            print("Contact email id:- ", word[2])
            break
    if flag == 0:
        print("Contact not found")
    file.close()

def all_contacts():                                 # This function shows all the contacts present in contact list
    
    length = count_()
    print("{0} contacts are present in contact book".format(length))
    file = open("contactbook.txt", "r")
    data = file.readlines()
    for line in data:
        word = line.split()
        print("Contact name:- ",word[0])
        print("Contact number:- ",word[1])
        print("Contact email id:- ",word[2])
    file.close()

def count_():                                    # count_ will return the number of contacts present in contact book
    
    file = open("contactbook.txt","r")
    count = 0
    data = file.readlines()
    for items in data:
        count += 1
    file.close()
    return count
    
flag = True
while flag:                                                # main of code 
    menu()
    choice = int(input("Enter your chocie:-"))
    if choice == 1:
        add_new()
    elif choice == 2:
        del_contact()
    elif choice == 3:
        update_contact()
    elif choice == 4:
        info()
    elif choice == 5:
        all_contacts()
    elif choice == 6:
        print("Exit sucessfully....!!!1")
        flag = False
    else:
        print("Invalid input !! \nTry again...")
