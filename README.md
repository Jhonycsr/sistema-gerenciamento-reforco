# sistema-gerenciamento-reforco
Um sistema completo para gerenciamento de alunos, notas trimestrais e controle de mensalidades para aulas de reforço escolar. O projeto conta com **duas formas de interação**: uma versão interativa via linha de comando (**CLI**) e uma interface gráfica moderna (**GUI**) desenvolvida com CustomTkinter.
---
## 🎯 Funcionalidades Principal

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
