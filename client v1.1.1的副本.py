import socket as s
Header=64
port=int(input('port input\n'))
Format='UTF-8'
disconnect_message='disconnect'
server=int('161.117.255.50')
addr=(server,port)
client=s.socket(s.AF_INET,s.SOCK_STREAM)
client.connect(addr)
def send(msg):
    message=msg.encode(Format)
    msgg=len(message)
    sendle=str(msgg).encode(Format)
    sendle+=b' '*(Header-len(sendle))
    client.send(sendle)
    client.send(message)
    print(client.recv(1412))
def recive(mss):
    mss=conn.recv(Header).decode(Format)
    if mss:
        mss=int(mss)
        msss=conn.recv(mss).decode(Format)
        print(f"{msss}")
send(input('enter message\n'))
send(disconnect_message)
