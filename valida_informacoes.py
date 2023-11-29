# funções criada para cadastrar o peso e nome do usuario.
def valida_peso():
    while True:
        try:
            peso = float(input("Digite o peso do usuario em kg(kilogramas): "))
        except ValueError:
            print("Por favor, digite apenas numeros !")
            continue
        else:
            if peso < 0 or peso > 400:
                print("Por favor, digite um valor de peso válido !")
                continue
            else:
                return peso


def valida_nome():
    while True:
        nome = input("Digite o primeiro nome do usuario: ")
        if not (nome.isalpha()):
            print("Digite um nome valido !")
            continue
        else:
            return nome