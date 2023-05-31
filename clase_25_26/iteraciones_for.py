# ejemplos practicos del for
# recordemos que el for siempre usa elementos de iteracion, tales como strings, rangos , tuplas

# primera iteracion

for i in range(1,20):
    print(f" numero de iteracion: {i}")

# otra forma seria 
for _ in range(20):
    print(f" numero de iteracion: {_}")


# iteracion por strings

reductor_texto = ""

for _ in "hola mundo":
    if _ != "h":
        reductor_texto += _

print(reductor_texto)


# iteracion por list
# !!!! pero antes! que es un list? 



