from socket import *
import json

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

method = input("Enter the method (Random, Add, Subtract): ")

if method not in ["Random", "Add", "Subtract"]:
    print("Invalid method. Please enter 'Random', 'Add', or 'Subtract'.")
else:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        request = {
            "method": method,
            "num1": num1,
            "num2": num2
        }

        
        print("Sending JSON request: ", json.dumps(request))

        clientSocket.send(json.dumps(request).encode())

        data = clientSocket.recv(1024).decode()
        response = json.loads(data)
        print("Result:", response["result"])

    except ValueError:
        print("Invalid input. Please enter valid integer numbers.")

clientSocket.close()
