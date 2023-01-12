#import socket and sys to do client-server connection
import socket
import sys

HOST, PORT = "localhost", 9999

#this is to print the current database on the client side
choice = '0'
print("**Welcome to Python DB**\n")
print("\t<Current Database>")
print("------------------------------")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(choice+"|", "utf-8"))
    received = str(sock.recv(1024), "utf-8")
    print(received)
print("------------------------------")

#This loop is to keep the program going on until the user wants to quit (press 8)
while (choice != '8'):


    print("==============================")
    print("\n\tPython DB Menu\n")
    print("==============================")
    print("1. Find Customer")
    print("2. Add Customer")
    print("3. Delete Customer")
    print("4. Update Customer Age")
    print("5. Update Customer Address")
    print("6. Update Customer Phone Number")
    print("7. Print Report")
    print("8. Exit")

    choice = input("Select: ")

    #menu 1 Find customer
    if (choice == '1'):
        print("\n\t<Find Customer>")
        print("------------------------------")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            target_name = input("Please input the customer name: ")
            sock.sendall(bytes(choice+"|"+target_name, "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print("\n"+received+"\n")
        print("------------------------------")

    #menu 2 Add customer
    elif (choice == '2'):
        print("\n\t<Add Customer>")
        print("------------------------------")
        print("Please input new customer information: ")
        add_name = input("Name: ")
        add_age = input("Age: ")
        add_address = input("Address: ")
        add_phone = input("Phone number: ")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall(bytes(choice+"|"+add_name+"|"+add_age+"|"+add_address+"|"+add_phone, "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print("\n"+received+"\n")
        print("------------------------------")

    #menu 3 Delete customer
    elif (choice == '3'):
        print("\n\t<Delete Customer>")
        print("------------------------------")
        print("Please input the name of the customer you wish to delete: ")
        delete_name = input("Name: ")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall(bytes(choice+"|"+delete_name, "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print("\n"+received+"\n")
        print("------------------------------")

    #menu 4 Update customer age
    elif (choice == '4'):
        print("\n\t<Update Customer Age>")
        print("------------------------------")
        print("Please input the name of the customer you wish to update: ")
        target_name = input("Name: ")
        target_age = input("Age: ")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall(bytes(choice+"|"+target_name+"|"+target_age, "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print("\n"+received+"\n")
        print("------------------------------")

    #menu 5 Update customer address
    elif (choice == '5'):
        print("\n\t<Update Customer Address>")
        print("------------------------------")
        print("Please input the name of the customer you wish to update: ")
        target_name = input("Name: ")
        target_address = input("Address: ")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall(bytes(choice+"|"+target_name+"|"+target_address, "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print("\n"+received+"\n")
        print("------------------------------")

    #menu 6 Update customer phone number
    elif (choice == '6'):
        print("\n<Update Customer Phone Number>")
        print("------------------------------")
        print("Please input the name of the customer you wish to update: ")
        target_name = input("Name: ")
        target_phone = input("Phone Number: ")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall(bytes(choice+"|"+target_name+"|"+target_phone, "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print("\n"+received+"\n")
        print("------------------------------")

    #menu 7 print report
    elif (choice == '7'):
        print("\n\t<Print Report>")
        print("------------------------------")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall(bytes(choice, "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print("\n"+received+"\n")
        print("------------------------------")

    #menu 8 exit
    elif (choice == '8'):
        print("**Thank you for using this program**")

    #exception handling
    else:
        print("Please try again");

#close socket before terminate the program
sock.close()
