from src.controller import produto_controller
from src.controller import usuario_controller

def exibir_menu():
    print("\nMAREA TOCA TUDO LTDA!")
    print("\n==== MENU ====")
    print("1 - Cadastrar Produto")
    print("2 - Listar produto")
    print("3 - Atualizar Produto")
    print("4 - Deletar Produto")
    print("5 - Buscar Produto unico")
    print("6 - Cadastar Usuario")
    print("7 - Listar Usuario")
    print("8 - Atualizar Usuario")
    print("9 - Deletar Usuario")
    print("0 - Sair")
    
def listar_produtos():
    print("\n--- Lista de Produtos ---")
    produtos = produto_controller.listar_produtos()
    if produtos:
        for produto in produtos:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preco {produto['preco']}")
    else:
        print("Não existe produtos cadastrados")
        
def cadastrar_produto():
    print("\n--- Cadastrar produto---")
    nome = input("Digite o nome: ")
    preco = input("Digite o preco: ")
    novo_id = produto_controller.cadastrar_produto(nome, preco)
    print(f"produto cadastrado com sucesso com o novo id {novo_id}.")
    
def opcao_atualizar():
    print("\nATUALIZANDO O PRODUTO")
    produto_id = input("Dgite o ID do produto")
    nome = input("Digite o nome do prduto")
    preco = input("Digite o preco do produto")
    
    linhas = produto_controller.atualizar_produto(produto_id, nome, preco)    
    if linhas > 0:
        print("Produto atualizado com sucesso!")
    else:
        print("Nenhum produto foi atualizado")
        
def cadastrar_cliente():
    nome = input("Digite seu nome")
    idade = input("digite sua idade")
    Email = input("Digite o Email")
    novo_id = usuario_controller.atualizar_usuario (nome, Email, idade)
    print(f"Cliente cadastrado com sucesso!com o novo id {novo_id}.")
    
def listar_usuarios():
    print("\n--- Lista de Usuarios ---")
    usuarios = usuario_controller.listar_produtos()
    if usuarios:
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nome: {usuario['nome']},")
    else:
        print("Não existe produtos cadastrados")
        
            
# main -> Inicializar o projeto    
def main():
    # While True para repetir mesmo que a opção digitada esteja errada 
    while True:
        exibir_menu()
        opc = input("Escolha uma opção:")
        
        if opc == "1":
            cadastrar_produto()
        elif opc == "2":
            listar_produtos()
        elif opc == "3":
            opcao_atualizar()
        elif opc == "6":
            cadastrar_cliente()
        elif opc == "7":
            listar_usuarios
            
        elif opc == "0":
            print("Saindo do sistema...")
            # sys.exit(0)
        else:
            print("Opção Inválida, tente novamente...")  
            
if __name__ == '__main__':
    main()

                    