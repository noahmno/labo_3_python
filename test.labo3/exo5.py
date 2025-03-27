def decorate(f):
    def wrapper():
        print('Avant appel')
        f()
        print('Après appel')
        
    return wrapper
 
def sayhello():
  print('Hello!')
 
g = decorate(sayhello)
g()