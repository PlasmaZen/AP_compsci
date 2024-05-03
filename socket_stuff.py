# cant do this on school computer because it has to open a port through the firewall

import socket

s = socket.socket()

print('Socket created - {}' .format(s))

port = 40674

s.bind(('', port))
print('Socket binded to {}' .format(port))

s.listen(5)
print('Socket is listening')

while  True:
    c, addr = s.accept()
    print('Got connection from', addr)

    c.send(b'thank you for connecting')

    c.close()