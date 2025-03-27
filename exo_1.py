
def hello():
    print("hello python ")

def call(f,*args,**kwargs):
    return f(*args,**kwargs)
   # return f(*args,**kwargs) # ** va comme ouvrir un dictionnaire , lui prends pas seulement des valeur comme avec 1 * , on a des cles ici op et on peutmettre des valeurs 
# * ---> Lavaleurestuntoplereprenant lesparamètresdans l’ordre
# ** ---->  Lavaleurestundictionnairereprenant lesparamètres
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def compute(a,b,op=add):
    return op(a,b)



call(hello)
print(call(add,40,2))
print(call(compute,44,2,op=sub))
print(call(compute,44,2,op=lambda a,b:a*b))

    

