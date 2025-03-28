class Silla:
    def __init__(self, material, color, patas=4):        #la funcion contructora (cuando una nueva clase sea creada se guiara por estos terminos)  #se llama init porque se ejcuta cuando el programa se inicialice
        self.patas = patas
        self.material = material
        self.color = color
        self.ocupada = False

    def sentarse(self):
        if not self.ocupada:
            self.ocupada = True
            print("Te has sentado en la silla")
        else:
            print("La silla ya está ocupada")
    
    def levantarse(self):
        if self.ocupada:                             #Verifica si la silla está ocupada (if self.ocupada)
            self.ocupada = False                     #Si está ocupada: Cambia el estado a no ocupada (self.ocupada = False)
            print("Te haz levantado")                #Imprime mensaje de confirmación
        else:                                        #Si no está ocupada:
            print("La silla ya está ocupada")        #Informa que ya estaba vacía

       

x = Silla("madera", "negro")
print(x.ocupada)                                     # False (inicialmente vacía)

x.sentarse()
x.sentarse()
x.levantarse()
x.levantarse()

silla_2 = Silla("plastico", "gris", 5)
print(silla_2.ocupada) 