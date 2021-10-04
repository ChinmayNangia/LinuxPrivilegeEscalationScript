#!/usr/bin/env python3

# Linux PrivEsc Script 

# Website used in the Process

# https://gtfobins.github.io/
# https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/
# This is script is made with video of Daniel Lowrie from youtube  --> https://www.youtube.com/watch?v=gc2cFwT_Fd0&list=PLtZSO0mhEgPz2ldxT3IxMgkKT94liKwup

# To be added capabilities , check for cron jobs and sudo -l privs ----> low hanging fruits and easy wins 

# It does ...
#          + OS , release and kernel information gathering 
#          + Checking the services that are running as root 
#          + Checking the process and the cronjobs that are running 
#          + Checking for SUID and GUID set owner user ID , set group owner Id 
#          + check for any cronjobs 
#          + create a text file to as output and name it as privEsc_summary.txt


import os


def return_to_main_function():
    GOTOMAIN  = input("Press enter to return  to main function and choose the appropriate option")
    MAIN()



# This will  check for OS release and  kernel information 
def OS_KERNEL_CHECK():
    print(flag)
    if flag != 0 :
        
        print("OS Kernel check function ")
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
       
        print("-----------------------------------------------------------------")
        ROOT_SERVICE_CHECK()
    
    else :
        os.system('clear')
        print("OS Kernel check function ")
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
    
    # This will run uname -a system command

    
    
    
    


 # This will checkk for the services running as rooot
def ROOT_SERVICE_CHECK():
    if flag != 0 :
       
        print(" Root Service Check Function ")
        os.system('ps aux | grep root')
        print("-----------------------------------------------------------------")
        SUID_GUID_CHECK()

    else:
        os.system('clear')
        os.system('ps aux | grep root')
        print("Root  service check function ")
        return_to_main_function()


 # THis will check for SUID and GUID binaries  
def SUID_GUID_CHECK():
    if flag != 0 :
        
        print('SUID & GUID check ')
        print(" ")
        print("SUID Checks")
        os.system('find / -type f -perm -04000 -ls 2>/dev/null')
        print("GUID Check")
        os.system('find / -perm -g=s -o -perm -u=s -type f 2>/dev/null')
        print("-----------------------------------------------------------------")
        print(" -----------------Full scan completed------------- ")
        return_to_main_function()

    else:
        os.system('clear')
        print("SUID and GUID check functions ")
        print("SUID Checks")
        os.system('find / -type f -perm -04000 -ls 2>/dev/null')
        print("GUID Check")
        os.system('find / -perm -g=s -o -perm -u=s -type f 2>/dev/null')
        return_to_main_function()


#-----------------------------------------------------------MAIN FUNCTION ---------------------------------------------------------------


def MAIN():
    global flag
    flag = 0 

    OPTION = input("""
    1 for OS and kernel check
    2 for root service check 
    3 SUID and GUID check 
    4 Full Scan
    5 For EXIT
    Lets Go !! >> """)

    




    if (OPTION == "1"):
        print(f"print you chose {OPTION}")
        OS_KERNEL_CHECK()
        


    if (OPTION == "2"):
        ROOT_SERVICE_CHECK()
        


    if (OPTION == "3"):
        SUID_GUID_CHECK()
    
    if (OPTION == "4"):
        flag = flag + 1
        OS_KERNEL_CHECK()
  
        



    if( OPTION == "5"):
        print("BYE , have fun escalating privileges !!!!")
        exit()


    else :
        print("This is invalid option try again  ")
        MAIN()
        

    
    
   

MAIN()

