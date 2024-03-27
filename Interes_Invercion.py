i = int(input("Seleccione tasa de interes: "))
c = int(input("Cuanto dinero queres invertir?"))
m = int(input("Cuantos tiempo quieres invertir tu dinero?: (Años)"))

c_total = c * (1 + (i/100)) ** m
print("Ingreso estimado de.", c_total)