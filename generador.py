import random

while True:
    minusculas = "abcdefghijklmnñopqrstuvwxyz"
    mayusculas = minusculas.upper()
    numeros = "1234567890"
    simbolos = ",;.:-_<>+*!$%&=?¿Ç|@#~€ºª"

    base = minusculas + mayusculas + numeros + simbolos

    longitud = int(input("""
______________________________________________ 
|                                             |
| ¿Cuantos caracteres quieres? (Máximo 89):   |
|_____________________________________________|
                         
ESCRIBE UN NÚMERO: """))
    muestra = random.sample(base,  longitud,)

    contraseña = "".join(muestra)
    print(contraseña)
