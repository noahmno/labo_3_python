from time import sleep 
def delay(t):
    def decorator(f):
        def wrapper(*args,**kwargs):
            sleep(t)
            return f(*args,**kwargs)
        return wrapper
    return decorator

@delay(2)
def printnum(i):
    print(i)


def binrep(n):
    while n > 0:
        yield n % 2
        n//=2
for b in binrep(12):
    print(b)
 