# Day 2 — Network Traffic & Python Tool

## What I did (EN)
- Installed tcpdump for packet capture
- Captured live network traffic from my VM
- Observed ICMP traffic using ping
- Observed DNS requests when resolving domain names
- Learned how to filter traffic (icmp, port 53)
- Created network traffic manually using ping
- Built a Python script to automate pinging a target
- Added user input and result checking to the script
- Combined Python + tcpdump to generate and observe traffic

## What I learned (EN)
- How network communication works at a basic level
- That DNS happens before any connection is made
- How ICMP (ping) works (request → reply)
- How to capture and analyze packets using tcpdump
- How to generate traffic intentionally and observe it
- How Python can be used to automate network actions

## Example commands

```bash
sudo tcpdump -i enp0s3
sudo tcpdump -i enp0s3 icmp
sudo tcpdump -i enp0s3 port 53
ping google.com
python3 scan.py
```

## Example Python
import os

target = input("Enter target: ")

print("Scanning...", target)

result = os.system("ping -c 3 " + target)

if result == 0:
    print("Target is reachable")
else:
    print("Target is NOT reachable")

## Mitä opin (FI)
- Opin kaappaamaan verkkoliikennettä tcpdump-työkalulla
- Opin, että DNS-kysely tapahtuu ennen yhteyden muodostamista
- Ymmärsin miten ping toimii (pyyntö ja vastaus)
- Opin suodattamaan verkkoliikennettä (ICMP, DNS)
- Opin yhdistämään Pythonin ja verkkoliikenteen
- Rakensin yksinkertaisen työkalun, joka testaa kohteen saavutettavuuden

## Thoughts
This was the first time I actually saw real network traffic. It helped me understand how the internet works behind the scenes. Combining Python and tcpdump made it feel like I was building real tools.
