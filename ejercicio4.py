class ArtefactosValiosos:
    def init(self, peso: float, nombre: str, precio: float, fecha_caducidad: str) -> None:
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad
    print("Artefacto valioso creado con éxito: {}".format(self.nombre))

    def __str__(self) -> str:
        return "Nombre: {}\npeso: {} kg\nprecio: {}\nfecha de caducidad: {}".format(self.nombre, self.peso, self.precio, self.fecha_caducidad)


def hijo_sin_amor(mochila, anillo_de_poder):
    if not mochila:
        return (False, 0)
    if mochila[0].nombre == anillo_de_poder:
        return (True, 1)
    else:
        resultado = hijo_sin_amor(mochila[1:], anillo_de_poder)
        return (resultado[0], resultado[1] + 1)

mochila = [ArtfactosValiosos(1, "Anillo de poder", 100, "2022-01-01"), ArtfactosValiosos(2, "Amuleto", 50, "2022-01-01"), ArtfactosValiosos(3, "Piedra preciosa", 75, "2022-01-01")]

resultado = hijo_sin_amor(mochila, "Anillo de poder")
if resultado[0]:
    print("Se encontro el anillo de poder en la mochila, se sacaron {} objetos antes de encontrarlo".format(resultado[1]))
else:
    print("No se encontro el anillo de poder en la mochila")

# creo objetos para  
artefacto1 = ArtefactosValiosos(2.5, "collar", 1000.0, "2022-12-31")
artefacto2 = ArtefactosValiosos(3.2, "jarron", 2000000.0, "2021-01-01")

print(artefacto1)
print(artefacto2) 

# ordeno por caducidad 
artefactos_valiosos = [artefacto1, artefacto2, ArtefactosValiosos(5.0, "Cuadro Picasso", 500.0, "2022-06-30")]

artefactos_valiosos_ordenados = sorted(artefactos_valiosos, key=lambda x: x.fecha_caducidad)

print("Artefactos valiosos ordenados por fecha de caducidad:")
for artefacto in artefactos_valiosos_ordenados:
    print(artefacto)

# altero el precio del artefacto 1
artefacto1.precio = 1500.0


