import serial
import time

from subprocess import call

locations=['/dev/ttyUSB0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3',
'/dev/ttyS0','/dev/ttyS1','/dev/ttyS2','/dev/ttyS3']  

def sayPhrase(phrase):
    commandLine="/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols \"http://translate.google.com/translate_tts?tl=en&q="+ phrase + "\""
    #print commandLine
    call(commandLine,shell=True)
    


# connect on the serial port
for device in locations:  
    try:  
        print "Trying...",device
        arduino = serial.Serial(device, 9600) 
        break
    except:  
        print "Failed to connect on",device   


while 1:


    try:
        arduino.write('Y')
        time.sleep(1)
        x = arduino.readline()
        x=x.replace(";","")
        x=x.replace(":"," ")
        xs= x.split()
        if xs[0]=='temp':
            temp=float(xs[1])
            print temp

    except:
        print "Failed to communicate!"
        time.sleep(1)

