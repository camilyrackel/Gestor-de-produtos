# Sistema de Cadastro de Produtos

# Dicionário para armazenar os produtos
produtos = {}

def cadastrar_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = float (input("Digite o preço do produto: "))
    quantidade = int (input("Digite a quantidade em estoque: "))
    
    produtos[codigo] = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    print("\nLista de Produtos:")
    for codigo, produto in produtos.items():
        print(f"Código: {codigo}")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Quantidade em estoque: {produto['quantidade']}\n")

def editar_produto():
    codigo = input("Digite o código do produto que deseja editar: ")
    if codigo in produtos:
        nome = input("Digite o novo nome do produto: ")
        preco = float(input("Digite o novo preço do produto: "))
        quantidade = int(input("Digite a nova quantidade em estoque: "))
        
        produtos[codigo]["nome"] = nome
        produtos[codigo]["preco"] = preco
        produtos[codigo]["quantidade"] = quantidade
        print("Produto editado com sucesso!")
    else:
        print("Produto não encontrado.")

def excluir_produto():
    codigo = input("Digite o código do produto que deseja excluir: ")
    if codigo in produtos:
        del produtos[codigo]
        print("Produto excluído com sucesso!")
    else:
        print("Produto não encontrado.")

while True:
    print("\nSistema de Cadastro de Produtos")
    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Editar Produto")
    print("4. Excluir Produto")
    print("5. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        editar_produto()
    elif opcao == "4":
        excluir_produto()
    elif opcao == "5":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
