login_senha={
    "CLAUDIAAGUILAR":{"senha": "123456"},
    "PATRICKSOARES":{"senha": "789456"}
}

def validar_login(usuario, senha):
    cont = 0
    while(cont <4):
        usuario = usuario.upper()

        if usuario in login_senha and senha == login_senha[usuario]["senha"]:
            print("Bem Vindo ao Sistema!!!")
            break
        else:
            print("Login ou senhas erradas")
            cont +=1
            if cont <4:
                usuario=input("Digite seu login: ")
                usuario = usuario.upper()
                senha = int(input("Digite a sua senha: "))
            else:
                print("Você bloqueou a sua senha, entre em contato com o administrador!")


usuario=input("Digite seu login: ")
senha = input("Digite a sua senha: ")

validar_login(usuario,senha)