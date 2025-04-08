listaProdutos = []
def cadastrarProduto(co):
    print("Bem-vindo ao cadastro de produtos.")
    print("O código do produto a ser cadastrado é: {}" .format(co))
    nome = input("Digite o nome do produto: ")
    fabricante = input("Digite o fabricante do produto: ")
    valor = float(input("Digite o valor do produto: "))
    dicionarioProduto = {'código': co,
                         'nome': nome,
                         'fabricante': fabricante,
                         'valor' : valor}
    listaProdutos.append(dicionarioProduto.copy())



def consultarProduto():
    while True:
        try:
            print("Bem-vindo a consulta de produtos.")
            opConsultar = int(input("Digite a opção desejada:\n"
                                    "1-Consultar todos os produtos\n"
                                    "2-Consultar por código\n"
                                    "3-Consultar por fabricante\n"
                                    "4-Retornar\n"
                                    ">>"))

            if opConsultar == 1:
                print("Bem-vindo a consulta de todos os produtos.")
                for produto in listaProdutos:
                    for key, value in produto.items():
                        print("{} : {}" .format(key, value))
            elif opConsultar == 2:
                print("Bem-vindo a consulta de produtos por código.")
                entrada = int(input("Digite o código do produto desejado: "))
                for produto in listaProdutos:
                    if(produto['código'] == entrada):
                        for key, value in produto.items():
                            print("{} : {}".format(key, value))
            elif opConsultar == 3:
                print("Bem-vindo a consulta de produtos por fabricante.")
                entrada = input("Digite o fabricante do produto desejado: ")
                for produto in listaProdutos:
                    if (produto['fabricante'] == entrada):
                        for key, value in produto.items():
                            print("{} : {}".format(key, value))
            elif opConsultar == 4:
                break
            else:
                print("A opção digitada não existe.")
                continue

        except ValueError:
            print("Pare de digitar valores que não são inteiros.")



def removerProduto():
    print("Bem-vindo a remoção de produtos.")
    entrada = int(input("Digite o código do produto que deseja remover: "))
    for produto in listaProdutos:
        if (produto['código'] == entrada):
            listaProdutos.remove(produto)



print("Bem vindo ao controle de estoque da mercearia do Adriano Rocha ")
registroProduto = 0
while True:
    try:
        opcao = int(input("Escolha a opção desejada:\n"
                          "1-Cadastrar Produto\n"
                          "2-Consultar Produto\n"
                          "3-Remover Produto\n"
                          "4- Sair"
                          "\n>>"))
        if opcao == 1:
            registroProduto += registroProduto + 1
            cadastrarProduto(registroProduto)
        elif opcao == 2:
            consultarProduto()
        elif opcao == 3:
            removerProduto()
        elif opcao == 4:
            print("Programa encerrado")
            break
        else:
            print("A opção não existe! Pare de digitar caracteres inválidos.")
            continue
    except ValueError:
        print("Pare de digitar valores que não são inteiros.")
