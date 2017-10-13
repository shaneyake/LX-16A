from time import sleep
from serial import Serial

Serial_Con = Serial("/dev/tty.wchusbserial1410", baudrate=115200, timeout=0.001)
Serial_Con.setDTR(1)
dictErrors = {  1 : "Input Voltage",
                2 : "Angle Limit",
                4 : "Overheating",
                8 : "Range",
                16 : "Checksum",
                32 : "Overload",
                64 : "Instruction"
        }

AX_START=0x55
TX_DELAY_TIME = 0.00002

def moveServo(id,speed,position):
    #print("Moving Servo ID:"+str(id)+"----------------------")
    AX_REG_WRITE =1
    AX_GOAL_SP_LENGTH =7
    if(position < 0):
        position = 0
    if(position > 1000):
        position = 1000
    if(speed < 0):
        speed = 0
    if(speed > 30000):
        speed = 30000

    p = [position&0xff, position>>8]
    s = [speed&0xff, speed>>8]
    checksum = (~(id + AX_GOAL_SP_LENGTH + AX_REG_WRITE + p[0] + p[1] + s[0] + s[1]))&0xff
    outData = chr(AX_START)
    #print(hex(ord(chr(AX_START))))
    outData += chr(AX_START)
    #print(hex(ord(chr(AX_START))))
    outData += chr(id)
    #print(hex(ord(chr(id))))
    outData += chr(AX_GOAL_SP_LENGTH)
    #print(hex(ord(chr(AX_GOAL_SP_LENGTH))))
    outData += chr(AX_REG_WRITE)
    #print(hex(ord(chr(AX_REG_WRITE))))
    outData += chr(p[0])
    #print(hex(ord(chr(p[0]))))
    outData += chr(p[1])
    #print(hex(ord(chr(p[1]))))
    outData += chr(s[0])
    #print(hex(ord(chr(s[0]))))
    outData += chr(s[1])
    #print(hex(ord(chr(s[1]))))
    outData += chr(checksum)
    #print(hex(ord(chr(checksum))))
    Serial_Con.write(outData)
    sleep(TX_DELAY_TIME)
    return True
#print("Done -----------")

def ReadTemp(id):
    #print("Read Temp ID:"+str(id)+"-------------")
    AX_READ_DATA=3
    AX_TEMP_READ=26
    Serial_Con.flushInput()
    checksum = (~(id + AX_READ_DATA + AX_TEMP_READ))&0xff
    outData = chr(AX_START)
    #print(hex(ord(chr(AX_START))))
    outData += chr(AX_START)
    #print(hex(ord(chr(AX_START))))
    outData += chr(id)
    #print(hex(ord(chr(id))))
    outData += chr(AX_READ_DATA)
    #print(hex(ord(chr(AX_READ_DATA))))
    outData += chr(AX_TEMP_READ)
    #print(hex(ord(chr(AX_TEMP_READ))))
    outData += chr(checksum)
    #print(hex(ord(chr(checksum))))
    Serial_Con.write(outData)
    sleep(TX_DELAY_TIME)
    #print("Done -----------")
    count=0
    sleep(0.1)
    while count<200:
        reply=Serial_Con.read(1)
        if reply != '':
            for x in range(0, 7):
                if x == 5:
                    #print reply.encode("hex")
                    #print str(int(reply.encode("hex"),16))+"*C"
                    tempture=int(reply.encode("hex"),16)
                reply=Serial_Con.read(1)
            count=200
            #print("-----------")
            return tempture
        count+=1
        sleep(0.1)

def ReadVin(id):
    #print("Read Temp ID:"+str(id)+"-------------")
    AX_READ_DATA=3
    AX_TEMP_READ=27
    Serial_Con.flushInput()
    checksum = (~(id + AX_READ_DATA + AX_TEMP_READ))&0xff
    outData = chr(AX_START)
    #print(hex(ord(chr(AX_START))))
    outData += chr(AX_START)
    #print(hex(ord(chr(AX_START))))
    outData += chr(id)
    #print(hex(ord(chr(id))))
    outData += chr(AX_READ_DATA)
    #print(hex(ord(chr(AX_READ_DATA))))
    outData += chr(AX_TEMP_READ)
    #print(hex(ord(chr(AX_TEMP_READ))))
    outData += chr(checksum)
    #print(hex(ord(chr(checksum))))
    Serial_Con.write(outData)
    sleep(TX_DELAY_TIME)
    #print("Done -----------")
    count=0
    sleep(0.1)
    while count<200:
        reply=Serial_Con.read(1)
        if reply != '':
            for x in range(0, 7):
                #print reply.encode("hex"),
                #print str(int(reply.encode("hex"),16))+""
                if x == 5:
                    #print reply.encode("hex")
                    #print str(int(reply.encode("hex"),16))+"*C"
                    tempture=int(reply.encode("hex"),16)
                reply=Serial_Con.read(1)
            count=200
            #print("-----------")
            return tempture
        count+=1
        sleep(0.1)

def ReadPos(id):
    #print("Read Temp ID:"+str(id)+"-------------")
    AX_READ_DATA=3
    AX_TEMP_READ=28
    Serial_Con.flushInput()
    checksum = (~(id + AX_READ_DATA + AX_TEMP_READ))&0xff
    outData = chr(AX_START)
    #print(hex(ord(chr(AX_START))))
    outData += chr(AX_START)
    #print(hex(ord(chr(AX_START))))
    outData += chr(id)
    #print(hex(ord(chr(id))))
    outData += chr(AX_READ_DATA)
    #print(hex(ord(chr(AX_READ_DATA))))
    outData += chr(AX_TEMP_READ)
    #print(hex(ord(chr(AX_TEMP_READ))))
    outData += chr(checksum)
    #print(hex(ord(chr(checksum))))
    Serial_Con.write(outData)
    sleep(TX_DELAY_TIME)
    #print("Done -----------")
    count=0
    sleep(0.1)
    while count<200:
        reply=Serial_Con.read(1)
        if reply != '':
            for x in range(0, 8):
                #print reply.encode("hex"),
                #print str(int(reply.encode("hex"),16))+""
                if x == 5:
                    #print reply.encode("hex")
                    #print str(int(reply.encode("hex"),16))+"*C"
                    pos1=reply.encode("hex")
                if x == 6:
                    #print reply.encode("hex")
                    #print str(int(reply.encode("hex"),16))+"*C"
                    pos2=int(reply.encode("hex")+pos1,16)
                reply=Serial_Con.read(1)
            count=200
            #print("-----------")
            return pos2
        count+=1
        sleep(0.1)

print("Starting.")
sleep(1)
print(".")
sleep(1)
print(".")
sleep(1)
print(".")
sleep(1)
print(".")
sleep(1)
print(".")

moveServo(1,500,0)
moveServo(2,500,0)
sleep(5)
print "ID:1 "+str(ReadTemp(1))+"*C"
sleep(1)
print "ID:2 "+str(ReadTemp(2))+"*C"
sleep(1)
print "ID:1 "+str(ReadVin(1))+"*V"
sleep(1)
print "ID:2 "+str(ReadVin(2))+"*V"
sleep(1)
print "ID:1 "+str(ReadPos(1))+"*P"
sleep(1)
print "ID:2 "+str(ReadPos(2))+"*P"
sleep(5)

moveServo(1,500,0)
moveServo(2,500,0)
sleep(1)
moveServo(1,500,100)
moveServo(2,500,100)
sleep(1)
moveServo(1,500,200)
moveServo(2,500,200)
sleep(1)
moveServo(1,500,300)
moveServo(2,500,300)
sleep(1)
moveServo(1,500,400)
moveServo(2,500,400)
sleep(1)
moveServo(1,500,500)
moveServo(2,500,500)
sleep(1)
moveServo(1,500,400)
moveServo(2,500,400)
sleep(1)
moveServo(1,500,300)
moveServo(2,500,300)
sleep(1)
moveServo(1,500,200)
moveServo(2,500,200)
sleep(1)
moveServo(1,500,100)
moveServo(2,500,100)
sleep(1)
moveServo(1,1000,850)
moveServo(2,1000,850)
sleep(2)
print "ID:1 "+str(ReadPos(1))+"*P"
sleep(1)
print "ID:2 "+str(ReadPos(2))+"*P"
