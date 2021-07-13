import time
import community_parser
import threading

check_community_thread = threading.Thread(target=community_parser.check_community())
check_community_thread.start()
