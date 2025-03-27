from time import sleep

def delay(f):
    def wrapper(*args,**kwargs):
        sleep(1)
        return f(*args,**kwargs)
    return wrapper 


@delay
def printnum(i):
    print(i)

cnt= 3
while cnt> 0 :
    printnum(cnt)
    cnt -= 1
print('KA-BOOM!')