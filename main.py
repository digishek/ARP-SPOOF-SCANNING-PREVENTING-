import getarp
import ping 
import statictable
import scanforattack
import scanforweakattack 
def getinput():
    print("STARTED ARP TOOL")
    print("1. Create static entries ")
    print("2. Scan for attack ")
    x=int(input("ENTER YOUR INPUT............................."))
    if(x==1):
        return table()
    if(x==2):
        return attack()
    else:
        return getinput()
def table():
    print("1.Work with existing ARP TABLE ")
    print("2.Create ARP for all devices (RECOMMENDED)")
    print("3.Manually add entries")
    print("4. go back")
    x=int(input())
    if(x==2):
        ping.pingall(ping.getadd())
        
    if(x==1):
        getarp.gettable(getarp.map)
       
    if(x==3):
        getarp.addvalues(getarp.map)
   
    if(x==4):
        return getinput()
    temp = input("Do you want to manually add more entries .....y/n")  
    if(temp=='y'):
        getarp.addvalues(getarp.map)
    print("All values found ,adding to static table")
    statictable.writearp(getarp.map)
def attack():
    print("WARNING , PLEASE RUN THIS IN SUDO MODE FOR IT TO WORK")
    print("Quick scaning for weak attack.....................")
    if(scanforweakattack.scan()):

        print("No attacks found , monitoring the network")
        print("This will keep on running in the background and notify you if attack happens")
        scanforattack.run()
        
        
getinput() 


