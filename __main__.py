from funcoes.alunos.funcoes_alunos import *
from funcoes.dados_e_menu_geral.funcoes_dados import *
from funcoes.dados_e_menu_geral.funcoes_menu_geral import *
from funcoes.mensalidades.funcoes_mensalidades import *
from funcoes.notas.funcoes_notas import *



alunos, trimestres, recuperacao, mensalidades = carregar_dados()



esc_principal = ""
while esc_principal != 0:
    mostrar_menu_geral()

    try:
        esc_principal = int(input("\nInforme sua escolha: "))
    except ValueError:
        print("\nERRO! Por favor, informe um número válido.")
        continue

    if esc_principal < 0 or esc_principal > 3:
        print("\nERRO! Informe uma escolha válida")
    else:
        if esc_principal == 1:
            esc_alunos = ""
            while esc_alunos != 0:    
                menu("ALUNOS")
                mostrar_tabela_opcoes_alunos()

                try:
                    esc_alunos = int(input("\nInforme sua escolha: "))
                except ValueError:
                    print("\nERRO! Por favor, informe um número válido.")
                    continue

                if esc_alunos < 0 or esc_alunos > 5:
                    print("\nERRO! Informe uma escolha válida")
                else:

                    # Opção 1
                    if esc_alunos == 1:
                        menu("CADASTRAR ALUNOS")
                        cadastrar_aluno(alunos)
                        salvar_dados(alunos, trimestres, recuperacao, mensalidades)

                    # Opção 2    
                    if esc_alunos == 2:
                        menu("MOSTRAR ALUNOS")
                        mostrar_alunos(alunos)

                    # Opção 3
                    if esc_alunos == 3:
                        menu("BUSCAR ALUNO")
                        buscar_aluno(alunos)

                    # Opção 4
                    if esc_alunos == 4:
                        menu("EDITAR ALUNO")
                        editar_aluno(alunos)
                        salvar_dados(alunos, trimestres, recuperacao, mensalidades)

                    # Opção 5
                    if esc_alunos == 5:
                        menu("REMOVER ALUNO")
                        remover_aluno(alunos)
                        salvar_dados(alunos, trimestres, recuperacao, mensalidades)

                    if esc_alunos == 0:
                        break

        if esc_principal == 2:
            esc_notas = ""
            while esc_notas != 0:
                menu("NOTAS")
                mostrar_tabela_opcoes_notas()

                try:
                    esc_notas = int(input("Informe sua escolha: "))
                except ValueError:
                    print("ERRO! Por favor, informe um número válido.")
                    continue

                if esc_notas < 0 or esc_notas > 3:
                    print("ERRO! Informe uma escolha válida")
                else:
                    if esc_notas == 1:
                        menu("CADASTRAR NOTAS")
                        cadastrar_notas(alunos, trimestres, recuperacao)
                        salvar_dados(alunos, trimestres, recuperacao, mensalidades)

                    if esc_notas == 2:
                        menu("MOSTRAR NOTAS")
                        mostrar_notas(alunos,trimestres, recuperacao)

                    if esc_notas == 3:
                        menu("EDITAR NOTAS")
                        editar_notas(alunos, trimestres, recuperacao)
                        salvar_dados(alunos, trimestres, recuperacao, mensalidades)

                    if esc_notas == 0:
                        break

        if esc_principal == 3:
            esc_mensalidades = ""
            while esc_mensalidades != 0:
                menu("MENSALIDADES")
                mostrar_tabela_opcoes_mensalidades()

                try:
                    esc_mensalidades = int(input("Informe uma escolha: "))
                except ValueError:
                    print("ERRO! Por favor, informe um número válido.")
                    continue

                if esc_mensalidades < 0 or esc_mensalidades > 4:
                    print("ERRO! Informe uma escolha válida")

                else:
                    if esc_mensalidades == 1:
                        menu("CADASTRAR MENSALIDADES")
                        cadastrar_mensalidades(alunos, mensalidades)
                        salvar_dados(alunos, trimestres, recuperacao, mensalidades)

                    if esc_mensalidades == 2:
                        menu("REGISTRAR PAGAMENTO")
                        registrar_pagamento_mensalidade(alunos, mensalidades)

                    if esc_mensalidades == 3:
                        menu("CONSULTAR MENSALIDADES")
                        consultar_mensalidades(alunos, mensalidades)

                    if esc_mensalidades == 4:
                        menu("RELATÓRIO DE PENDENTES")
                        mostrar_relatorio_pendentes(mensalidades)

                    if esc_mensalidades == 0:
                        break

        if esc_principal == 0:
            salvar_dados(alunos, trimestres, recuperacao, mensalidades)
            print("Saindo do sistema... Até logo!")
            break