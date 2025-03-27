from time import sleep 
def delay(t):
    def decorator(f):  # le decorateur renvoie la fonction mais modifié , ajout d'un comportement avant et  près l'appel d'une fonction
        def wrapper(*args,**kwargs): # génerateur lui renvoie dez décorateurs
            sleep(t)
            return f(*args,**kwargs)
        return wrapper
    return decorator

@delay(2) # le @ syntaxe qui indique que y'aura un décorateur
def printnum(i):
    print(i)


def binrep(n): # fonction générattrice
    while n > 0:
        yield n % 2 # yield c'est comme un return qui retient ou on est dans la fonction
        n//=2
for b in binrep(334):
    print(b)
 