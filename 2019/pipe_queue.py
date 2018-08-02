#coding:utf-8
import multiprocessing
import time
 
def proc1(pipe):
    while True:
        for i in range(10):
            print ("发送 %s"%i)
            pipe.send(i)
            time.sleep(1)
 
def proc2(pipe):
    while True:
        print ('proc2 接收:',pipe.recv())
        time.sleep(1)
 
def proc3(pipe):
    while True:
        print ('proc3 接收:',pipe.recv())
        time.sleep(1)
# Build a pipe
pipe = multiprocessing.Pipe()
print (pipe)


if __name__ == '__main__':
    # Pass an end of the pipe to process 1
    p1   = multiprocessing.Process(target=proc1, args=(pipe[0],))
    # Pass the other end of the pipe to process 2
    p2   = multiprocessing.Process(target=proc2, args=(pipe[1],))
    p3   = multiprocessing.Process(target=proc3, args=(pipe[1],))

    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()