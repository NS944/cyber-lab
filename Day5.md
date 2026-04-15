# Day 5 — Combined Scanner & Multi-Target Port Scanning

## What I did (EN)
- Combined my host scanner and port scanner into one tool (scanner.py)  
- Created a workflow: check if host is alive before scanning ports  
- Used exit() and continue to control program flow  
- Improved the tool to handle multiple targets in one run  
- Used input() and split() to process multiple targets  
- Implemented nested loops for scanning multiple targets and ports  
- Added logic to skip unreachable hosts  
- Added a summary feature to display open ports clearly  
- Improved output formatting for readability  

## What I learned (EN)
- How to combine multiple scripts into one structured tool  
- How control flow (if, continue, exit) affects program behavior  
- How to process multiple user inputs efficiently  
- How nested loops work in practice  
- That tools should not only work but also present results clearly  
- That summarizing results is important for usability  
- How basic scanners are structured in real cybersecurity tools  

## Example commands

```bash
python3 scanner.py
```
## Example python
```
import os
import socket

user_input = input("Enter targets (separated by space): ")
targets = user_input.split()

ports = [22, 80, 443]

for target in targets:
    print("=" * 40)
    print(f"Scanning {target}")
    print("=" * 40)

    print("\n[+] Checking if host is alive...\n")
    result = os.system("ping -c 2 " + target)

    if result != 0:
        print("Host is not reachable. Skipping port scan.\n")
        continue

    print("\n[+] Host is reachable. Starting port scan...\n")

    open_ports = []

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port)
        else:
            print(f"Port {port} is CLOSED")

        sock.close()

    print("\n[+] Summary")
    if open_ports:
        print(f"Open ports on {target}: {open_ports}")
    else:
        print(f"No open ports found on {target}")

    print()
```
## Mitä opin (FI)
- Opin yhdistämään kaksi erillistä skriptiä yhdeksi työkaluksi
- Opin käyttämään ohjelman ohjausrakenteita (if, continue, exit)
- Opin käsittelemään useita kohteita yhdellä ajolla
- Ymmärsin sisäkkäisten silmukoiden käytön käytännössä
- Opin, että työkalun tulee esittää tulokset selkeästi
- Opin, että tulosten yhteenveto parantaa käytettävyyttä
- Ymmärsin paremmin, miten skannerit toimivat kyberturvallisuudessa

## Thoughts
Today felt like building a real tool instead of just small scripts. Combining multiple features into one workflow and improving the output made the program feel more practical and closer to real-world cybersecurity tools.
