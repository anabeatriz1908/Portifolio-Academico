numeros_leds = {
    "1" : 2,
    "2" : 5,
    "3" : 5,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 3,
    "8" : 7,
    "9" : 6,
    "0" : 6
}

num_casos = int(input())
quantidade_leds = 0 
for i in range(num_casos):
    entrada_valor = input()
    for num in entrada_valor:
        if num == "1":
            quantidade_leds += numeros_leds["1"]
        elif num == "2":
            quantidade_leds += numeros_leds["2"]
        elif num == "3":
            quantidade_leds += numeros_leds["3"]
        elif num == "4":
            quantidade_leds += numeros_leds["4"]
        elif num == "5":
            quantidade_leds += numeros_leds["5"]
        elif num == "6":
            quantidade_leds += numeros_leds["6"]
        elif num == "7":
            quantidade_leds += numeros_leds["7"]
        elif num == "8":
            quantidade_leds += numeros_leds["8"]
        elif num == "9":
            quantidade_leds += numeros_leds["9"]
        else:
            quantidade_leds += numeros_leds["0"]
    print(f"{quantidade_leds} leds")
    quantidade_leds = 0
