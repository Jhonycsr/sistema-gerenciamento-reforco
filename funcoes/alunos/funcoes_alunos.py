from time import sleep

def validar_alunos(prompt, eh_telefone=False):
    while True:
        sleep(1)
        frase = input(prompt).strip()

        if len(frase) == 0:
            sleep(1)
            print("ERRO! Por favor, preencha os campos corretamente.")
            continue

        if eh_telefone and (len(frase) != 9 or not frase.isdigit()):
            sleep(1)
            print("ERRO! Telefone precisa conter 9 dígitos númericos.")
            continue
        return frase


def mostrar_dados_alunos(nome, info):
    sleep(1)
    print("-" * 40)
    print(f"Nome: {nome}\nResponsável: {info['Responsável']}\nTelefone: {info['Telefone']}\nSérie: {info['Série']}\nEscola: {info['Escola']}")
    print("-" * 40)



def cadastrar_aluno(alunos):
    sleep(1)
    nome = validar_alunos("Nome: ").title().strip()
    if nome not in alunos:
        sleep(1)
        responsavel = validar_alunos("Responsável: ").title().strip()
        telefone = validar_alunos("Telefone: ", eh_telefone=True).strip()
        serie = validar_alunos("Série: ").strip()
        escola = validar_alunos("Escola: ").strip()
        alunos[nome] = {"Responsável": responsavel, "Telefone": telefone, "Série": serie, "Escola": escola}
        sleep(1)
        print(f"Aluno {nome} cadastrado com sucesso!")
    else:
        sleep(1)
        print("Nome já cadastrado!")


def mostrar_alunos(alunos):
    if alunos:
        for n, info in alunos.items():
            mostrar_dados_alunos(n, info)
    else:
        sleep(1)
        print("ERRO! Cadastre alunos primeiro.\n")


def buscar_aluno(alunos):
    sleep(1)
    buscar = str(input("Nome do aluno: ")).strip().title()
    encontradas = [nom for nom in alunos if nom.startswith(buscar)]

    if len(encontradas) > 0:
        sleep(1)
        print(f"\nOpções encontradas: {encontradas}")

        sleep(1)
        escolha = str(input("\nDigite o nome completo do aluno que deseja ver: ")).strip().title()

        if escolha in alunos:
            info = alunos[escolha]
            mostrar_dados_alunos(escolha, info)
        else:
            sleep(1)
            print("ERRO! Esse aluno não está na lista de opções.")
    else:
        sleep(1)
        print("Nenhum aluno encontrado com esse início de nome.\n")


def editar_aluno(alunos):
    sleep(1)
    nome_aluno = validar_alunos("Nome: ").title().strip()

    if nome_aluno in alunos:
        info = alunos[nome_aluno]
        mostrar_dados_alunos(nome_aluno, info)
        sleep(1)
        esc_edit = input("Alterar: ").lower().strip()
        if esc_edit == "responsável":
            sleep(1)
            new_resp = validar_alunos("Digite o novo Responsável: ").title()
            alunos[nome_aluno]["Responsável"] = new_resp
            sleep(1)
            print("Responsável atualizado com sucesso!")

        elif esc_edit == "telefone":
            sleep(1)
            new_tel = validar_alunos("Digite o novo Telefone: ", eh_telefone=True)
            alunos[nome_aluno]["Telefone"] = new_tel
            sleep(1)
            print("Telefone atualizado com sucesso!")

        elif esc_edit == "série":
            sleep(1)
            new_ser = validar_alunos("Digite a nova Série: ")
            alunos[nome_aluno]["Série"] = new_ser
            sleep(1)
            print("Série atualizada com sucesso!")

        elif esc_edit == "escola":
            sleep(1)
            new_sch = validar_alunos("Digite a nova Escola: ")
            alunos[nome_aluno]["Escola"] = new_sch
            sleep(1)
            print("Escola atualizada com sucesso!")

        else:
            sleep(1)
            print("ERRO! Opção Inválida.")

    else:
        sleep(1)
        print("Aluno não encontrado, tente o nome completo!")


def remover_aluno(alunos):
    sleep(1)
    nome_aluno = validar_alunos("Nome: ").title()

    if nome_aluno in alunos:
        info = alunos[nome_aluno]
        sleep(1)
        print("Aluno encontrado: ")
        mostrar_dados_alunos(nome_aluno, info)
        sleep(1)
        esc_remove = input("Deseja realmente remover? [S/N]: ").upper().strip()
        if esc_remove == "S":
            del alunos[nome_aluno]
            sleep(1)
            print("Aluno removido com sucesso!")

        if esc_remove not in "SN":
            sleep(1)
            print("ERRO! Respostas válidas: [S/N]")
    else:
        sleep(1)
        print("Aluno não encontrado, tente o nome completo!")


def mostrar_tabela_opcoes_alunos():
    sleep(1)
    print("""    1 - Cadastrar aluno
    2 - Ver alunos
    3 - Buscar aluno
    4 - Editar aluno
    5 - Remover aluno
    0 - Voltar para o Menu""")
