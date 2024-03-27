def calcular_media_temperaturas(temperaturas):
    media = sum(temperaturas) / len(temperaturas)
    return media
def contar_temperaturas_superiores_o_iguales_a_media(temperaturas, media):
    count = sum(1 for temp in temperaturas if temp >= media)
    return count
def main():
    n = int(input("Ingrese la cantidad de temperaturas: "))
    temperaturas = []
    for i in range(n):
        temp = float(input(f"Ingrese la temperatura {i + 1}: "))
        temperaturas.append(temp)
    media = calcular_media_temperaturas(temperaturas)
    print("La media de las temperaturas es:", media)
    count = contar_temperaturas_superiores_o_iguales_a_media(temperaturas, media)
    print("Cantidad de temperaturas superiores o iguales a la media:", count)
if __name__ == "__main__":
    main()