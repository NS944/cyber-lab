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
