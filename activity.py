import socket                   

port = 60000                    
s = socket.socket()             
host = socket.gethostname()     
s.bind((host, port))            
s.listen(5)                    

print ('Server listening....')

while True:
    conn, addr = s.accept()     
    print ('Got connection from'), addr
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()


# client.py

import socket                  

s = socket.socket()             
host = socket.gethostname()     
port = 60000                    
s.connect((host, port))
s.send("Hello server!")

with open('received status', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')

