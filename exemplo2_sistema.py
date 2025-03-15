
# Sistema de desconto de veiculo 
# Solicite o nome do veiculo 
# E o preço do veiculo 
# se o preço > 80k -> 60% de desconto 
# Se o prço  > 50k -> 30% de desconto
# Se o preço > 30k -> Não existe desconto





veiculo = input("qual o nome do veiculo")

preço = float("80000")


if preço <= 80000:
    desconto = 0.6
elif preço > 50000:
    desconto = 0.3
else:
    desconto = 0
    
valor_final = preço * (1 - desconto)
    
print("veiculo: ", veiculo)
print("preço:", preço)
print("o preço do carro é de R$:", valor_final)
print("seu desconto é de:", desconto * 100, "%")


