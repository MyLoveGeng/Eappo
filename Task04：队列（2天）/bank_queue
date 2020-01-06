import threading
import time
import random

queue = []
nums = 0

def come_guest():
    while True:
        global nums, queue
        nums += 1
        print("您的号码是{}，您前面还有{}位客人".format(nums, len(queue)))
        time.sleep(random.uniform(1, 3))
        queue.append(nums)

def get_guest():
    while True:
        global queue
        time.sleep(random.uniform(3, 5))
        guest = queue.pop(0)
        print("呼叫号码为{}的客人".format(guest))

if __name__ == '__main__':
    c1 = threading.Thread(target=come_guest)
    g1 = threading.Thread(target=get_guest)
    c1.start()
    g1.start()
    c1.join()
    g1.join()
