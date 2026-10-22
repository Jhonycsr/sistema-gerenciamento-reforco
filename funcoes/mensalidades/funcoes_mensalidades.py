from time import sleep


def mostrar_tabela_opcoes_mensalidades():
    sleep(1)
    print("""    1 - Cadastrar Mensalidades
    2 - Registrar Pagamento
    3 - Consultar Mensalidades
    4 - Relátorio de pendentes
    0 - Voltar para o Menu""")


def cadastrar_mensalidades(alunos, mensalidades):
    sleep(1)
    nome_aluno = input("Nome do aluno: ").title().strip()

    if nome_aluno in alunos:
        if nome_aluno not in mensalidades:
            mensalidades[nome_aluno] = {}

        sleep(1)
        mes_mensalidade = input("Digite o mês da mensalidade (ex: Janeiro): ").title().strip()
        if mes_mensalidade in mensalidades[nome_aluno]:
            sleep(1)
            print("ERRO: A mensalidade desse mês já foi gerada!")

        else:
            sleep(1)
            while True:
                try:
                    valor_total = float(input("Digite o valor da mensalidade: R$ "))
                    if valor_total > 0:
                        break
                    print("ERRO! O valor deve ser maior que zero.")
                except ValueError:
                    print("ERRO! Por favor, digite um valor numérico válido (ex 150.00)")



            mensalidades[nome_aluno][mes_mensalidade] = {
            "Valor Total": valor_total,
            "Valor Pago": 0.0,
            "Status": "Pendente"
        }

            sleep(1)
            print("Mensalidade cadastrada com sucesso!")
    else:
        sleep(1)
        print("ERRO! Aluno não cadastrado.")


def registrar_pagamento_mensalidade(alunos, mensalidades):
    sleep(1)
    nome_aluno = input("Nome do aluno: ").title().strip()

    if nome_aluno in alunos:
        if nome_aluno in mensalidades and mensalidades[nome_aluno]:
            sleep(1)
            mes_mensalidade = input("Digite o mês de mensalidade (ex: Janeiro): ").title().strip()


            if mes_mensalidade in mensalidades[nome_aluno]:
                dados_mes = mensalidades[nome_aluno][mes_mensalidade]

                if dados_mes["Status"] == "Pago":
                    sleep(1)
                    print("Este mês já possui mensalidade paga!")

                else:
                    sleep(1)
                    falta_pagar = dados_mes["Valor Total"] - dados_mes["Valor Pago"]
                    sleep(1)
                    print(f"Falta pagar R${falta_pagar} neste mês!")

                    sleep(1)
                    while True:
                        try:
                            valor_recebido = float(input("Valor a ser pago: R$ "))
                            if valor_recebido > 0:
                                break
                            print("ERRO! O valor pago deve ser maior que zero.")
                        except ValueError:
                            print("ERRO! Por favor, digite um valor numérico válido (ex: 150.00)")

                
                    if valor_recebido > falta_pagar:
                        dados_mes["Valor Pago"] = dados_mes["Valor Total"]
                        dados_mes["Status"] = "Pago"

                        troco = valor_recebido - falta_pagar
                        sleep(1)
                        print(f"Pagamento quitado! Troco: R$ {troco}")

                    elif valor_recebido == falta_pagar:
                        dados_mes["Valor Pago"] += valor_recebido
                        dados_mes["Status"] = "Pago"
                        sleep(1)
                        print("Pagamento quitado com sucesso!")

                    else:
                        dados_mes["Valor Pago"] += valor_recebido
                        dados_mes["Status"] = "Parcial"
                        novo_saldo = dados_mes["Valor Total"] - dados_mes["Valor Pago"]
                        sleep(1)
                        print(f"Pagamento parcial registado. Ainda faltam R${novo_saldo} para quitar este mês.")

            else:
                sleep(1)
                print(f"ERRO: mensalidade para o mês {mes_mensalidade} não encontrada!")

        else:
            sleep(1)
            print(f"Nenhuma mensalidade gerada para o aluno {nome_aluno}!")

    else:
        sleep(1)
        print("ERRO: Aluno não cadastrado!")

        
def consultar_mensalidades(alunos, mensalidades):
    sleep(1)
    nome_aluno = input("Nome do aluno: ").title().strip()

    if nome_aluno in alunos:
        if nome_aluno in mensalidades and mensalidades[nome_aluno]:
            sleep(1)
            print("=" * 40)
            print(f"Extrato de Mensalidades = {nome_aluno}")
            print("=" * 40)

            for mes, dados in mensalidades[nome_aluno].items():
                sleep(1)
                print(f"\n--- Mês: {mes} ---")
                print(f"  • Valor Total: R$ {dados['Valor Total']:.2f}")
                print(f"  • Valor Pago: R$ {dados['Valor Pago']:.2f}")

                if dados["Status"] != "Pago":
                    falta = dados["Valor Total"] - dados["Valor Pago"]
                    print(f"  • Restante: R$ {falta:.2f}")

                print(f"  • Status: {dados['Status']}")
            print("-" * 40)

        else:
            sleep(1)
            print(f"Nenhuma mensalidade gerada para o aluno {nome_aluno}")

    else:
        sleep(1)
        print("ERRO! Aluno não cadastrado.")


def mostrar_relatorio_pendentes(mensalidades):
    encontrou_pendencias = False

    sleep(1)
    print("=" * 45)
    print(f"{'RELATÓRIO DE MENSALIDADES PENDENTES':^45}")
    print("=" * 45)

    for nome_aluno, meses in mensalidades.items():
        tem_pendencia_aluno = False

        for mes, dados in meses.items():
            if dados["Status"] != "Pago":
                sleep(1)
                encontrou_pendencias = True

                if not tem_pendencia_aluno:
                    print(f"\nAluno: {nome_aluno}")
                    print("-" * 30)
                    tem_pendencia_aluno = True

                falta_pagar = dados["Valor Total"] - dados["Valor Pago"]
                print(f"  • Mês: {mes}")
                print(f"    - Status: {dados['Status']}")
                print(f"    - Valor Restante: R$ {falta_pagar:.2f}")

    if not encontrou_pendencias:
        sleep(1)
        print("\nNenhuma pendência encontrada! Todas as mensalidades estão em dia.")

    print("=" * 45)