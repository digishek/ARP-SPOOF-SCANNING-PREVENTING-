import os

map ={}

def gettable(map):
    with os.popen('arp -a') as f:
        data = f.read()
    data=data.split() 
    for i in range(len(data)):
        if(data[i]=="at" and data[i+1]!="<incomplete>" ):
            map[data[i-1]]=data[i+1]
def addvalues(map):
    n=int(input("How many values do you want to add"))
    for i in range(n):
        ip=input("Enter the value of ip")
        ip='('+ip+')'
        mac=input("Enter the corresponding MAC address")
        map[ip]=mac
