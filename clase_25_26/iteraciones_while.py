from random import randint

# el famoso y while

# edad = randint(1,20)
# print(f"La edad es: {edad}")

# while edad < 18 :
    
#     edad = randint(1,20)
#     print(f"La edad es: {edad}")

flag = True

while flag:

    edad = randint(1,20)
    print(f"La edad es: {edad}")

    if edad == 18 :
      flag = False
    #   break !! mirar por que pasa esto jeje
    if edad == 2:
        print("como es igual a 2, lo paso por arriba")
        continue
else:
    print("de alguna forma iba a salir o salir")


