# Day 3 — Multi-Target Scanning, TCP & Detection Mindset

## What I did (EN)
• Improved my Python script to scan multiple targets automatically  
• Used a for loop to iterate through targets  
• Added output formatting to make results clearer  
• Learned the difference between ICMP, DNS, and TCP traffic  
• Generated TCP traffic using curl  
• Captured TCP traffic using tcpdump  
• Observed TCP SYN packets (connection start)  
• Learned how to filter TCP traffic  
• Used a filter to isolate SYN packets only  
• Repeated connections to observe patterns in traffic  

## What I learned (EN)
• How to automate scanning of multiple targets using loops  
• That Python indentation is critical for code execution  
• How TCP differs from ICMP and DNS  
• That TCP connections start with a SYN packet  
• How web requests generate TCP traffic  
• That network traffic is constant and includes background noise  
• How filtering is necessary to isolate specific behavior  
• That cybersecurity involves recognizing patterns, not just individual packets  

## Example commands
```bash
python3 scan.py
sudo tcpdump -i enp0s3 tcp
curl http://example.com
sudo tcpdump -i enp0s3 -nn tcp
sudo tcpdump -i enp0s3 -nn 'tcp[tcpflags] & tcp-syn != 0'
````

## Example Python

```python
import os

targets = ["google.com", "1.1.1.1", "8.8.8.8"]

for target in targets:
    print("=" * 30)
    print("Scanning...", target)

    result = os.system("ping -c 2 " + target)

    if result == 0:
        print("Target is reachable")
    else:
        print("Target is NOT reachable")
```

## Mitä opin (FI)

- Opin parantamaan Python-työkalua niin, että se käsittelee useita kohteita automaattisesti  
- Opin käyttämään for-silmukkaa käytännössä  
- Ymmärsin, että Pythonissa sisennys on erittäin tärkeä  
- Opin eron TCP-, ICMP- ja DNS-liikenteen välillä  
- Ymmärsin, että TCP-yhteys alkaa SYN-paketilla  
- Opin, että verkkoliikenne on jatkuvaa ja sisältää taustakohinaa  
- Opin suodattamaan TCP-liikennettä tcpdumpilla  
- Ymmärsin, että kyberturvallisuudessa tärkeää on tunnistaa liikennemalleja  

## Thoughts

Today I started thinking more like an analyst instead of just running commands. The most important insight was that networks are always active, so filtering and pattern recognition are necessary to understand what is happening.




