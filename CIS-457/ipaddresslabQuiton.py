def decimalTobinary(num):
    binary = bin(num)
    if(len(binary) <= 4):
        binary = binary.replace("0b", "0000")
    else:
        binary = binary.replace("0b", "")
    if(len(binary) < 8):
        while(len(binary) < 8):
            binary = "0" + binary
    return binary

def ipidentifier():
    
    ipAddress = input("Enter IP address: ")
    while(ipAddress != "stop"):
        ip = []
        number = ""
        ipclass = ""
        subnetmask = ""
        for digit in ipAddress:
            if(digit == "."):
                ip.append(int(number))
                number = ""
                continue
            number = number + digit
        ip.append(int(number)) 

        #ip address in binary
        binaryIP = ""
        counter = 0
        for digit in ip:
            binaryDigit = decimalTobinary(digit)
            counter += 1
            if(counter <= 3):
                binaryIP += binaryDigit + "."
            else:
                binaryIP += binaryDigit
        print(binaryIP)

        #ip/subnet mask class identification
        if(ip[0] >= 0 and ip[0] <= 127):
            ipclass = "A"
            subnetmask = "255.0.0.0"
        elif(ip[0] >= 128 and ip[0] <= 191):
            ipclass = "B"
            subnetmask = "255.255.0.0"
        elif(ip[0] >= 192 and ip[0] <= 223):
            ipclass = "C"
            subnetmask = "255.255.255.0"
        elif(ip[0] >= 224 and ip[0] <= 239):
            ipclass = "D"
            subnetmask = "no default subnet mask"
        else:
            ipclass = "E"
            subnetmask = "no default subnet mask"
        
        print("Class: " + ipclass)
        print("Default Subnet Mask: " + subnetmask)
        print("-------------------------------------")
        ipAddress = input("Enter IP address: ")
    

ipidentifier()




