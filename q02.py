# 2- Escreva um programa em Python que imprima os números ímpares de 1 a 20.
impares =[]
for n in range(21):
  if n%2 !=0:
    impares.append(n)
print(impares)
