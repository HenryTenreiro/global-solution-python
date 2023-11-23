import valida_informacoes
def cadastrar_usuario():
    usuario = []
    while True:
        print("Vamos começar o cadastro de usuario")
        nome = valida_informacoes.valida_nome()
        usuario.append(f"Nome: {nome}")
        peso = valida_informacoes.valida_peso()
        usuario.append(f"Peso: {peso}")
        print("Deseja arrumar as informações ? ")
        print(usuario)
        print("1 - sim\n"
              "2 - não")
        opcao = input()
        match opcao:
            case "1":
                print("Retornando ao começo....")
                usuario.clear()
            case "2":
                usuario.append(peso * 35)
                print("Cadastrado finalizado, retornado ao menu principal :D")
                print("-----------------------------------------------------")
                return usuario
            case _:
                print("Por favor, escolha uma opção valida!")


