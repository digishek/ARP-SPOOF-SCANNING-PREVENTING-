import subprocess

import os
def writearp(map):
    
    sudoPassword = input("Please enter your password..............")

    for i in map :
        string= " sudo arp -s "+i[1:-1]+" "+map[i]
        print("Writing "+i[1:-1]+" "+map[i])
        os.popen("sudo -S %s"%(string), 'w').write(sudoPassword)
    print("Your static ARP table has successfully been created")
    
