import json
from collections import defaultdict

# Caminho para o arquivo JSON
caminho_arquivo = "C:/Users/Carlos/2023-2-Squad10/Projeto/ConversorPDF-JSON/Dados JSON/2023 dados.json"

# Lê os dados do arquivo JSON com a codificação 'utf-8'
with open(caminho_arquivo, "r", encoding="utf-8") as file:
    dados_json = json.load(file)

# Dicionário para armazenar contagem de licitações por mês e por município
contagem_licitacoes = defaultdict(lambda: defaultdict(int))

# Processa os dados do JSON
for item in dados_json:
    nome_municipio = item["nomeMunicipio"]
    data_post = item["dataPost"]
    numero_licitacoes = item["numeroLicitacoes"]

    # Extrai o mês da data
    mes = data_post.split("-")[1]

    # Atualiza a contagem de licitações
    contagem_licitacoes[mes][nome_municipio] += numero_licitacoes

# Cria uma lista de resultados no formato desejado
resultados = []
for mes, municipios in contagem_licitacoes.items():
    for municipio, total_licitacoes in municipios.items():
        resultado = {
            "Municipio": municipio,
            "Mes": mes,
            "TotalLicitacoes": total_licitacoes
        }
        resultados.append(resultado)

# Gera um novo JSON com os resultados
with open("resultados.json", "w", encoding="utf-8") as file:
    json.dump(resultados, file, indent=2, ensure_ascii=False)

print("Resultados salvos no arquivo 'resultados.json'.")
