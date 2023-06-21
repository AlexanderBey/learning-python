import time 
from threading import Thread


def do_this():
    print("Starting this!")
    #Simulate doing something
    time.sleep(2)
    print("Did this!")

def do_that():
    print("Starting that!")
    #Simulate doing something
    time.sleep(3)
    print("Did that!")


do_this()
do_that()

thread1 = Thread(target=do_this)
thread1.start()

thread2 = Thread(target=do_that)
thread2.start() 