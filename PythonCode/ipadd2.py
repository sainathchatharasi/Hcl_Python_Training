import os, ipaddress

#clear screen of the command prompt
os.system('cls')

while True:
    ip = input("enter IP address: ")
    try:
    #checks for the format of the ip address
        print(ipaddress.ip_address(ip))
        print("ip Valid")
    except:
        print('-'*50)
        print('IP is not valid')
    finally:
        if ip =='q':
            print("script Finished")
            break