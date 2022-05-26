import threading
import time
  
def print_cube(n):
    for num in n:
       print("Cube:", (num*num*num))
  
def print_square(num):
    print("Square:", num*num)
  
if __name__ == "__main__":
    t1 = threading.Thread(target=print_cube, args=([10,2,5,6],))
    t2 = threading.Thread(target=print_square, args=(10,))
    t1.start()
    #time.sleep(4)
    print(threading.current_thread())
    t2.start()

    t1.join()
    #time.sleep(4)
    t2.join()
    print(threading.main_thread().name)
    print("Done!")