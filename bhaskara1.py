import math 

print("olá digite um número")
a = int(input())

print("Digite outro número")
b = int(input())

print("Agora digite o ultimo número para o calculo")
c = int(input())

Delta = b**2 - 4 * a * c

 
if Delta < 0:
    print("O Delta é negativo, não há raízes reais.")
else:
    raiz_Delta = math.sqrt(Delta)  # Calcula a raiz quadrada de Delta

    x1 = (-b + raiz_Delta) / (2 * a)  # Primeira raiz
    x2 = (-b - raiz_Delta) / (2 * a)  # Segunda raiz

    print("O resultado de x1 é:", x1)
    print("O resultado de x2 é:", x2)