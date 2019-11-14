#Code to get device ID

def getserial():
    cpuserial ="0000000000000000"
    try:
        f = open('/proc/cpuinfo','r')
        for line in f:
            if line [0:6]=='Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial ="Error"

    return cpuserial
    
print ("Device Id is ",getserial())  
