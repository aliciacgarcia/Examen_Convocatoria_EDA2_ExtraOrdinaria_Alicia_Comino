class ArtefactosValiosos:
    def init(self, peso: float, nombre: str, precio: float, fecha_caducidad: str) -> None:
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad
    print("Artefacto valioso creado con éxito: {}".format(self.nombre))

    def __str__(self) -> str:
        return "Nombre: {}\npeso: {} kg\nprecio: {}\nfecha de caducidad: {}".format(self.nombre, self.peso, self.precio, self.fecha_caducidad)

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