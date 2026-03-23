NEGRITO = "\033[1m"
PISCAR = "\033[5m"
VERMELHO = "\033[31m"
RESET = "\033[0m"

login_senha={
    "CLAUDIAAGUILAR":{"senha": 123456},
    "PATRICKSOARES":{"senha": 789456}
}
estoque = {"Arroz":{"quantidade": 30, "preco": 25.40, "descricao": "Arroz Camil 5kg"},
           "Feijao":{"quantidade": 75, "preco": 9.80, "descricao": "Feijão Camil 1kg"}
           }

def validar_login(usuario, senha):
    cont = 0
    while(cont <3):
        usuario = usuario.upper()
        if usuario in login_senha and senha == login_senha[usuario]["senha"]:
            print("Bem Vindo ao Sistema!!!")
            return True 
        else:
            print("Login ou senhas erradas")
            cont +=1
            if cont <3:
                usuario=input("Digite seu login: ")
                usuario = usuario.upper()
                senha = int(input("Digite a sua senha: "))
            else:
                print("Você bloqueou a sua senha, entre em contato com o administrador!")
                return False

def programa_estoque():
    if validar_login(usuario, senha)== True:
        while True:
            aviso()
            print("""            XXXXXXXXXX--MENU--XXXXXXXXXX
                1 - Adicionar produto
                2 - Atualizar produto
                3 - Listar todos os produtos
                4 - Verificar estoque baixo
                5 - Relatório do estoque
                6 - Sair      
         """)
            opcao = int(input("Digite o número da opção desejada: "))
            if menu(opcao) == False:
                break


def aviso():
    for nome, dados in estoque.items():
        if dados["quantidade"]< 50:
            print(f"{NEGRITO} {VERMELHO} {PISCAR} O produto {nome} está com estoque baixo - disponível para venda ({dados['quantidade']} unidades) {RESET} \n" )

def menu(opcao):
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        print("Opção 2")
    elif opcao == 3:
        listar_produtos()
    elif opcao == 4:
        estoque_baixo()
    elif opcao == 5:
        rel_estoque()
    else:
        print("Saindo do programa...")
        return False
        

def cadastrar_produto():
    continuar = "S"
    while continuar == "S":
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        preco = float(input("Digite o preço: "))
        descricao = input("Digite a descrição: ")

        estoque[nome]={
            "quantidade": quantidade,
            "preco": preco,
            "descricao": descricao
        }
        continuar = input("Produto cadastrado com sucesso, se deseja cadastrar outro produto digite (S/N): ").upper()

def listar_produtos():
    if not estoque:
        print("Nenhum produto cadastrado.")
    else:
        print("\n--- Estoque ---")
        for nome, dados in estoque.items():
            print(f" Produto: {nome} - {dados['quantidade']} unidades - R${dados['preco']} - {dados['descricao']}")


def estoque_baixo():
    print("========Estoque baixo=========")
    print("Estoque não pode ser abaixo de 50 unidades para cada produto!")
    for nome, dados in estoque.items():
        if dados["quantidade"]< 50:
            print(f"Produto {nome} - ({dados['quantidade']} unidades) \n" )

def rel_estoque():
    print("========Relatório de Estoque =========")
    for nome, dados in estoque.items():
        total = dados['quantidade'] * dados['preco']
        print(f"Produto {nome} - ({dados['quantidade']} unidades) - R$({dados['preco']} ) - Valor total R${total} ")



usuario=(input("Digite seu login: "))
senha = int(input("Digite a sua senha: "))
 
programa_estoque()