#Parte 1 - recorrido de lista.

lista_1 = (1, 15, 20, 5, 14, 22, 30)               #lista de números a sumar y recorrer.

suma = 0                                           #variable inicializada en 0. 

for num in lista_1:                                #bucle for para conteo y suma de valores.
    suma = suma + num 

print("La suma de la lista de números es: " ,suma)  #imprime el resultado en pantalla. 

#Parte 2 - manejo de excepciones.

lista_1 = [1, 15, 20, 5, 14, 22, 30]             #lista de números a sumar y recorrer.

suma = 0                                         #variable inicializada en 0.                                         
resultado = 0
for num in lista_1:
    suma = suma + num 


opcion = int(input("Ingrese la opción que desee : + \n 1) ingresar un valor. \n 2) salir."))   #Se le solicita al usuario que elija la opción que desea realizar.

while (opcion):
    if (opcion == 1):

        try:
            divisor = int(input("Ingrese el divisor"))                                         #Inicia el bloque de código que permite la excepción, se agregan 2 de ellas.
            resultado = suma / divisor
        except ZeroDivisionError:                                                              #Valor en 0.
            print ("Agregue otro divisor que no sea 0.")
        except ValueError:                                                                     #Si se ingresa un valor inválido.
            print("agregue otro valor que no sea un caracter.")
        else:
            print("El resultado es:", resultado)
    if (opcion == 2):                                                                          #Si desea salir del programa.
        print("Gracias por ingresar.")
        break


#Parte 3 - Paso de parámetros


def parametros():                                                                              #Se agrega una operación matemática que afecta a ambos casos, el valor entero
    num = int(input("digite un valor"))                                                        #Valor ingresado por el usuario.
    resultado = num + 2
    lista_1[2] += num
    print (resultado)
    print (lista_1)

parametros()


#parte 4 - Paso por resultado


def cambio_elemento():                                                                         #En este caso se pasa el valor por referencia, ya que modifica los valores de la lista original.

    lista_1[1] = 100
    print (lista_1)

cambio_elemento()


print("La lista se modificó tal que: ", lista_1)                                               #Se imprime nuevamente la lista para comprobar que se pasa por referencia.