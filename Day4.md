# Day 4 — Multi-Input Scanning & Port Scanning

## What I did (EN)
- Improved my Python scanner to accept multiple user-input targets  
- Used input() and split() to process multiple targets  
- Made the tool more dynamic instead of using fixed values  
- Created a new script for port scanning using Python  
- Used the socket module to test connections to ports  
- Scanned common ports (22, 80, 443)  
- Tested port scanning on real targets (e.g. google.com)  
- Tested scanning on localhost (127.0.0.1)  
- Combined understanding of host availability and port scanning  

## What I learned (EN)
- How to handle user input in Python and convert it into usable data  
- How to split strings into lists for processing multiple targets  
- That ports represent services running on a system  
- How TCP connections are used to check if a port is open  
- That an open port means a service is accessible  
- The difference between scanning a remote host and localhost  
- How basic port scanning works in practice  
- That cybersecurity involves identifying exposed services  

## Example commands

```bash
python3 scan.py
python3 port_scan.py
```
## Example python

```
import socket

target = input("Enter target: ")

ports = [22, 80, 443]

for port in ports:
    print(f"Checking {target}:{port}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    sock.close()
```
## Mitä opin (FI)
- Opin käsittelemään käyttäjän syötettä Pythonissa ja jakamaan sen useisiin kohteisiin
- Opin käyttämään split()-funktiota listojen muodostamiseen
- Ymmärsin, että portit edustavat palveluita tietokoneessa
- Opin, että TCP-yhteydellä voidaan testata portin avoimuus
- Ymmärsin, että avoin portti tarkoittaa saavutettavaa palvelua
- Opin eron etäkohteen ja localhostin skannaamisen välillä
- Opin, miten porttiskannaus toimii käytännössä
- Ymmärsin, että kyberturvallisuudessa etsitään avoimia palveluita

Thoughts

Today felt like a shift from basic scripting to something closer to real cybersecurity work. Instead of just checking if a system is reachable, I started identifying what services are running. This made the tools feel much more practical and closer to real-world use.
