import time
import community_parser
import threading

check_community_trial_thread = threading.Thread(target=community_parser.check_community_trial())
check_community_trial_thread.start()
