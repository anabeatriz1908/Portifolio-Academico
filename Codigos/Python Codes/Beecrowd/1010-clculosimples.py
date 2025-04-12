codigo1, num1, valoruni1 = input().split(" ")
codigo2, num2, valoruni2 = input().split(" ")

codigo1= int(codigo1)
num1= int(num1)
valoruni1= float(valoruni1)

codigo2= int(codigo2)
num2 = int(num2)
valoruni2 = float(valoruni2)

valor= (num1*valoruni1) + (num2*valoruni2)

print(f"VALOR A PAGAR: R$ {valor:.2f}")
