#Creator: Paul Bauer
# 20210060

# Enunciado 2
# Declare a structure POINT. Input the coordinates of a point cariable and determine
# the audrant in which it lies.

def Runner():
      x = PuntoX()
      
      y = PuntoY(x)
      
      Tabla()
      
      Cuadro = Quadrant(x, y)
# </Def Runner>




def PuntoX():
      print("Ingrese el valor x:")
      x = int(input())
      
      return(x)
# </Def PuntoX>



def PuntoY(x):
      print("Ingrese el valor y:")
      y = int(input())
      
      print("Usted acaba de crear el punto (", x, "; ", y, ")", sep='')
      
      return(y)
# </Def PuntoY>




def Tabla():
      print("")
      print("Usaremos la tabla siguiente para definir en que cuadrado queda su punto.")
      print("Cuadrado 1: (+ ; +)")
      print("Cuadrado 2: (- ; +)")
      print("Cuadrado 3: (- ; -)")
      print("Cuadrado 4: (+ ; -)")
# </Def Tabla>




def Quadrant(x, y):
      print("")
      print("Su punto queda en el cuadrado", end=" ")
      
         #Cuadro 1
      if (x >= 0):
            if (y >= 0):
                  print("1 !")
                  final = 1
            # </ If y >= 0 >
      # </ If x >= 0 >
      
      
         #Cuadro 2
      if (x < 0):
            if (y >= 0):
                  print("2 !")
                  final = 2
            # </ If y >= 0 >
      # </ If x < 0 >
      
      
         #Cuadro 3
      if (x < 0):
            if (y < 0):
                  print("3 !")
                  final = 3
            # </ If y < 0 >
      # </ If x < 0 >
      
      
         #Cuadro 4
      if (x >= 0):
            if (y < 0):
                  print("4 !")
                  final = 4
            # </ If y < 0 >
      # </ If x >= 0 >
      
      
      return(final) #Sirve para la prueba unitaria.
# </Def Quadrant>


























































#Fin.