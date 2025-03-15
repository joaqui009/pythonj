
def calcular_agua(peso):
    # A recomendação é 35 ml de água por kg de peso
    quantidade_agua = peso * 35
    return quantidade_agua

# Entrada do peso com verificação de erro
while True:
    try:
        peso = float(input("Digite o seu peso em kg: "))
        if peso <= 0:
            print("Por favor, digite um peso válido maior que zero.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")

# Calcular a quantidade de água necessária
agua_necessaria = calcular_agua(peso)

# Exibir o resultado
print(f"A quantidade de água que você deve beber por dia é: {agua_necessaria} ml")
