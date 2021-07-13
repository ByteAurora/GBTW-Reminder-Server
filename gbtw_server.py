import time
import community_parser
import threading

check_community_thread = threading.Thread(target=community_parser.check_community())
check_community_thread.start()

for loop in range(1, 1000):
    print("hi")
    time.sleep(1)
