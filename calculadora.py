

        
def menu():
    print("menu da calculadora")
    print("1 - Somar")
    print("2 - Subtrair")
    print("9 - Sair")
    
def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def verificaopcao(opcao):
    if opcao == 1:  
        num1 = float(input("digite o numero 1"))
        num2 = float(input("digite o numero 2"))
        print(subtrair(num1, num2))
    elif opcao == 2:
        num1 = float(input("digite o numero 1"))
        num2 = float(input("digite o numero 2"))
        print(subtrair(num1, num2))

def calculadora():  
    while True:
        menu()
        opcao = int(input("escolha uma opcao"))
        verificaopcao(opcao)
        
calculadora()