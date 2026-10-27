#Concept Understanding

import time
#print(time.time())
def cal_sq(numbers):
    print("Square Numbers:")
    for number in numbers:
        time.sleep(0.2)
        print("Squares:",number*number)
def cal_cub(numbers):
    print("Cubic Numbers:")
    for number in numbers:
        time.sleep(0.2)
        print("Cubes:",number*number*number)
initial_time=time.time()
l=[1,2,3,4,5]
cal_sq(l)
cal_cub(l)
print("Time Taken:",time.time()-initial_time)

import time
import threading
def cal_sq(numbers):
    print("Square Numbers:")
    for number in numbers:
        time.sleep(0.2)
        print("Squares:",number*number)
def cal_cub(numbers):
    print("Cubic Numbers:")
    for number in numbers:
        time.sleep(0.2)
        print("Cubes:",number*number*number)
initial_time=time.time()
l=[1,2,3,4]
t1=threading.Thread(target=cal_sq,args=(l,))
t2=threading.Thread(target=cal_cub,args=(l,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Time Taken:",time.time()-initial_time)

#Using class Thread

from threading import Thread
import time
class A(Thread):
    def run(self):
        for i in range(10):
            print(i)
            time.sleep(1)
ob=A()
ob1=A()
ob.start()
ob1.start()
ob.join() #joining object thread to main thread
ob1.join()
print("Main Thread is Ended..")

#Using ThreadPoolExecutor

import threading
import time
from concurrent.futures import ThreadPoolExecutor
def fun(name,x):
    for i in range(x):
        print(f"{name}:{i}")
        time.sleep(1)
t1=threading.Thread(target=fun,name="thread1",args=("thread-1",10))
t2=threading.Thread(target=fun,name="thread2",args=("thread-2",10))
t1.start()
t2.start()
print(t1.is_alive())
print(t2.is_alive())
t1.join()
t2.join()
print("Main thread is Ended..")
print(t1.is_alive())
print(t2.is_alive())

#1st Questions Practice
import threading
def worker():
    print("Hello from worker thread")
t1=threading.Thread(target=worker)
t1.start()
print("Hello from main thread")
t1.join()

#2nd
import threading
def numbers():
    for i in range(1,6):
        print(threading.current_thread().name,":",i)
t1=threading.Thread(target=numbers,name="Thread-1")
t2=threading.Thread(target=numbers,name="Thread-2")
t3=threading.Thread(target=numbers,name="Thread-3")
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

#2nd using ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import threading
def numbers(name,x):
    for i in range(1,x+1):
        print(f"{name}:{i}")
t1=threading.Thread(target=numbers,name="thread1",args=("Thread-1",5))
t2=threading.Thread(target=numbers,name="thread2",args=("Thread-2",5))
t3=threading.Thread(target=numbers,name="thread3",args=("Thread-3",5))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

#3rd
import threading
def calculate_sum(x,y):
    result=x+y
    print("sum =",x+y)
t1=threading.Thread(target=calculate_sum,args=(10,20))
t1.start()
t1.join()
print("Main Thread Completed..")

#4th
import threading
counter=0
def increment():
    global counter
    for i in range(100000):
        counter+=1
t1=threading.Thread(target=increment)
t2=threading.Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()
print("Final Counter:",counter)

#5th
import threading
counter=0
lock=threading.Lock()
def increment():
    global counter
    for i in range(100000):
        with lock:
            counter+=1
t1=threading.Thread(target=increment)
t2=threading.Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()
print("Final Counter:",counter)

#6th
import threading
import time
def A():
    print("A Started")
    time.sleep(2)
    print("A Finished")
def B():
    print("B Started")
t1=threading.Thread(target=A)
t2=threading.Thread(target=B)
t1.start()
t1.join()
t2.start()
t2.join()

#7th
import threading
import time
event=threading.Event()
def worker():
    event.wait()
    print(threading.current_thread().name,"has started execution")
t1=threading.Thread(target=worker,name="Thread1")
t2=threading.Thread(target=worker,name="Thread2")
t3=threading.Thread(target=worker,name="Thread3")
t1.start()
t2.start()
t3.start()
print("Main Thread is Sleeping..")
time.sleep(2)
print("Main Thread Sending Signal..")
event.set()
t1.join()
t2.join()
t3.join()

#8th
import threading
import time
semaphore=threading.Semaphore(2)
def worker():
    with semaphore:
        print(threading.current_thread().name,"entered critical section")
        time.sleep(2)
        print(threading.current_thread().name,"existed critical section")
thread=[]
for i in range(1,6):
    t=threading.Thread(target=worker,name=f"Thread-{i}")
    thread.append(t)
    t.start()
for t in thread:
    t.join()
print("Main Thread is Completed")

#9th
import threading
import time
def background_task():
    while True:
        print("Running in Background")
        time.sleep(0.5)
t=threading.Thread(target=background_task,daemon=True)
t.start()
time.sleep(2)
print("Main Thread Completed..")

#10th
from concurrent.futures import ThreadPoolExecutor,as_completed
def square(n):
    return n*n
t=ThreadPoolExecutor(max_workers=3)
futures=[t.submit(square,i) for i in range(1,6)]
for i in as_completed(futures):
    print(i.result())
t.shutdown()









