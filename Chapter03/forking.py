import os


def child():
    print("We are in the child process with PID= %d" % os.getpid())


def parent():
    print("We are in the parent process with PID= %d" % os.getpid())
    new_ref = os.fork()
    if new_ref == 0:
        child()
    else:
        print("We are in the parent process and our child process has PID = %d" % new_ref)


parent()
