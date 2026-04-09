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
