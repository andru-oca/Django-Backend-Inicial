# if - elif - else

# siempre tienen esa funcionalidad de que en cualquier lenguaje de programacion
# donde te permite seleccionar el recorrido de la decision requerida

# EJEMPLO PRACTICO

polygon_selected = input("ingrese una cantidad de lados") or 0

polygon_selected = int(polygon_selected) 

if polygon_selected == 1 :
    print("esto no es un poligono")
elif polygon_selected > 1 :
    print("esto si es un poligono")
else:
    print("que me pusiste, cheamigo?")