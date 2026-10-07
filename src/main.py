hospedes = []

##Entrada de dados (input): Seu programa agora consegue conversar com quem está usando o teclado.##

def cadastrar_hospede():
    print("\n--- CADASTRO DE HÓSPEDE ---")
    nome = input("Digite o nome do hóspede: ")
    cpf = input("Digite o CPF do hóspede: ")
    idade = input("Digite a idade do hóspede: ")

##Organização (Dicionário {}): O sistema pega essas entradas e empacota em uma ficha estruturada (nome, cpf, idade).##

    novo_hospede = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade
    }

##Armazenamento (Lista [] + .append()): A ficha foi guardada na memória principal do projeto.##
    
    hospedes.append(novo_hospede)
    print(f" Hóspede {nome} cadastrado com sucesso!")

cadastrar_hospede()

def listar_hospedes():
    if len(hospedes) == 0:
        print("\nNenhum hóspede cadastrado ainda.")
        return

    print("\n--- LISTA DE HÓSPEDES ----")
    for hospede in hospedes:
        print(f"Nome: {hospede['nome']} | CPF: {hospede['cpf']} | Idade: {hospede['idade']}")

cadastrar_hospede()
listar_hospedes()


def buscar_hospede():
    print("\n--- BUSCAR HÓSPEDE ---")
    cpf_busca = input("Digite o CPF para busca: ")

    for hospede in hospedes:
        if hospede['cpf'] == cpf_busca:
            print(f"\n Hóspede Encontrado: {hospede['nome']} | Idade: {hospede['idade']}")
            return

    print("\n Nenhum Hóspede encontrado com esse CPF. ")
    
cadastrar_hospede()
listar_hospedes()
buscar_hospede()