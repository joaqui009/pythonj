
def carro_matheus():    
    print("peugeot 206 turbo")
    
carro_matheus()

def escrever_carro(nome):   
    print(nome)
    
escrever_carro("marea manual")

def somar_numeros(num1, num2):
    return num1 + num2

resultado = somar_numeros(4, 4)
print("o resultado é:", resultado)

def verificaidade(idade):   
    if idade >= 18:
        return "pode ver o filme"
    else:
        return "nao pode ver o filme"

print("digite sua idade")
idade = int(input())

resultado = verificaidade(idade)

print(resultado)