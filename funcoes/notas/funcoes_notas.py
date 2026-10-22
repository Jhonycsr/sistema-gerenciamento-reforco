from time import sleep

def mostrar_tabela_opcoes_notas():
    sleep(1)
    print("""    1 - Cadastrar Notas
    2 - Mostrar Notas Aluno
    3 - Editar Notas
    0 - Voltar para o Menu""")


def cadastrar_notas(alunos, trimestre, recuperacao):
    sleep(1)
    nome_aluno = input("Nome do aluno: ").title().strip()

    if nome_aluno in alunos:
        sleep(1)
        esc_cadastrar_notas = input("Deseja cadastradar as notas de algum trimestre ou de recuperação? [Trimestre / Recuperação]: ").lower().strip()

        if esc_cadastrar_notas == "trimestre":
            numeros_trimestres_validos = [1, 2, 3]
            
            while True:
                try:
                    sleep(1)
                    numero_trimestre = int(input("Digite o número do trimestre [1 / 2 / 3]: "))

                    if numero_trimestre in numeros_trimestres_validos:
                        break

                    else:
                        print("ERRO! Por favor, escolha um trimestre válido [1, 2 ou 3].")

                except ValueError:
                    sleep(1)
                    print("ERRO! Digite apenas números inteiros (1, 2 ou 3).")

            dados_trimestre = trimestre[numero_trimestre]

            if nome_aluno not in dados_trimestre:
                dados_trimestre[nome_aluno] = {}

            sleep(1)
            materia = input("Nome da matéria: ").title().strip()

            if materia not in dados_trimestre[nome_aluno]:
                sleep(1)
                print(f"Matéria {materia} não cadastrada no trimestre! Cadastrando agora...")
                dados_trimestre[nome_aluno][materia] = {}
            else:
                sleep(1)
                print("Matéria já cadastrada! Matendo informações anteriores...")

            while True:
                try:
                    sleep(1)
                    quant_notas = int(input("Quantidade de notas a serem digitadas: "))
                    if quant_notas > 0:
                        break
                    print("ERRO! Digite uma quantidade válida (pelo menos 1).")
                
                except ValueError:
                    sleep(1)
                    print("ERRO! Digite um número inteiro válido.")

            for num in range(1, quant_notas + 1):
                while True:
                    try:
                        sleep(1)
                        nota = float(input(f"Nota {num}: "))
                        if 0 <=  nota <= 10:
                            break
                        print("ERRO! A nota precisa estar entre 0 e 10.")

                    except ValueError:
                        sleep(1)
                        print("ERRO! Digite um número válido (ex: 8.5).")

                if 0 <= nota <= 10:
                    nome_da_nota = f"Nota {num}"

                    dados_trimestre[nome_aluno][materia][nome_da_nota] = nota

                else:
                    sleep(1)
                    print("Nota inválida!")

            sleep(1)
            print(f"Notas adicionadas com sucesso em {materia} do aluno {nome_aluno}!")

        elif esc_cadastrar_notas == "recuperação" or esc_cadastrar_notas == "recuperacao":
            if nome_aluno not in recuperacao:
                recuperacao[nome_aluno] = {}

            sleep(1)
            materia = input("Nome da matéria: ").title().strip()

            if materia not in recuperacao[nome_aluno]:
                sleep(1)
                print(f"Matéria {materia} não cadastrada na recuperação! Cadastrando agora...")
                recuperacao[nome_aluno][materia] = {}
            else:
                sleep(1)
                print("Matéria já cadastrada! Matendo informações anteriores...")

            while True:
                try:
                    sleep(1)
                    nota_recuperacao = float(input(f"Digite a nota da recuperação para {nome_aluno}: "))
                    if 0 <= nota_recuperacao <= 10:
                        break
                    print("ERRO! A nota precisa estar entre 0 e 10.")

                except ValueError:
                    sleep(1)
                    print("ERRO! Digite um número válido (ex: 8.5).")

            if 0 <= nota_recuperacao <= 10:
                recuperacao[nome_aluno][materia] = nota_recuperacao
                sleep(1)
                print(f"Nota de recuperação em {materia} adicionada para {nome_aluno}.")
            else:
                sleep(1)
                print("Nota inválida!")

        else:
            sleep(1)
            print("Opção Inválida!")

    else:
        sleep(1)
        print("ERRO! Aluno não cadastrado.")


def mostrar_dados_notas(nome_aluno, trimestre, recuperacao):
    tem_notas = False
    sleep(1)
    print("=" * 40)
    print(f"Aluno: {nome_aluno}")
    print('=' * 40)
    for num_trimeste, dados_trimeste in trimestre.items():
        if nome_aluno in dados_trimeste:
            tem_notas = True
            sleep(1)
            print(f"\n--- Trimestre {num_trimeste} ---")
            materias = dados_trimeste[nome_aluno]
            for materia, notas in materias.items():
                sleep(1)
                print(f"\nMatéria: {materia}")
                if len(notas) > 0:
                    media = sum(notas.values()) / len(notas)
                    sleep(1)
                    print(f"  Média: {media:.1f}")
                else:
                    sleep(1)
                    print("  Média: N/A (sem notas)")
                for nome_nota, valor_nota in notas.items():
                    sleep(1)
                    print(f"  • {nome_nota}: {valor_nota}")
                

    if nome_aluno in recuperacao:
        tem_notas = True
        sleep(1)
        print(f"\n--- Recuperação ---")
        materias = recuperacao[nome_aluno]
        for materia, notas in materias.items():
            sleep(1)
            print(f"\nMatéria: {materia}")
            sleep(1)
            print(f"  • Nota Recuperação: {notas}")

    if not tem_notas:
        sleep(1)
        print("Nenhuma nota registrada para este aluno.")
    


def mostrar_notas(alunos, trimestre, recuperacao):
    sleep(1)
    nome_aluno = input("Nome do aluno: ").title().strip()

    if nome_aluno in alunos:
        mostrar_dados_notas(nome_aluno, trimestre, recuperacao)
    else:
        sleep(1)
        print("ERRO! Aluno não cadastrado.")

        
def editar_notas(alunos, trimestre, recuperacao):
    sleep(1)
    nome_aluno = input("Deseja editar as notas do aluno: ").title().strip()

    if nome_aluno in alunos:
        mostrar_dados_notas(nome_aluno, trimestre, recuperacao)
        sleep(1)
        esc_trimestre_ou_recuperacao = input("Deseja alterar as notas de um trimestre ou da recuperação? [trimestre / recuperação]: ").lower().strip()
        
        if esc_trimestre_ou_recuperacao == "trimestre":
            trimestes_validos = [1, 2, 3]

            while True:
                try:
                    sleep(1)
                    esc_trimestre = int(input("Escolha o trimestre [1 / 2 / 3]: "))

                    if esc_trimestre in trimestes_validos:
                        break
                    else:
                        print("ERRO! Por favor, escolha um trimestre válido [1, 2 ou 3].")

                except ValueError:
                    sleep(1)
                    print("ERRO! Digite apenas números inteiros (1, 2 ou 3).")
            

            dados_trimestre = trimestre[esc_trimestre]
            if nome_aluno in dados_trimestre:
                materias = dados_trimestre[nome_aluno]

                sleep(1)
                materia = input("Diga o nome da matéria que deseja alterar a nota: ").title().strip()

                if materia in materias:
                    notas_materia = dados_trimestre[nome_aluno][materia]
                    for nome_nota, valor_nota in notas_materia.items():
                        sleep(1)
                        print(f"  • {nome_nota}: {valor_nota}")

                    sleep(1)
                    esc_nome_nota = input("Digite qual nota deseja selecionar [ex: Nota 1]: ").title().strip()

                    if esc_nome_nota in notas_materia:
                        sleep(1)
                        esc_editar_ou_excluir = input("Deseja editar ou excluir a nota? [editar / excluir]: ").lower().strip()

                        if esc_editar_ou_excluir == "editar":
                            while True:
                                try:
                                    sleep(1)
                                    nova_nota = float(input("Digite o valor da nova nota: "))
                                    if 0 <= nova_nota <= 10:
                                        break
                                    else:
                                        print("ERRO! A nota precisa estar entre 0 e 10.")

                                except ValueError:
                                    sleep(1)
                                    print("ERRO! Digite um número válido (ex: 8.5).")
                            
                            if 0 <= nova_nota <= 10:
                                notas_materia[esc_nome_nota] = nova_nota
                                sleep(1)
                                print("Nota alterada com sucesso!")

                        elif esc_editar_ou_excluir == "excluir":
                            del notas_materia[esc_nome_nota]
                            sleep(1)
                            print(f"{esc_nome_nota} removida com sucesso!")

                        else:
                            sleep(1)
                            print("Erro! Digite um opção válida.")


                        if len(notas_materia) == 0:
                            del dados_trimestre[nome_aluno][materia]
                            sleep(1)
                            print(f"Como não restaram notas, a matéria {materia} foi removida deste trimestre")

        elif esc_trimestre_ou_recuperacao == "recuperacao" or esc_trimestre_ou_recuperacao == "recuperação":
            if nome_aluno in recuperacao:
                materias = recuperacao[nome_aluno]

                sleep(1)
                materia = input("Diga o nome da matéria que deseja alterar a nota: ").title().strip()

                if materia in materias:
                    nota_materia = recuperacao[nome_aluno][materia]

                    sleep(1)
                    print(f"\nMatéria: {materia}")
                    sleep(1)
                    print(f"  • Nota Recuperação: {nota_materia}")

                    sleep(1)
                    esc_editar_ou_excluir = input("Deseja editar ou excluir a nota? [editar / excluir]: ").lower().strip()

                    if esc_editar_ou_excluir == "editar":

                        while True:
                            try:
                                sleep(1)
                                nova_nota = float(input("Digite o valor da nova nota: "))
                                if 0 <= nova_nota <= 10:
                                    break
                                else:
                                    print("ERRO! A nota precisa estar entre 0 e 10.")

                            except ValueError:
                                sleep(1)
                                print("ERRO! Digite um número válido (ex: 8.5).")

                        if 0 <= nova_nota <= 10:
                            recuperacao[nome_aluno][materia] = nova_nota
                            sleep(1)
                            print("Nota alterada com sucesso!")

                    elif esc_editar_ou_excluir == "excluir":

                        del recuperacao[nome_aluno][materia]
                        sleep(1)
                        print(f"Nota removida com sucesso!")
                        sleep(1)
                        print("Como não resta mais notas nesta matéria, ela também foi removida da recuperação!")

                    else:
                        sleep(1)
                        print("ERRO! Digite uma opção válida.")



                else:
                    sleep(1)
                    print("Matéria não encontrada para este aluno neste trimestre.")


        else:
            sleep(1)
            print(f"O aluno {nome_aluno} não possui notas registradas")

    else:
        sleep(1)
        print("ERRO! Aluno não cadastrado!")