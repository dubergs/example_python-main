#Tarifas del hotelWC
categoria = {
    "individual": 2500,
    "doble": 4600,
    "familiar": 5200,
}
print(categoria)

#Proceso de hospedaje
dias = 4
price = dias * categoria["individual"]
print("Su categoria es individual:")
print("Su valor total por sus dias de hospedaje es:", price)

#Valor con iva
iva = 16
aumentar = price * (iva / 100)
aumentado = price + aumentar
print("Nuevo valor con iva:")
print(aumentado)

#Descuento con iva
descuento = 5
print("Se te hara un descuento del 5%:")
proceso = aumentado * (descuento / 100)
disminucion = aumentado - proceso
print("Valor con descuento:")
print(disminucion)



