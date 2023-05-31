"""
EXERCISE TEXTO
para pasar a un funcion
Diseñar un programa que permita ingresar un texto, separarlo mediante la función
split() en una lista y obtener una nueva lista con las palabras ordenadas por el
tamaño de cada cadena.
"""


MOCK_TEXT ="""Why do we use it?

    It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose.
"""

def get_data()->list:
    
    input_text = input("ingrese texto a analizar")

    return input_text.split(" ")

def clean_data(splitted_data:list ):
    
    cleaned_words_list = []

    patterns_chars = ["\n" , "." , "-","!"]

    for word in splitted_data:
        for chars in patterns_chars:
            if chars in word:
                word.replace(chars,'')
        
        if len(word.strip()) == 0 :
            cleaned_words_list.append(words.strip())

    return cleaned_words_list

def order_list(cleaned_words_list:list)->list:
    return cleaned_words_list.sort(key=len)



def main():
    """
    @params
    return
    """
    # obtener el texto por el medio que sea necesario
    retrive_data:list = get_data()

    # dividir el texto en palabras
    ordered_list_cleaned:list = clean_data(retrive_data)

    # sort palabras

    return order_list(ordered_list_cleaned)