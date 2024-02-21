from msj.mensajes import mensaje_exito, mensaje_fracaso
from data.abecedario import abecedario_incompleto as abecedario


def caja_bomba():
    return ">>>💥<<<"


def adivinar_clave(letra):
    ls = abecedario()
    if letra in ls:
        return mensaje_exito()
    else:
        return " ".join([mensaje_fracaso(), caja_bomba()])



while(True):
    v = input("adivina el valor, sino adios: ")
    r = adivinar_clave(v.upper())
    if len(r) > 30:
        print(r)
        break
    print(r)



# def nombre():  #-> crear el diseño
# nombre         #-> exportando diseño
# nombre()       #-> ejecutar la funcion
