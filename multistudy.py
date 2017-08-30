# from multiprocessing import Process
# import os

# 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))#在这里用process类代表了一个进程对象
#     print('Child process will start.')
#     p.start() #用.start()方法启动Process实例
#     p.join() #.join()方法可以等待子进程结束后继续往下运行
#     print('Child process end.')
## 这个程序只能在cmd里运行，不能在VScode的console里运行，我在这里怀疑是VScode只允许创建一个进程，cmd里没有这个限制

## 启动大量的子进程，用进程池的方式批量创建子进程
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3) #每个子进程sleep随机的时间，从最后的结果可以看出来4个程序在在运行的时间上有交错
    end = time.time()
    print('Task %s runs %0.2f seconds, task start at %0.2f, task end at %0.2f' % (name, (end-start), start, end))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print("waiting for all subprocess done...")
    p.close() #对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    p.join()
    print('ALL subprocess done')