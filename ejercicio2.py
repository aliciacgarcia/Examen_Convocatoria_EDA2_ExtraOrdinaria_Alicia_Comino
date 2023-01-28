
class Nombre:

    def __init__(self, id_ciherente, id_siglo, id_armadura, numero_escuadra) -> None:
        self.id_ciherente = id_ciherente
        self.id_siglo = id_siglo
        self.id_armadura = id_armadura
        self.numero_escuadra = numero_escuadra

    def __str__(self) -> str:
        return "{}-{}{}{}{}".format(self.id_ciherente, self.id_siglo, self.id_armadura, self.numero_escuadra)



class armaduras(Nombre):

    def __init__(self, id_ciherente, id_siglo, id_armadura, numero_escuadra, rango) -> None:
        super().__init__(id_ciherente, id_siglo, id_armadura, numero_escuadra)
        self.nombre = super().__str__()
        self.rango = rango
        print("Stormtrooper creado con nombre {} y rango {}".format(self.nombre, self.rango))


    def __str__(self)-> str:
        return "Nombre de la armadura: {} Rango: {}".format(self.nombre, self.rango)

    def calificacion(self):
        if self.rango == "Alta":
            print(f"La armadura {self.nombre} es de alta calidad")
        elif self.rango == "Media":
            print(f"La armadura {self.nombre} es de calidad media")
        else:
            print(f"La armadura {self.nombre} es de baja calidad")



# Ejemplo creando objetos para probar la calificacion 

lista_armaduras = []
armadura_1 = armaduras("MK",8,6,5,6,"oficial")
armadura_2 = armaduras("MK",5,6,4,7,"oficial")
lista_armaduras.append(armadura_1)
lista_armaduras.append(armadura_2)
for armadura in lista_armaduras:
    print(armadura)