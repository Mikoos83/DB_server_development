import socketserver

#trimData method: take list as an input and trim leading and trailing spaces in each element
def trimData(list):
    for index in range (0,4):
        list[index] = list[index].strip(" ")
#compareData method: take two variables and compare if they are idential. Used to find if the customer data already exists
def compareData(list1, list2):
    return (list1[0] == list2[0] and list1[1] == list2[1] and list1[2] == list2[2] and list1[3] == list2[3] )

#stringMaker method: create a string by concatenate list elements and "|"
def stringMaker(data):
    name, age, address, phoneNum = data
    return (name+"|"+age+"|"+address+"|"+phoneNum)

#open data.txt file and read the data
my_file = open('data.txt')
raw_data = my_file.readlines()

#Initialization of the list that will save all the tuples
processed_data = []

#trim the data, convert them into tuple ands save it in the list
for data in raw_data:
    #remove escape sequence '\n'
    data = data[0:-1]

    #split the string with the delimiter '|'
    data = data.split('|')

    #if the name field is empty, skip
    if (data[0].isspace()):
        continue

    #remove leading and trailing spaces
    trimData(data)

    #once the data is trimmed, cast them in the tuple and put them in the list
    processed_data.append(tuple(data))

#once it finishes reading data from the file, close the file
my_file.close()


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
            #receive request string from the client and parse it
            self.data = self.request.recv(1024).strip()
            convert_data = str(self.data, "utf-8")
            request = convert_data.split("|")

            #this request will be received when client side starts
            if(request[0] == '0'):
                new_string = ''
                for data in processed_data:
                    new_string += stringMaker(data)+"\n"
                self.request.sendall(bytes(new_string, "utf-8"))

            #menu 1: find customer
            elif (request[0] == '1'):
                data_found = 0
                for data in processed_data:
                    if (data[0] == request[1]):
                        new_string = stringMaker(data)
                        self.request.sendall(bytes(new_string, "utf-8"))
                        data_found = 1
                        break;

                if(data_found == 0):
                    new_message = "Target name not found in the database"
                    self.request.sendall(bytes(new_message, "utf-8"))

            #menu 2: add customer
            elif (request[0] == '2'):
                if(request[1] == '' or request[1].isspace()):
                    error_message = "Name field cannot be empty. Please try again."
                    self.request.sendall(bytes(error_message, "utf-8"))
                else:
                    new_customer_data = request[1:]
                    trimData(new_customer_data)
                    data_found = 0
                    for data in processed_data:
                        if(compareData(data, new_customer_data)):
                            error_message = "Customer already exsits."
                            self.request.sendall(bytes(error_message, "utf-8"))
                            data_found = 1
                            break;
                    if (data_found == 0):
                        processed_data.append(tuple(new_customer_data))
                        new_message = stringMaker(new_customer_data)+" successfully added"
                        self.request.sendall(bytes(new_message, "utf-8"))

            #menu 3: delete customer
            elif (request[0] == '3'):
                data_found = 0
                for data in processed_data:
                    if (data[0] == request[1]):
                        index = processed_data.index(data)
                        processed_data.pop(index)
                        new_message = "Customer data successfully deleted"
                        self.request.sendall(bytes(new_message, "utf-8"))
                        data_found = 1
                        break
                if(data_found == 0):
                    error_message = "Customer information does not exist"
                    self.request.sendall(bytes(error_message, "utf-8"))

            #menu 4: Update customer age
            elif (request[0] == '4'):
                data_found = 0
                for data in processed_data:
                    if (data[0] == request[1]):
                        x = processed_data.index(data)
                        data = list(data)
                        data[1] = request[2]
                        data = tuple(data)
                        processed_data[x] = data
                        new_message = request[1]+"'s age has been updated to "+data[1]
                        self.request.sendall(bytes(new_message, "utf-8"))
                        data_found = 1
                        break
                if(data_found == 0):
                    error_message = "Customer information does not exist"
                    self.request.sendall(bytes(error_message, "utf-8"))

            #menu 5: Update customer address
            elif (request[0] == '5'):
                data_found = 0
                for data in processed_data:
                    if (data[0] == request[1]):
                        x = processed_data.index(data)
                        data = list(data)
                        data[2] = request[2]
                        data = tuple(data)
                        processed_data[x] = data
                        new_message = request[1]+"'s address has been updated to "+data[2]
                        self.request.sendall(bytes(new_message, "utf-8"))
                        data_found = 1
                        break
                if(data_found == 0):
                    error_message = "Customer information does not exist"
                    self.request.sendall(bytes(error_message, "utf-8"))

            #menu 6: Update customer phone number
            elif (request[0] == '6'):
                data_found = 0
                for data in processed_data:
                    if (data[0] == request[1]):
                        x = processed_data.index(data)
                        data = list(data)
                        data[3] = request[2]
                        data = tuple(data)
                        processed_data[x] = data
                        new_message = request[1]+"'s phone number has been updated to "+data[3]
                        self.request.sendall(bytes(new_message, "utf-8"))
                        data_found = 1
                        break
                if(data_found == 0):
                    error_message = "Customer information does not exist"
                    self.request.sendall(bytes(error_message, "utf-8"))

            #menu 7: Print database on client side
            elif (request[0] == '7'):
                new_string = ''
                sorted_data = sorted(processed_data, key = lambda x: x[0])
                for data in sorted_data:
                    new_string += stringMaker(data)+"\n"
                self.request.sendall(bytes(new_string, "utf-8"))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
