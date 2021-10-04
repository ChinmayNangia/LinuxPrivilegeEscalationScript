#!/usr/bin/env python3

# Linux PrivEsc Script 

# Website used in the Process

# https://gtfobins.github.io/
# https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/



# It does ...
#          + OS , release and kernel information gathering 
#          + Checking the services that are running as root 
#          + Checking the process and the cronjobs that are running 
#          + Checking for SUID and GUID set owner user ID , set group owner Id 
#          + check for any cronjobs 
#          + create a text file to as output and name it as privEsc_summary.txt


import os
os.system('clear')

def return_to_main_function():
    GOTOMAIN  = input("Press enter to return  to main function and choose the appropriate option")
    MAIN()



# This will  check for OS release and  kernel information 
def OS_KERNEL_CHECK():
    # print("OS Kernel check function ")
    # This will run uname -a system command
    
    print(" ")
    os.system('whoami')
    os.system('id')
    os.system('uname -a')
    os.system('uname -r')
    print(" ")
    print("---------------------------------- etc/passwd start ---------------------------------------")
    print(" ")
    os.system('cat /etc/passwd')
    print(" ")
    print("---------------------------------- etc/passwd end  ---------------------------------------")
    print(" ")
    os.system('cat /etc/*-release')
    os.system('cat /etc/issue')
    return_to_main_function()
    
    
    


 # This will checkk for the services running as rooot
def ROOT_SERVICE_CHECK():
   print("Root  service check function ")
   return_to_main_function()


 # THis will check for SUID and GUID binaries  
def SUID_GUID_CHECK():
    print("SUID and GUID check functions ")
    return_to_main_function()


#-----------------------------------------------------------MAIN FUNCTION ---------------------------------------------------------------


def MAIN():
    OPTION = input("""
    1 for OS and kernel check
    2 for root service check 
    3 SUID and GUID check 
    4 for EXIT
    Lets Go !! >> """)


    if (OPTION == "1"):
        print(f"print you chose {OPTION}")
        OS_KERNEL_CHECK()
        


    elif (OPTION == "2"):
        ROOT_SERVICE_CHECK()
        


    elif (OPTION == "3"):
        SUID_GUID_CHECK()
        



    elif( OPTION == "4"):
        print("BYE !!")
        exit()


    else :
        print("This is invalid option try again Be safe ")
        MAIN()
        

    
    
   

MAIN()

