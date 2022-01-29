import json
import socket as s
import threading as t
HEADER=64
lis=[]
Format='utf-8'
port=int(input('port\n'))
chang='change'
SERVER=s.socket(s.AF_INET,s.SOCK_STREAM)
server=float(input("server adress"))
addra=(server,port)
disconnect_message='disconnect'
store='storage'
SERVER.bind(addra)
def handclient(conn,addra):
    print(f"[new connection]{addra}connected.")
    connected=True
    while connected:
        msg=conn.recv(HEADER).decode(Format)
        if msg:
            msg=int(msg)
            msgg=conn.recv(msg).decode(Format)
            if msgg==disconnect_message:
                connected=False
            if msgg==store:
                def send(msg):
                    message=msg.encode(Format)
                    msgg=len(message)
                    sendle=str(msgg).encode(Format)
                    sendle+=b' '*(Header-len(sendle))
                    server.send(sendle)
                    server.send(message)
                    print(server.recv(1412))
                send(lis)
            if msgg == chang:
                port=int(input('pls insert new port\n'))
                print('successfuly changed port')
            lis.append(msgg)
            with open('cloud 01','w'):
                deta=dict(lis)
                json.dumps(deta)
            print(f"{[addra]} {msgg}")
            conn.send('recived message'.encode(Format))
            conn.close()
def start():
    with open('cloud 01','r') as j:
        data=json.loads(j)
        dat=list(data.values())
        lis=dat
    server.listen()
    print(f"[listening]on {server}")
    while True:
        conn,addra=server.accept()
        thread=threading.Thread(target=handclient,arg=(conn,addra))
        thread.start()
        print(f"[active connections]{threading.activeCount()-1}")
    print('server is starting...')
start()

