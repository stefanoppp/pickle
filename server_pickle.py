import socket

import subprocess
import pickle
import threading

FORMAT='utf-8'
SERVER=socket.gethostbyname(socket.gethostname())
PORT=5050
ADDR=(SERVER, PORT)
HEADER=1024
serversocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(ADDR)
serversocket.listen()

def client(conn, addr):
    print(f"Nuevo cliente")
    connected=True
    while connected:
        msg=conn.recv(HEADER)       
        message=pickle.loads(msg)
        if message==b"\nDisconnect":    
            connected=False
        else:
            user_input=message.split()
            proceso=subprocess.Popen(user_input, stdout=subprocess.PIPE, universal_newlines=True, stderr=subprocess.PIPE)
            stdout,stderr=proceso.communicate()
            
            failed=pickle.dumps(stderr)
            conn.send(failed)
            output=pickle.dumps(stdout)
            conn.send(output)
        print(f"[{addr}] {message}")
        conn.send(message)
    conn.close()

def run():
    serversocket.listen()
    while True:
        conn,addr=serversocket.accept()
        thread=threading.Thread(target=client, args=(conn, addr))
        thread.run()
if __name__ == '__main__':
   run()