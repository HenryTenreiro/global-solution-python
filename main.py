import cadastro_usuario
import valida_informacoes

print("Olá, seja bem vindo ao nosso sistema")
print("Aqui vamos te ajudar a se manter hidratado :D")
usuario = []

while True:
    print("Por favor, escolha uma opção abaixo (apenas numeros)")
    print("1 - Me cadastrar\n"
          "2 - Ver quantidade de agua que devo tomar\n"
          "3 - Ver bons hábitos para manter uma hidratação\n"
          "4 - Ver maus hábitos para se manter hidratado\n"
          "5 - Mostrar minha informações de cadastro\n"
          "6 - Sair")
    opcao = input()
    match opcao:
        case "1":
            usuario = cadastro_usuario.cadastrar_usuario()
        case "2":
            while True:
                print("Ver informações de um usuario cadastrado ? (Digite apenas numeros)")
                print("1 - sim\n"
                      "2 - não\n"
                      "3 - sair do menu")
                verificar_cadastro = input()
                match verificar_cadastro:
                    case "1":
                        if len(usuario) == 0:
                            print("Não existe nenhum usuario cadastrado !")
                        else:
                            print(f"Quantidade de agua que precisa tomar em litros : {usuario[2] / 1000} litros")
                            print(f"Seria o equivalente há {usuario[2] / 250} copos de agua de 250 ml")
                            print("Retornando ao menu...")
                    case "2":
                        while True:
                            peso = valida_informacoes.valida_peso()
                            quantidade_agua = peso * 35
                            print(f"A quantidade de agua seria : {quantidade_agua / 1000:.2f} litros")
                            print(f"Seria o equivalente há {quantidade_agua / 250} copos de 250 ml")
                            print("Deseja ver a recomendação de outra pessoa ? (digite apenas numeros)")
                            print("1 - sim\n"
                                  "2 - não")
                            quer_ver = input()
                            match quer_ver:
                                case "1":
                                    continue
                                case "2":
                                    print("Vamos voltar ao menu")
                                    print("--------------------------------")
                                    break
                                case _:
                                    print("Por favor, escolha uma opção valida!")
                    case "3":
                        print("Retornando ao menu principal")
                        print("-----------------------------")
                        break
                    case _:
                        print("Por favor, escolha uma opção valida")
        case "3":
            print("Não substitua a água por outras bebidas para se hidratar")
            print("Beber água antes e após as refeições")
            print("Consumir frutas e vegetais ricas em água")
            print("Saiba mais em https://www.bbc.com/portuguese/articles/c3gzp123yy0o")
        case "4":
            print("ingestão de álcool ou café")
            print("substituir água por isotônico")
            print("ingerir água somente quando sente sede")
            print("Saiba mais em https://www.bbc.com/portuguese/articles/c3gzp123yy0o")
        case "5":
            if len(usuario) == 0:
                print("não tem nenhum usuario Cadastrado")
            else:
                print(usuario)
        case "6":
            break
