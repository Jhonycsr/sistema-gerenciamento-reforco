import customtkinter as ctk
from funcoes.dados_e_menu_geral.funcoes_dados import *

class AppReforco(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Reforço Escolar")
        self.geometry("800x600")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.alunos, self.trimestres, self.recuperacao, self.mensalidades = carregar_dados()

        self.criar_menu_lateral()
        self.criar_area_conteudo()
        self.limpar_area_conteudo()
        self.mostrar_tela_inicial()
        

    def criar_menu_lateral(self):

        self.frame_menu = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.frame_menu.grid(row=0, column=0, sticky="nsew")

        label_titulo = ctk.CTkLabel(
            self.frame_menu,
            text="REFORÇO ESCOLAR",
            font=("Arial", 16, "bold")
        )
        label_titulo.pack(pady=20, padx=20)

        btn_inicio = ctk.CTkButton(
            self.frame_menu,
            text="🏠  Início",
            fg_color="#1f6aa5",
            hover_color="#144870",
            anchor="w",
            command=self.mostrar_tela_inicial
        )
        btn_inicio.pack(pady=8, padx=15, fill="x")

        btn_alunos = ctk.CTkButton(
            self.frame_menu,
            text="👨‍🎓  Alunos",
            anchor="w",
            command=self.mostrar_tela_alunos
        )
        btn_alunos.pack(pady=8, padx=15, fill="x")

        btn_notas = ctk.CTkButton(
            self.frame_menu,
            text="📚  Notas",
            anchor="w",
            command=self.mostrar_tela_notas
        )
        btn_notas.pack(pady=8, padx=15, fill="x")

        btn_mensalidades = ctk.CTkButton(
            self.frame_menu,
            text="💳  Mensalidades",
            anchor="w",
            command=self.mostrar_tela_mensalidades
        )
        btn_mensalidades.pack(pady=8, padx=15, fill="x")


    def criar_area_conteudo(self):
        self.frame_conteudo = ctk.CTkFrame(self)
        self.frame_conteudo.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    def mostrar_tela_inicial(self):

        self.limpar_area_conteudo()

        lbl_boas_vindas = ctk.CTkLabel(
            self.frame_conteudo,
            text="SISTEMA DE GESTÃO DE REFORÇO ESCOLAR",
            font=("Arial", 22, "bold")
        )
        lbl_boas_vindas.pack(pady=(20, 5))

        lbl_subtitulo = ctk.CTkLabel(
            self.frame_conteudo,
            text="Bem-vindo(a)! Escolha um módulo no menu lateral para começar.",
            font=("Arial", 14),
            text_color="gray"
        )
        lbl_subtitulo.pack(pady=(0, 20))

        frame_cards = ctk.CTkFrame(self.frame_conteudo, fg_color="transparent")
        frame_cards.pack(pady=20, fill="x", padx=20)
        frame_cards.grid_columnconfigure((0, 1), weight=1)

        card_alunos = ctk.CTkFrame(frame_cards, corner_radius=10)
        card_alunos.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        total_alunos = len(self.alunos)
        lbl_card1_num = ctk.CTkLabel(card_alunos, text=str(total_alunos), font=("Arial", 28, "bold"), text_color="#1f6aa5")
        lbl_card1_num.pack(pady=(15, 0))
        lbl_card1_txt = ctk.CTkLabel(card_alunos, text="Alunos Cadastrados", font=("Arial", 13, "bold"))
        lbl_card1_txt.pack(pady=(0, 15))

        card_pendentes = ctk.CTkFrame(frame_cards, corner_radius=10)
        card_pendentes.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        pendencias = 0
        for cobrancas in self.mensalidades.values():
            for info in cobrancas.values():
                if info["status"] in ["Pendente", "Parcial"]:
                    pendencias += 1

        cor_status = "red" if pendencias > 0 else "green"
        lbl_card2_num = ctk.CTkLabel(card_pendentes, text=str(pendencias), font=("Arial", 28, "bold"), text_color=cor_status)
        lbl_card2_num.pack(pady=(15, 0))
        lbl_card2_txt = ctk.CTkLabel(card_pendentes, text="Mensalidades Pendentes", font=("Arial", 13, "bold"))
        lbl_card2_txt.pack(pady=(0, 15))

        frame_banner = ctk.CTkFrame(self.frame_conteudo, corner_radius=10)
        frame_banner.pack(pady=30, padx=20, fill="x")

        lbl_frase = ctk.CTkLabel(
            frame_banner,
            text="\"A educação transforma vidas e constrói o futuro.\"\n\nUtilize o menu à esquerda para navegar entre Alunos, Notas e Mensalidades.",
            font=("Arial", 13, "italic"),
            justify="center"
        )
        lbl_frase.pack(pady=25, padx=15)

    def limpar_area_conteudo(self):
        for widget in self.frame_conteudo.winfo_children():
            widget.destroy()

        self.update_idletasks()


    def mostrar_tela_alunos(self):
        self.limpar_area_conteudo()
        label_titulo = ctk.CTkLabel(
            self.frame_conteudo,
            text="GESTÃO DE ALUNOS",
            font=("Arial", 20, "bold")
        )
        label_titulo.pack(pady=20)

        self.tabview_alunos = ctk.CTkTabview(self.frame_conteudo)
        self.tabview_alunos.pack(pady=10, padx=20, fill="both", expand=True)

        tab_cadastrar = self.tabview_alunos.add("Cadastrar Aluno")
        tab_consultar = self.tabview_alunos.add("Consultar / Lista")


        self.frame_form = ctk.CTkFrame(tab_cadastrar)
        self.frame_form.pack(pady=10, padx=20, fill="x")

        label_nome = ctk.CTkLabel(self.frame_form, text="Nome:", font=("Arial", 14))
        label_nome.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_nome = ctk.CTkEntry(self.frame_form, placeholder_text="Ex: João Silva", width=300)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        label_responsavel = ctk.CTkLabel(self.frame_form, text="Responsável:", font=("Arial", 14))
        label_responsavel.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_responsavel = ctk.CTkEntry(self.frame_form, placeholder_text="EX: Maria Silva", width=300)
        self.entry_responsavel.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        label_telefone = ctk.CTkLabel(self.frame_form, text="Telefone:", font=("Arial", 14))
        label_telefone.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_telefone = ctk.CTkEntry(self.frame_form, placeholder_text="Ex: 999999999", width=300)
        self.entry_telefone.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        label_serie = ctk.CTkLabel(self.frame_form, text="Série:", font=("Arial", 14))
        label_serie.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.entry_serie = ctk.CTkEntry(self.frame_form, placeholder_text="Ex: 1° Ano do Fundamental", width=300)
        self.entry_serie.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        label_escola = ctk.CTkLabel(self.frame_form, text="Escola:", font=("Arial", 14))
        label_escola.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.entry_escola = ctk.CTkEntry(self.frame_form, placeholder_text="Ex: Escola João Maria", width=300)
        self.entry_escola.grid(row=4, column=1, padx=10, pady=10, sticky="w")


        btn_salvar = ctk.CTkButton(
            tab_cadastrar,
            text="Salvar Aluno",
            command=self.salvar_aluno_gui
        )
        btn_salvar.pack(pady=15)

        self.label_status = ctk.CTkLabel(tab_cadastrar, text="", font=("Arial", 13, "bold"))
        self.label_status.pack(pady=5)

        frame_busca = ctk.CTkFrame(tab_consultar)
        frame_busca.pack(pady=10, padx=10, fill="x")

        self.entry_busca = ctk.CTkEntry(
            frame_busca,
            placeholder_text="Digite o nome do aluno para buscar...",
            width=350
        )
        self.entry_busca.pack(side="left", padx=10, pady=10)

        btn_buscar = ctk.CTkButton(
            frame_busca,
            text="Buscar",
            width=100,
            command=self.filtrar_alunos_gui
        )
        btn_buscar.pack(side="left", padx=5)

        self.scroll_alunos = ctk.CTkScrollableFrame(tab_consultar, height=300)
        self.scroll_alunos.pack(pady=10, padx=10, fill="both", expand="True")

        self.atualizar_lista_alunos_gui()

    def salvar_aluno_gui(self):
        nome = self.entry_nome.get().title().strip()
        responsavel = self.entry_responsavel.get().title().strip()
        telefone = self.entry_telefone.get().strip()
        serie = self.entry_serie.get().strip()
        escola = self.entry_escola.get().strip()

        if not nome or not responsavel or not telefone or not serie or not escola:
            self.label_status.configure(text="ERRO! Preencha todos os campos corretamente.", text_color = "red")
            return

        if len(telefone) != 9 or not telefone.isdigit():
            self.label_status.configure(text="ERRO! O telefone precisar ter 9 dígitos númericos.", text_color = "red")
            return

        if nome in self.alunos:
            self.label_status.configure(f"ERRO! O aluno '{nome}' já está cadastrado.", text_color = "red")
            return

        self.alunos[nome] = {
            "Responsável": responsavel,
            "Telefone": telefone,
            "Série": serie,
            "Escola": escola
        }

        salvar_dados(self.alunos, self.trimestres, self.recuperacao, self.mensalidades)

        self.atualizar_lista_alunos_gui()
        self.label_status.configure(text=f"Aluno '{nome}' cadastrado com sucesso!", text_color = "green")

        self.entry_nome.delete(0, "end")
        self.entry_responsavel.delete(0, "end")
        self.entry_telefone.delete(0, "end")
        self.entry_serie.delete(0, "end")
        self.entry_escola.delete(0, "end")


    def atualizar_lista_alunos_gui(self, termo_busca=""):
        for widget in self.scroll_alunos.winfo_children():
            widget.destroy()

        if not self.alunos:
            lbl_vazio = ctk.CTkLabel(
                self.scroll_alunos,
                text="Nenhum aluno cadastrado no sistema.",
                font=("Arial", 14)
            )
            lbl_vazio.pack(pady=20)
            return

        encontrou = False

        for nome, info in self.alunos.items():
            if termo_busca.lower() in nome.lower():
                encontrou = True

                card = ctk.CTkFrame(self.scroll_alunos)
                card.pack(pady=5, padx=5, fill="x")
    
                texto_aluno = (
                    f"Nome: {nome}\n"
                    f"Responsável: {info['Responsável']} | Telefone: {info['Telefone']}\n"
                    f"Série: {info['Série']} | Escola: {info['Escola']}"
                )
                
                lbl_info = ctk.CTkLabel(
                    card,
                    text=texto_aluno,
                    justify="left",
                    font=("Arial", 12)
                )
                lbl_info.pack(side="left", padx=15, pady=20)

                frame_botoes = ctk.CTkFrame(card, fg_color="transparent")
                frame_botoes.pack(side="right", padx=10, pady=10)

                btn_editar = ctk.CTkButton(
                    frame_botoes,
                    text="Editar",
                    width=75,
                    fg_color="orange",
                    hover="#d97706",
                    command=lambda n=nome: self.abrir_janela_editar_aluno(n)
                )
                btn_editar.pack(side="top", pady=2)

                btn_excluir = ctk.CTkButton(
                    frame_botoes,
                    text="Excluir",
                    width=75,
                    fg_color="red",
                    hover_color="#b91c1c",
                    command=lambda n=nome: self.excluir_aluno_gui(n)
                )
                btn_excluir.pack(side="top", pady=2)
    
            if not encontrou:
                lbl_erro = ctk.CTkLabel(
                    self.scroll_alunos,
                    text=f"Nenhum aluno encontrado com '{termo_busca}'.",
                    font=("Arial", 13)
                )
                lbl_erro.pack(pady=20)


    def filtrar_alunos_gui(self):
        termo = self.entry_busca.get().strip()
        self.atualizar_lista_alunos_gui(termo_busca=termo)


    def abrir_janela_editar_aluno(self, nome_antigo):
        janela_edit = ctk.CTkToplevel(self)
        janela_edit.title(f"Editar Aluno: {nome_antigo}")
        janela_edit.geometry("450x400")
        janela_edit.grab_set()

        lbl_titulo = ctk.CTkLabel(janela_edit, text=f"Editando {nome_antigo}", font=("Arial", 16, "bold"))
        lbl_titulo.pack(pady=15)

        frame_fields = ctk.CTkFrame(janela_edit)
        frame_fields.pack(pady=10, padx=20, fill="both", expand=True)

        info = self.alunos[nome_antigo]

        ctk.CTkLabel(frame_fields, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        entry_nome = ctk.CTkEntry(frame_fields, width=250)
        entry_nome.insert(0, nome_antigo)
        entry_nome.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame_fields, text="Responsável:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_responsavel = ctk.CTkEntry(frame_fields, width=250)
        entry_responsavel.insert(0, info['Responsável'])
        entry_responsavel.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame_fields, text="Telefone:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        entry_telefone = ctk.CTkEntry(frame_fields, width=250)
        entry_telefone.insert(0, info['Telefone'])
        entry_telefone.grid(row=2, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame_fields, text="Série:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        entry_serie = ctk.CTkEntry(frame_fields, width=250)
        entry_serie.insert(0, info['Série'])
        entry_serie.grid(row=3, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame_fields, text="Escola:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        entry_escola = ctk.CTkEntry(frame_fields, width=250)
        entry_escola.insert(0, info['Escola'])
        entry_escola.grid(row=4, column=1, padx=10, pady=5)

        lbl_status_edit = ctk.CTkLabel(janela_edit, text="", font=("Arial", 12, "bold"))
        lbl_status_edit.pack(pady=5)


        def salvar_alteracoes():
            novo_nome = entry_nome.get().title().strip()
            resp = entry_responsavel.get().title().strip()
            tel = entry_telefone.get().strip()
            serie = entry_serie.get().strip()
            escola = entry_escola.get().strip()

            if not novo_nome or not resp or not tel or not serie or not escola:
                lbl_status_edit.configure(text="Preencha todos os campos!", text_color="red")
                return

            if novo_nome != nome_antigo and novo_nome in self.alunos:
                lbl_status_edit.configure(text="Já existe um aluno com esse novo nome!", text_color="red")
                return

            if novo_nome != nome_antigo:
                del self.alunos[nome_antigo]

            self.alunos[novo_nome] = {
                "Responsável": resp,
                "Telefone": tel,
                "Série": serie,
                "Escola": escola
            }

            salvar_dados(self.alunos, self.trimestres, self.recuperacao, self.mensalidades)

            self.atualizar_lista_alunos_gui()
            janela_edit.destroy()

        btn_confirmar = ctk.CTkButton(janela_edit, text="Salvar Alterações", command=salvar_alteracoes)
        btn_confirmar.pack(pady=10)


    def excluir_aluno_gui(self, nome_aluno):
        if nome_aluno in self.alunos:
            del self.alunos[nome_aluno]

            for num_tri in self.trimestres:
                if nome_aluno in self.trimestres[num_tri]:
                    del self.trimestres[num_tri][nome_aluno]

            if nome_aluno in self.recuperacao:
                del self.recuperacao[nome_aluno]

            if nome_aluno in self.mensalidades:
                del self.mensalidades[nome_aluno]

            salvar_dados(self.alunos, self.trimestres, self.recuperacao, self.mensalidades)

            self.atualizar_lista_alunos_gui()


    def mostrar_tela_notas(self):
        self.limpar_area_conteudo()

        label_titulo = ctk.CTkLabel(
            self.frame_conteudo,
            text="GESTÃO DE NOTAS E BOLETIM",
            font=("Arial", 20, "bold")
        )
        label_titulo.pack(pady=(10, 5))

        self.tabview_notas = ctk.CTkTabview(self.frame_conteudo)
        self.tabview_notas.pack(pady=10, padx=20, fill="both", expand=True)

        tab_lancar = self.tabview_notas.add("Lançar Notas")
        tab_boletim = self.tabview_notas.add("Boletim / Ver notas")


        self.frame_form_notas = ctk.CTkFrame(tab_lancar)
        self.frame_form_notas.pack(pady=10, padx=20, fill="x")
        self.frame_form_notas.grid_columnconfigure(1, weight=1)

        lista_alunos = list(self.alunos.keys()) if self.alunos else ["Nenhum aluno cadastado"]

        label_aluno = ctk.CTkLabel(self.frame_form_notas, text="Aluno:", font=("Arial", 14))
        label_aluno.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.option_aluno_nota = ctk.CTkOptionMenu(
            self.frame_form_notas,
            values=lista_alunos,
            width=280
        )
        self.option_aluno_nota.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        label_periodo = ctk.CTkLabel(self.frame_form_notas, text="Período:", font=("Arial", 14))
        label_periodo.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.option_periodo = ctk.CTkOptionMenu(
            self.frame_form_notas,
            values=["Trimestre 1", "Trimestre 2", "Trimestre 3", "Recuperação"],
            width=280
        )
        self.option_periodo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        label_materia = ctk.CTkLabel(self.frame_form_notas, text="Matéria:", font=("Arial", 14))
        label_materia.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_materia = ctk.CTkEntry(
            self.frame_form_notas,
            placeholder_text="Ex: Matemática, Português...",
            width=280
        )
        self.entry_materia.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        label_valor_nota = ctk.CTkLabel(self.frame_form_notas, text="Nota (0 a 10):", font=("Arial", 14))
        label_valor_nota.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.entry_valor_nota = ctk.CTkEntry(
            self.frame_form_notas,
            placeholder_text="Ex: 8.5",
            width=280
        )
        self.entry_valor_nota.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        btn_salvar_nota = ctk.CTkButton(
            tab_lancar,
            text="Cadastrar / Adicionar Nota",
            command=self.salvar_nota_gui
        )
        btn_salvar_nota.pack(pady=15)

        self.label_status_nota = ctk.CTkLabel(tab_lancar, text="", font=("Arial", 13, "bold"))
        self.label_status_nota.pack(pady=5)


        frame_seletor_boletim = ctk.CTkFrame(tab_boletim)
        frame_seletor_boletim.pack(pady=10, padx=10, fill="x")

        lbl_boletim_aluno = ctk.CTkLabel(frame_seletor_boletim, text="Selecione o Aluno:", font=("Arial", 14))
        lbl_boletim_aluno.pack(side="left", padx=10, pady=10)

        self.option_boletim_aluno = ctk.CTkOptionMenu(
            frame_seletor_boletim,
            values=lista_alunos,
            width=250
        )
        self.option_boletim_aluno.pack(side="left", padx=10, pady=10)

        btn_ver_boletim = ctk.CTkButton(
            frame_seletor_boletim,
            text="Ver Boletim",
            command=self.gerar_boletim_gui
        )
        btn_ver_boletim.pack(side="left", padx=10)

        self.scroll_boletim = ctk.CTkScrollableFrame(tab_boletim, height=300)
        self.scroll_boletim.pack(pady=10, padx=10, fill="both", expand=True)


    def salvar_nota_gui(self):
        aluno = self.option_aluno_nota.get()
        periodo = self.option_periodo.get()
        materia = self.entry_materia.get().title().strip()
        valor_str = self.entry_valor_nota.get().strip()

        if aluno == "Nenhum aluno cadastrado":
            self.label_status_nota(text="ERRO! Cadastre um aluno primeiro.", text_color = "red")
            return

        if not materia or not valor_str:
            self.label_status_nota.configure(text="ERRO! Prrencha a matéria e o valor da nota.", text_color = "red")
            return

        try:
            valor_nota = float(valor_str)
            if not (0<= valor_nota <= 10):
                self.label_status_nota.configure(text="ERRO! A nota deve estar entre 0 e 10.", text_color = "red")
                return
        except ValueError:
            self.label_status_nota.configure(text="ERRO! Digite um valor numérico válido.", text_color = "red")
            return

        if "Trimestre" in periodo:
            num_trim = int(periodo.split()[1])
            dados_trim = self.trimestres[num_trim]

            if aluno not in dados_trim:
                dados_trim[aluno] = {}

            if materia not in dados_trim[aluno]:
                dados_trim[aluno][materia] = {}

            qtd_existente = len(dados_trim[aluno][materia])
            nome_nota = f"Nota {qtd_existente + 1}"
            dados_trim[aluno][materia][nome_nota] = valor_nota

        elif periodo == "Recuperação":
            if aluno not in self.recuperacao:
                self.recuperacao[aluno] = {}

            self.recuperacao[aluno][materia] = valor_nota

        salvar_dados(self.alunos, self.trimestres, self.recuperacao, self.mensalidades)

        self.label_status_nota.configure(
            text=f"Nota {valor_nota} adicionada em {materia} para {aluno}!",
            text_color = "green"
        )

        self.entry_materia.delete(0, "end")
        self.entry_valor_nota.delete(0, "end")


    def gerar_boletim_gui(self):
        for widget in self.scroll_boletim.winfo_children():
            widget.destroy()

        aluno = self.option_boletim_aluno.get()
        if aluno == "Nenhum aluno cadastrado":
            return

        tem_notas = False

        for num_trim, dados_trim in self.trimestres.items():
            if aluno in dados_trim and dados_trim[aluno]:
                tem_notas = True

                card_trim = ctk.CTkFrame(self.scroll_boletim)
                card_trim.pack(pady=5, padx=5, fill="x")

                lbl_trim_titulo = ctk.CTkLabel(
                    card_trim,
                    text=f"--- Trimestre {num_trim} ---",
                    font=("Arial", 14, "bold")
                )
                lbl_trim_titulo.pack(anchor="w", padx=10, pady=5)

                for materia, notas in dados_trim[aluno].items():
                    if notas:
                        media = sum(notas.values()) / len(notas)
                        str_notas = ", ".join([f"{k}: {v}" for k, v in notas.items()])
                        texto_materia = f"  • {materia}: {str_notas}  |  Média: {media:.1f}"
                    else:
                        texto_materia = f"  • {materia}: Sem notas registradas"

                    lbl_mat = ctk.CTkLabel(card_trim, text=texto_materia, font=("Arial", 12))
                    lbl_mat.pack(anchor="w", padx=20, pady=(5, 2))

                    for nome_nota, valor in list(notas.items()):
                        frame_linha_nota = ctk.CTkFrame(card_trim, fg_color="transparent")
                        frame_linha_nota.pack(fill="x", padx=25, pady=2)

                        lbl_nota_str = ctk.CTkLabel(
                            frame_linha_nota,
                            text=f"   - {nome_nota}: {valor}",
                            font=("Arial", 12)
                        )
                        lbl_nota_str.pack(side="left")

                        btn_del_nota = ctk.CTkButton(
                            frame_linha_nota,
                            text="X",
                            width=25,
                            height=20,
                            fg_color="red",
                            hover_color="#b91c1c",
                            command=lambda t=num_trim, m=materia, n=nome_nota: self.abrir_janela_editar_nome(aluno, t, m, n)
                        )
                        btn_del_nota.pack(side="right", padx=2)

                        btn_edit_nota = ctk.CTkButton(
                            frame_linha_nota,
                            text="Editar",
                            width=50,
                            height=20,
                            fg_color="orange",
                            hover_color="#d97706",
                            command=lambda t=num_trim, m=materia, n=nome_nota, v=valor: self.abrir_janela_editar_nota(aluno, t, m, n, v)
                        )
                        btn_edit_nota.pack(side="right", padx=2)


        if aluno in self.recuperacao and self.recuperacao[aluno]:
            tem_notas = True
            card_rec = ctk.CTkFrame(self.scroll_boletim)
            card_rec.pack(pady=5, padx=5, fill="x")

            lbl_rec_titulo = ctk.CTkLabel(
                card_rec, 
                text="--- Recuperação ---", 
                font=("Arial", 14, "bold"),
                text_color="orange"
            )
            lbl_rec_titulo.pack(anchor="w", padx=10, pady=5)

            for materia, nota in self.recuperacao[aluno].items():
                lbl_mat_rec = ctk.CTkLabel(
                    card_rec, 
                    text=f"  • {materia}: Nota {nota}", 
                    font=("Arial", 12)
                )
                lbl_mat_rec.pack(side="left")

                btn_del_rec = ctk.CTkButton(
                    card_rec,
                    text="X",
                    width=25,
                    height=20,
                    fg_color="red",
                    hover_color="#b91c1c",
                    command=lambda m=materia: self.excluir_nota_recuperacao_gui(aluno, m)
                )
                btn_del_rec.pack(side="right", padx=2)

                
                btn_edit_rec = ctk.CTkButton(
                    card_rec,
                    text="Editar",
                    width=50,
                    height=20,
                    fg_color="orange",
                    hover_color="#d97706",
                    command=lambda m=materia, v=nota: self.abrir_janela_editar_nota(aluno, "Recuperação", m, "", v)
                )
                btn_edit_rec.pack(side="right", padx=2)

        if not tem_notas:
            lbl_vazio = ctk.CTkLabel(
                self.scroll_boletim, 
                text=f"Nenhuma nota registrada para {aluno}.", 
                font=("Arial", 13)
            )
            lbl_vazio.pack(pady=20)


    def abrir_janela_editar_nota(self, aluno, trimestre, materia, nome_nota, valor_atual):
        janela_edit = ctk.CTkToplevel(self)
        janela_edit.title("Editar Nota")
        janela_edit.geometry("350x220")
        janela_edit.grab_set()

        titulo = f"Editar {nome_nota} ({materia})" if nome_nota else f"Editar Recuperação ({materia})"
        lbl_titulo = ctk.CTkLabel(janela_edit, text=titulo, font=("Arial", 14, "bold"))
        lbl_titulo.pack(pady=15)

        frame_field = ctk.CTkFrame(janela_edit)
        frame_field.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(frame_field, text="Nova Nota (0-10):").pack(side="left", padx=10, pady=10)
        entry_nova_nota = ctk.CTkEntry(frame_field, width=100)
        entry_nova_nota.insert(0, str(valor_atual))
        entry_nova_nota.pack(side="left", padx=10, pady=10)

        lbl_status_edit = ctk.CTkLabel(janela_edit, text="", font=("Arial", 12, "bold"))
        lbl_status_edit.pack(pady=5)

        def salvar_edicao_nota():
            str_nota = entry_nova_nota.get().strip()
            try:
                novo_valor = float(str_nota)
                if not (0 <= novo_valor <= 10):
                    lbl_status_edit.configure(text="Nota deve ser de 0 a 10!", text_color="red")
                    return
            except ValueError:
                lbl_status_edit.configure(text="Digite um número válido!", text_color="red")
                return

            if trimestre == "Recuperação":
                self.recuperacao[aluno][materia] = novo_valor
            else:
                self.trimestres[trimestre][aluno][materia][nome_nota] = novo_valor

            salvar_dados(self.alunos, self.trimestres, self.recuperacao, self.mensalidades)

            self.gerar_boletim_gui()
            janela_edit.destroy()

        btn_salvar = ctk.CTkButton(janela_edit, text="Salvar Alteração", command=salvar_edicao_nota)
        btn_salvar.pack(pady=10)

    def excluir_nota_gui(self, aluno, trimestre, materia, nome_nota):
        if aluno in self.trimestres[trimestre] and materia in self.trimestres[trimestre][aluno]:
            if nome_nota in self.trimestres[trimestre][aluno][materia]:
                del self.trimestres[trimestre][aluno][materia][nome_nota]
                
                if not self.trimestres[trimestre][aluno][materia]:
                    del self.trimestres[trimestre][aluno][materia]

                salvar_dados(self.alunos, self.trimestres, self.recuperacao, self.mensalidades)
                self.gerar_boletim_gui()

    def excluir_nota_recuperacao_gui(self, aluno, materia):
        if aluno in self.recuperacao and materia in self.recuperacao[aluno]:
            del self.recuperacao[aluno][materia]
            salvar_dados(self.alunos, self.trimestres, self.recuperacao, self.mensalidades)
            self.gerar_boletim_gui()


    def mostrar_tela_mensalidades(self):
        self.limpar_area_conteudo()

        label_titulo = ctk.CTkLabel(
            self.frame_conteudo,
            text="GESTÃO DE MENSALIDADES",
            font=("Arial", 20, "bold")
        )
        label_titulo.pack(pady=(10, 5))

        self.tabview_mensalidades = ctk.CTkTabview(self.frame_conteudo)
        self.tabview_mensalidades.pack(pady=10, padx=20, fill="both", expand=True)

        tab_gerar = self.tabview_mensalidades.add("Gerar Cobrança")
        tab_pagar = self.tabview_mensalidades.add("Registrar Pagamento")
        tab_relatorio = self.tabview_mensalidades.add("Relatório / Pendentes")

        lista_alunos = list(self.alunos.keys()) if self.alunos else ["Nenhum aluno cadastrado"]

        frame_gerar = ctk.CTkFrame(tab_gerar)
        frame_gerar.pack(pady=10, padx=20, fill="x")
        frame_gerar.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(frame_gerar, text="Aluno:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.option_aluno_gerar_mens = ctk.CTkOptionMenu(frame_gerar, values=lista_alunos, width=280)
        self.option_aluno_gerar_mens.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(frame_gerar, text="Mês/Ano:", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_mes_mens = ctk.CTkEntry(frame_gerar, placeholder_text="Ex: Março/2026", width=280)
        self.entry_mes_mens.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(frame_gerar, text="Valor (R$):", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_valor_mens = ctk.CTkEntry(frame_gerar, placeholder_text="Ex: 150.00", width=280)
        self.entry_valor_mens.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        btn_gerar = ctk.CTkButton(tab_gerar, text="Gerar Mensalidade", command=self.gerar_mensalidade_gui)
        btn_gerar.pack(pady=15)

        self.label_status_gerar_mens = ctk.CTkLabel(tab_gerar, text="", font=("Arial", 13, "bold"))
        self.label_status_gerar_mens.pack(pady=5)


        frame_pagar = ctk.CTkFrame(tab_pagar)
        frame_pagar.pack(pady=10, padx=20, fill="x")
        frame_pagar.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(frame_pagar, text="Aluno:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.option_aluno_pagar_mens = ctk.CTkOptionMenu(frame_pagar, values=lista_alunos, width=280)
        self.option_aluno_pagar_mens.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(frame_pagar, text="Mês/Ano:", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_mes_pagar = ctk.CTkEntry(frame_pagar, placeholder_text="Ex: Março/2026", width=280)
        self.entry_mes_pagar.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(frame_pagar, text="Valor Pago (R$):", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_valor_pago = ctk.CTkEntry(frame_pagar, placeholder_text="Ex: 150.00", width=280)
        self.entry_valor_pago.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        btn_pagar = ctk.CTkButton(tab_pagar, text="Confirmar Pagamento", command=self.registrar_pagamento_gui)
        btn_pagar.pack(pady=15)

        self.label_status_pagar_mens = ctk.CTkLabel(tab_pagar, text="", font=("Arial", 13, "bold"))
        self.label_status_pagar_mens.pack(pady=5)


        btn_atualizar_relatorio = ctk.CTkButton(tab_relatorio, text="Atualizar Relatório", command=self.atualizar_relatorio_mensalidades_gui)
        btn_atualizar_relatorio.pack(pady=10)

        self.scroll_relatorio_mens = ctk.CTkScrollableFrame(tab_relatorio, height=300)
        self.scroll_relatorio_mens.pack(pady=10, padx=10, fill="both", expand=True)

        self.atualizar_relatorio_mensalidades_gui()


    def gerar_mensalidade_gui(self):
        aluno = self.option_aluno_gerar_mens.get()
        mes = self.entry_mes_mens.get().strip().capitalize()
        valor_str = self.entry_valor_mens.get().strip()

        if aluno == "Nenhum aluno cadastrado":
            self.label_status_gerar_mens.configure(text="ERRO! Cadastre um aluno primeiro.", text_color="red")
            return

        if not mes or not valor_str:
            self.label_status_gerar_mens.configure(text="ERRO! Preencha o Mês/Ano e o Valor.", text_color="red")
            return

        try:
            valor = float(valor_str)
            if valor <= 0:
                self.label_status_gerar_mens.configure(text="ERRO! O valor deve ser maior que zero.", text_color="red")
                return
        except ValueError:
            self.label_status_gerar_mens.configure(text="ERRO! Digite um valor numérico válido (ex: 150.00).", text_color="red")
            return

        if aluno not in self.mensalidades:
            self.mensalidades[aluno] = {}

        if mes in self.mensalidades[aluno]:
            self.label_status_gerar_mens.configure(text=f"AVISO: Mensalidade de {mes} já existia para {aluno} e foi atualizada!", text_color="orange")

        self.mensalidades[aluno][mes] = {
            "valor_total": valor,
            "valor_pago": 0.0,
            "status": "Pendente"
        }

        salvar_dados(self.alunos, self.trimestres, self.recuperacao, self.mensalidades)

        self.label_status_gerar_mens.configure(text=f"Mensalidade de {mes} (R$ {valor:.2f}) gerada com sucesso!", text_color="green")
        self.entry_mes_mens.delete(0, "end")
        self.entry_valor_mens.delete(0, "end")
        self.atualizar_relatorio_mensalidades_gui()


    def registrar_pagamento_gui(self):
        aluno = self.option_aluno_pagar_mens.get()
        mes = self.entry_mes_pagar.get().strip().capitalize()
        pago_str = self.entry_valor_pago.get().strip()

        if aluno == "Nenhum aluno cadastrado":
            self.label_status_pagar_mens.configure(text="ERRO! Cadastre um aluno primeiro.", text_color="red")
            return

        if aluno not in self.mensalidades or mes not in self.mensalidades[aluno]:
            self.label_status_pagar_mens.configure(text=f"ERRO! Nenhuma cobrança encontrada para {aluno} em {mes}.", text_color="red")
            return

        try:
            valor_pago_agora = float(pago_str)
            if valor_pago_agora <= 0:
                self.label_status_pagar_mens.configure(text="ERRO! Digite um valor de pagamento válido.", text_color="red")
                return
        except ValueError:
            self.label_status_pagar_mens.configure(text="ERRO! Digite um valor numérico válido.", text_color="red")
            return

        dados_cobranca = self.mensalidades[aluno][mes]
        dados_cobranca["valor_pago"] += valor_pago_agora

        total = dados_cobranca["valor_total"]
        pago_acumulado = dados_cobranca["valor_pago"]

        if pago_acumulado >= total:
            dados_cobranca["status"] = "Pago"
            troco = pago_acumulado - total
            msg = f"Pagamento concluído com sucesso!"
            if troco > 0:
                msg += f" Troco: R$ {troco:.2f}"
            self.label_status_pagar_mens.configure(text=msg, text_color="green")
        else:
            dados_cobranca["status"] = "Parcial"
            restante = total - pago_acumulado
            self.label_status_pagar_mens.configure(text=f"Pagamento parcial registrado! Resta pagar: R$ {restante:.2f}", text_color="orange")

        salvar_dados(self.alunos, self.trimestres, self.recuperacao, self.mensalidades)
        self.entry_mes_pagar.delete(0, "end")
        self.entry_valor_pago.delete(0, "end")
        self.atualizar_relatorio_mensalidades_gui()


    def atualizar_relatorio_mensalidades_gui(self):
        for widget in self.scroll_relatorio_mens.winfo_children():
            widget.destroy()

        if not self.mensalidades:
            lbl_vazio = ctk.CTkLabel(self.scroll_relatorio_mens, text="Nenhuma mensalidade cadastrada.", font=("Arial", 14))
            lbl_vazio.pack(pady=20)
            return

        for aluno, cobrancas in self.mensalidades.items():
            if cobrancas:
                card = ctk.CTkFrame(self.scroll_relatorio_mens)
                card.pack(pady=5, padx=5, fill="x")

                lbl_aluno = ctk.CTkLabel(card, text=f"Aluno: {aluno}", font=("Arial", 14, "bold"))
                lbl_aluno.pack(anchor="w", padx=10, pady=5)

                for mes, info in cobrancas.items():
                    status = info["status"]
                    cor = "green" if status == "Pago" else ("orange" if status == "Parcial" else "red")
                    
                    texto_mes = (
                        f"   • {mes}: Total R$ {info['valor_total']:.2f} | "
                        f"Pago: R$ {info['valor_pago']:.2f} | Status: {status}"
                    )

                    lbl_info = ctk.CTkLabel(card, text=texto_mes, font=("Arial", 12), text_color=cor)
                    lbl_info.pack(anchor="w", padx=20, pady=2)


if __name__ == "__main__":
    app = AppReforco()
    app.mainloop()