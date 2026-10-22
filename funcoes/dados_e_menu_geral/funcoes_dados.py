import json

def salvar_dados(alunos, trimestres, recuperacao, mensalidades):
    dados = {
        "alunos": alunos,
        "trimestres": trimestres,
        "recuperacao": recuperacao,
        "mensalidades": mensalidades
    }

    with open("dados_reforco.json", "w", encoding="utf-8") as ficheiro:
        json.dump(dados, ficheiro, indent=4, ensure_ascii=False)

    print("Dados salvos com sucesso!")


def carregar_dados():
    try:
        with open("dados_reforco.json", "r", encoding="utf-8") as ficheiro:
            dados = json.load(ficheiro)

            raw_trimestres = dados.get("trimestres", {})
            trimestres = {int(k): v for k, v in raw_trimestres.items()}

            for t in [1, 2, 3]:
                if t not in trimestres:
                    trimestres[t] = {}

            return dados.get("alunos", {}), trimestres, dados.get("recuperacao", {}), dados.get("mensalidades", {})
        
    except FileNotFoundError:
        return {}, {1: {}, 2: {}, 3: {}}, {}, {}