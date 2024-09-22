#asegurando que no se tome valor total en caso de que no se seleccione compra
total_palomitas = 0
total_bebidas = 0
#codigo
print("¿El comprador pertenece a DUOC?")
print("1.Si")
print("2.No")
opcion_duoc=int(input("ingrese su opción: "))
1==True
2==False
if opcion_duoc==1:
  print("Pertenece a DUOC")
elif opcion_duoc==2:
  print("No pertenece a DUOC")
print("")
print("")
print("¿Que entrada desea?")
print("1.Estreno: $4.800")
print("2.Normal: $2.900")
opcion_entrada=int(input("ingrese su opción: "))
if opcion_entrada==1:
  print("Estreno: $4.800")
elif opcion_entrada==2:
  print("Normal: $2.900")
cantidad_entrada=int(input("Ingrese la cantidad de entradas: "))
if opcion_entrada==1:
  total_entrada= cantidad_entrada*4800
  print("El valor de sus entradas: $", {total_entrada} )
elif opcion_entrada==2:
  total_entrada= cantidad_entrada*2900
  print("El valor de sus entradas: $", {total_entrada} )
print("")
print("")
print("¿desea agregar palomitas a su pedido?")
print("1.Si")
print("2.No")
opcion_palomitas=int(input("ingrese su opción: "))
if opcion_palomitas==1:
  print("Seleccione el tamaño de sus palomitas")
  print("1.Palomitas pequeñas $2.500")
  print("2.Palomitas medianas $4.500")
  print("3.Palomitas grandes $7.800")
  tamaño_palomitas=int(input("ingrese su opción: "))
  if tamaño_palomitas==1:
    print("A seleccionado palomitas pequeñas por $2.500")
  elif tamaño_palomitas==2:
    print("A seleccionado palomitas medianas por $4.500")
  else :
    print("A seleccionado palomitas grandes por $7.800")
  cantidad_palomitas=int(input("ingrese la cantidad que desea comprar: "))
  if tamaño_palomitas==1:
    total_palomitas=cantidad_palomitas*2500
  elif tamaño_palomitas==2:
      total_palomitas=cantidad_palomitas*4500
  else :
        total_palomitas=cantidad_palomitas*7800
  print("El valor de sus palomitas: $", total_palomitas )
elif opcion_palomitas==2:
  print("No desea palomitas")
print("")
print("")
print("Desea agregar bebidas a su pedido?")
print("1.Si")
print("2.No")
opcion_bebidas=int(input("ingrese su opción: "))
if opcion_bebidas==1:
  print("Seleccione el tamaño de sus bebidas")
  print("1.Bebidas pequeñas $1000")
  print("2.Bebidas medianas $1250")
  print("3.Bebidas grandes $2000")
  tamaño_bebidas=int(input("ingrese su opción: "))
  if tamaño_bebidas==1:
    print("A seleccionado bebidas pequeñas por $1000")
  elif tamaño_bebidas==2:
    print("A seleccionado bebidas medianas por $1250")
  else :
    print("A seleccionado bebidas grandes por $2000")
  cantidad_bebidas=int(input("ingrese la cantidad que desea comprar: "))
  if tamaño_bebidas==1:
    total_bebidas=cantidad_bebidas*1000
  elif tamaño_bebidas==2:
    total_bebidas=cantidad_bebidas*1250
  else :
    total_bebidas=cantidad_bebidas*2000
  print("El valor de sus bebidas es: $", total_bebidas )
elif opcion_bebidas==2:
  print("No desea bebidas")
print("")
print("")
if opcion_duoc==1:
  descuento_duoc=total_entrada*0.7
  print("El valor de sus entradas con descuento: $",round(descuento_duoc))
  total_descuento=descuento_duoc+total_palomitas+total_bebidas
  print("El valor total de su pedido es: $", round(total_descuento))
  print("Indique la cantidad de efectivo: ")
  efectivo=int(input())
  cambio_descuento=efectivo-total_descuento
  print("Su cambio es: $", round(cambio_descuento))
  print("Gracias por su compra")
else :
  total=total_entrada+total_palomitas+total_bebidas
  print("El valor total de su pedido es: $", total)
  print("Indique la cantidad de efectivo: ")
  efectivo=int(input())
  cambio=efectivo-total
  print("Su cambio es: $", round(cambio))
  print("Gracias por su compra")