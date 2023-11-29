import valida_informacoes
# funcao cadastrar_usuario criada para cadastrar o usuario
def cadastrar_usuario():
    usuario = []
    while True:
        print("Vamos começar o cadastro de usuario")
        nome = valida_informacoes.valida_nome()
        usuario.append(f"Nome: {nome}")
        peso = valida_informacoes.valida_peso()
        usuario.append(f"Peso em kg: {peso}")
        print("Confirma informações ? ")
        print(usuario[0])
        print(usuario[1])
        print("----------")
        print("1 - sim\n"
              "2 - não")
        # case 1: informação aceita e retornara para o usuario
        # case 2: informação invalida, retornará para coletar novas informações
        # case _: informação coloca no imput foi constatada invalida e dará retornará para escolher uma opçaõ valida (1 ou 2).
        opcao = input()
        match opcao:
            case "1":
                print("Cadastrado finalizado, retornado ao menu principal :D")
                print("-----------------------------------------------------")
                usuario.append(peso * 35)
                return usuario
            case "2":
                print("Retornando ao começo para colocar novas informações....")
                usuario.clear()
            case _:
                print("Por favor, escolha uma opção valida!")


