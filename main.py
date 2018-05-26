from uconnect import uConnect
#from ufirebase import uFirebase
#-import searchh
cn = uConnect()
cn.wlan_manual()
#--searchh.verf()
import socket 
import machine
#HTML to send to browsers

html = open("index.html",'r').read()

print html

#Setup PINS
LED0 = machine.Pin(0, machine.Pin.OUT)
LED2 = machine.Pin(2, machine.Pin.OUT)

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    LEDON0 = request.find('/?LED=ON0')
    LEDOFF0 = request.find('/?LED=OFF0')
    LEDON2 = request.find('/?LED=ON2')
    LEDOFF2 = request.find('/?LED=OFF2')
    #print("Data: " + str(LEDON0))
    #print("Data2: " + str(LEDOFF0))
    if LEDON0 == 6:
        print('TURN LED0 ON')
        LED0.off()
    if LEDOFF0 == 6:
        print('TURN LED0 OFF')
        LED0.on()
    if LEDON2 == 6:
        print('TURN LED2 ON')
        LED2.off()
    if LEDOFF2 == 6:
        print('TURN LED2 OFF')
        LED2.on()
    response = html
    conn.send(response)
    conn.close()