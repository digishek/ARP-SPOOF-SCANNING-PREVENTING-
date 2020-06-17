import os
def scan():
    arr=set()
    with os.popen('arp -a') as f:
        data = f.read()
    data=data.split() 
    for i in range(len(data)):
        if(data[i]=="at" and data[i+1]!="<incomplete>" ):
            if data[i-1] in arr:
                print("WARNING!!!!!!!!! YOU ARE UNDER ATTACK ")
                print("The mac address causing problem is " ,data[i+1])
                return False
            else:
                arr.add(data[i-1])
    return True 