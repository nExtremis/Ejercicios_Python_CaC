#creamos banderas para las validaciones
flagNombre = 0
flagEdad = 0
flagDni = 0

class Persona:
    def __init__(self,nombre,edad,dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    #getters
    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    @property
    def dni(self):
        return self.__dni
    
    #setter
    @nombre.setter
    def nombre(self,nombre):
        global flagNombre #variable global para poder modificarla desde la clase
        if isinstance(nombre, str):
            if nombre.isalpha():
                
                flagNombre=0
                self.__nombre =  nombre
            else:
                flagNombre = 1
                print("no es un nombre valido")
                    
        else:
            flagNombre = 1
            print("No es el tipo de dato correcto.")
            
    @edad.setter
    def edad(self,edad):
        global flagEdad #variable global para poder modificarla desde la clase
        edadInt = int(edad)
        if int(edad):
            
            if edadInt > 0 and edadInt < 100 :
                flagEdad=0
                self.__edad =  edadInt
            else:
                flagEdad = 1
                print("no es un edad valida")
                    
        else:
            flagEdad = 1
            print("No es el tipo de dato correcto.")

    @dni.setter
    def dni(self,dni):
        global flagDni #variable global para poder modificarla desde la clase
        if int(dni):
            print("if")
            dniStr= str(dni)
            if len(dniStr) == 8 :
                flagDni=0
                self.__dni =  dni
            else:
                flagDni = 1
                print("Dni invalido") 
                    
        else:
            flagDni = 1
            print("No es el tipo de dato correcto.")
            
    
    def mostrar(self):
        return f"nombre:{self.__nombre}\n edad:{self.__edad}\n dni:{self.__dni}"
    
    
    def Es_mayor_de_edad(self):
        if self.__edad >=18 :
            return True
        else:
            return False
        
 ## faltan setters y las validaciones       

    

class Cuenta:
    def __init__(self,titular="",cantidad = 0):
        self.__titular = titular
        self.__cantidad = cantidad
    @property
    def titular(self):
        return  self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self,titular):
        if titular.isalpha():
            self.__titular = titular
        else:
            flag = 1
            print("Error.Vuelva a ingresar") 



    def mostrar(self):
        return f"titular : {self.__titular} \ncantidad: {self.__cantidad}"

    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad

    def retirar(self,cantidad):
        self.__cantidad = self.__cantidad - cantidad    

p1 = Persona("gonzalo",29,38354532)

p1.nombre = input("ingrese su nombre")
while flagNombre == 1:
    p1.nombre = input("ingrese su nombre")
    print(flagNombre)

p1.edad = input("ingrese su edad")     
while flagEdad == 1:
    p1.edad = input("ingrese su edad")  

p1.dni = input("ingrese su dni")      
while flagDni == 1:
    p1.dni = input("ingrese su dni")


print(p1.nombre)
print(p1.edad)
print(p1.dni)
input("Press any key to finalize script")  