
def hello():
    print("hello python ")

def call(f,*args,**kwargs):
    return f(*args,**kwargs)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def compute(a,b,op=add):
    return op(a,b)



call(hello)
print(call(add,40,2))
print(call(sub,40,2))

    

