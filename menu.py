from valoresminimos import runMinimos
from gato4x4 import iniciar_juego_gato


def menu():
	print("*** MENU ***")
	print("1.-Valores mínimos de la función")
	print("2.-Juego de gato de 4x4")
	print("3.-Salir")
	while True:
		opcion = int(input("Ingresa la opción deseada entre 1-3:"))
		if opcion >= 1 and opcion <=3:
			break
		else:
			print("Valor incorrecto")
	return opcion

if __name__ == "__main__": 
	opcion = menu()
	print(opcion)