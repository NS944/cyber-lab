import os

target = input("Enter target: ")

print("Scanning...", target)

result = os.system("ping -c 3 " + target)

if result == 0:
    print("Target is reachable")
else:
    print("Target is NOT reachable")
