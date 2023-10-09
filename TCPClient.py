from socket import *

serverName = "localHost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

command = input("Enter a command (Random, Add, Subtract): ")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

sentence = f"{command};{num1};{num2}"
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024).decode()
print("From server: ", modifiedSentence)

clientSocket.close()
