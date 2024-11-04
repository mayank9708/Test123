import socket
import sys
import os

# Grab the banner
def grab_banner(ip_address, port):
    try:
        s = socket.socket()
        s.connect((ip_address, port))
        banner = s.recv(1024).decode('utf-8')  # Decode the banner to string format
        print(f"{ip_address}:{banner}")
        s.close()
    except:
        return

# Check for vulnerabilities based on the banner
def checkVulns(banner):
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        with open(filename, 'r') as file:  # Correctly open the file
            for line in file.readlines():
                line = line.strip('\n')
                if banner in line:
                    print(f"{banner} is vulnerable")
                else:
                    print(f"{banner} is not vulnerable")

def main():
    portList = [21, 22, 25, 80, 110]
    for x in range(0, 255):
        for port in portList:
            ip_address = '192.168.0.' + str(x)  # Specify the desired IP range
            banner = grab_banner(ip_address, port)  # Get banner
            if banner:
                checkVulns(banner)  # Check vulnerabilities

if __name__ == '__main__':
    main()

