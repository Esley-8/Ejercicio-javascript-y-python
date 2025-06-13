""" HAZ UNA FUNCION QUE CUENTE EL NUMERO DE VOCALES EN UN STRING PASADA POR PARAMETROS"""

lista_vocales = 
["a" , "e", "i", "o","u"]




def cont_vocales(msg):
    nvocales =0
    for char in msg:
        
        if char in lista_vocales:
            nvocales +=1
        
        print (f"{msg} tiene {nvocales} vocales.")

cont_vocales("Aceituna")
cont_vocales("Murciélago")
cont_vocales("Educación")
cont_vocales("Aeropuerto")
cont_vocales("Otorrinolaringólogo")
cont_vocales("Euforia")
cont_vocales("Aceite")
cont_vocales("Paleontólogo")
cont_vocales("Arquitectura")
cont_vocales("Hipopótamo")
cont_vocales("Aceituna")
cont_vocales("Aceituna")
        