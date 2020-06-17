import os
import socket 
import getarp
def getadd(): 
    print("We are getting your address .........................")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    address=(s.getsockname()[0])
    s.close()
    print("Your address is ",address)
    return address 

def pingall(address):
    print("Generating arp table.....................")
    counter=1
    value=[i for i in address.split('.')]
    string=""
    print("Sending ping to all address........................")
    for i in range(len(value)-1):
        string+=value[i]+"." 
    while(counter<=255):
        if(counter%15==0):
            print("Getting values for the past 15 tables")
            getarp.gettable(getarp.map)
            print("Current table is")
            print(getarp.map)
        print("Pinging "+ string+str(counter) )
        os.system("ping "+string+str(counter)+" -c 1") 
        print("Operation was successful")
        counter+=1 
    print("Pinging compleated")
    print("Arp table generated")