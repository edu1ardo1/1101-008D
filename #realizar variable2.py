#realizar variable
#consultar saldo
saldo = 15000
#que desea pedir
while True:
    
print("bienvenido al local de sushi, elija un menu")

print("1. pikachu roll: $4500")

print("2. otaku roll: $5000")

print("3. pulpo venenoso roll: $5200")

print("4. anguila electrica roll: $4800")

print("5. salir")

#solicitar opcion al usuario
opcion = input("selecione una opcion(1-5): ")

#realizaracciones segun las opciones selecionadas 
if opcion =="1":
    print(f"tu saldo es de: ${saldo}")
elif opcion == "2":
    print(f"tu saldo es de: $10500")
elif opcion == "5":
    print(f"gracias por su compra.")

    