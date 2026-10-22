# 📚 Sistema de Gestão de Reforço Escolar

Um sistema completo para gerenciamento de alunos, notas trimestrais e controle de mensalidades para aulas de reforço escolar. O projeto conta com **duas formas de interação**: uma versão interativa via linha de comando (**CLI**) e uma interface gráfica moderna (**GUI**) desenvolvida com CustomTkinter.

---

## 🎯 Funcionalidades Principais

- **📋 Gestão de Alunos:** Cadastro, consulta, edição e remoção de alunos (com informações de responsáveis, telefone, série e escola).
- **📝 Lançamento de Notas:** Controle de notas por trimestres (1º, 2º e 3º) e registro de recuperação.
- **💰 Controle Financeiro:** Cadastro de mensalidades, registro de pagamentos e geração automática de relatórios de alunos pendentes.
- **💾 Persistência de Dados:** Todos os dados são salvos e recarregados automaticamente via arquivos no formato JSON (`dados_reforco.json`).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Interface Gráfica (GUI):** CustomTkinter
- **Persistência:** JSON (Manipulação de arquivos nativa)
- **Empacotamento:** PyInstaller / auto-py-to-exe (para geração de executável `.exe`)

---

## 📂 Estrutura do Projeto

```text
gerenciamento_reforco/
│
├── funcoes/                      # Módulos do backend e interface
│   ├── alunos/                   # Lógica de CRUD de alunos
│   ├── dados_e_menu_geral/       # Funções de carga/salvamento do JSON e menus
│   ├── interface_gui/            # Interface gráfica em CustomTkinter (app_gui.py)
│   ├── mensalidades/             # Lógica financeira e relatórios
│   └── notas/                    # Controle de notas e recuperação
│
├── __main__.py                   # Ponto de entrada da versão Terminal (CLI)
├── .gitignore                    # Filtro de arquivos de compilação
└── README.md                     # Documentação do projeto

🚀 Como Executar o Projeto
Pré-requisitos
Ter o Python 3.x instalado em sua máquina.

1. Clonar o Repositório
Bash
git clone [https://github.com/Jhonycsr/sistema-gerenciamento-reforco.git](https://github.com/Jhonycsr/sistema-gerenciamento-reforco.git)
cd sistema-gerenciamento-reforco
2. Instalar as Dependências (apenas para a versão GUI)
Bash
pip install customtkinter
3. Executar a Versão Terminal (CLI)
Bash
python __main__.py
4. Executar a Versão com Interface Gráfica (GUI)
Bash
python funcoes/interface_gui/app_gui.py
💻 Versão Executável (.exe)
O projeto foi empacotado para uso direto no Windows sem necessidade de instalação do Python.
Você pode baixar a versão executável pronta para uso na seção de Releases do repositório.

✍️ Autor
Desenvolvido por Jhonatan César Andrade Silva

GitHub - https://github.com/Jhonycsr

LinkedIn - https://www.linkedin.com/in/jhonatan-c%C3%A9sar-97213b446/
