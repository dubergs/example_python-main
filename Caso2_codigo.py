""
accion1 = "Ya identifique el proyecto a trabajar"
proyectoA = 1
hora = 10000
horas_diarias = 8
dias = 30 
sueldo_max = 1500000

print(accion1)

sueldo_diario = hora * horas_diarias
print("El salario diario es:")
print(sueldo_diario)

""
sueldo_mensual = sueldo_diario * dias
print("El salario mensual es:")
print(sueldo_mensual)

#
if sueldo_mensual > sueldo_max:
    print("Su salario es mayor al tope máximo")

if sueldo_mensual < sueldo_max:
    print("Se te incrementara un 6%")


    