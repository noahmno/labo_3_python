def decorate(f):
    def wrapper():
        print('Avant appel')
        f()
        print('Après appel')
    return wrapper
 
@decorate
def sayhello():
    print('Hello!')
 
sayhello()

class Natural:
    def __init__(self,n):
        self.__n = n 
        self.__bin_n = n 
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__bin_n==0:
            raise StopIteration()
        bit = self.__bin_n % 2
        self.__bin_n //=2
        return bit 
for b in Natural(12):
    print(b)