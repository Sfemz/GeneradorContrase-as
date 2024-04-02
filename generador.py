import random

while True:
    minusculas = "abcdefghijklmnñopqrstuvwxyz"
    mayusculas = minusculas.upper()
    numeros = "1234567890"
    simbolos = ",;.:-_<>+*!$%&=?¿Ç|@#~€ºª"

    base = minusculas + mayusculas + numeros + simbolos

    longitud = int(input("¿Cuantos caracteres quieres? (Máximo 89): "))
    muestra = random.sample(base,  longitud,)
    contraseña = "".join(muestra)
    print(contraseña)
