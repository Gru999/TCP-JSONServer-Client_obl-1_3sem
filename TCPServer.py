import threading
from socket import *
import random
import json

serverName = "localhost"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

def handleClient(connectionSocket, address):
    data = connectionSocket.recv(1024).decode()
    print(f"Received: {data}")

    try:
        request = json.loads(data)
        if "method" in request:
            method = request["method"]
            if method == "Random":
                if "num1" in request and "num2" in request:
                    num1 = request["num1"]
                    num2 = request["num2"]
                    result = str(random.randint(num1, num2))
                else:
                    result = "Missing 'num1' or 'num2' in JSON request"
            elif method == "Add":
                if "num1" in request and "num2" in request:
                    num1 = request["num1"]
                    num2 = request["num2"]
                    result = str(num1 + num2)
                else:
                    result = "Missing 'num1' or 'num2' in JSON request"
            elif method == "Subtract":
                if "num1" in request and "num2" in request:
                    num1 = request["num1"]
                    num2 = request["num2"]
                    result = str(num1 - num2)
                else:
                    result = "Missing 'num1' or 'num2' in JSON request"
            else:
                result = "Invalid method in JSON request"
        else:
            result = "Missing 'method' in JSON request"

    except json.JSONDecodeError:
        result = "Invalid JSON format"

    response = {"result": result}
    connectionSocket.send(json.dumps(response).encode())
    connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Client connected")
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()

