import socket
import pickle

FORMAT = 'utf-8'
CLIENT = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (CLIENT, PORT)
HEADER=1024
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)
def main():
    def send(msg):
        serial = pickle.dumps(msg)
        client.send(serial)
        print(serial)
        print(client.recv(HEADER))
        
    text_input=bytes(input("Texto a ingresar:\n"), FORMAT)
    while text_input != b"exit":
        send(text_input)
        text_input = bytes(input("Digite comando:\n"),FORMAT)
    if text_input == b"exit":
        send(b'Disconnect')
        client.close()
if __name__ == '__main__':
    main()