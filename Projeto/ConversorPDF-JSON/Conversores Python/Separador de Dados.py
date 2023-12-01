import json
from collections import defaultdict
import os

# Caminho do arquivo JSON
caminho_arquivo = "C:/Users/Carlos/2023-2-Squad10/Projeto/ConversorPDF-JSON/Dados JSON/Dados Gerais 2021 a 2023 JSON/2022 dados.json"

# Dicionário padrão para armazenar dados por município
dados_por_municipio = defaultdict(list)

# Ler dados do arquivo JSON
with open(caminho_arquivo, "r", encoding="utf-8") as file:
    dados_json = json.load(file)

# Adicionar a chave "Ano": "2021" em cada item
for dado in dados_json:
    dado["Ano"] = "2023"

# Organizar os dados por município
for dado in dados_json:
    municipio = dado["Municipio"]
    dados_por_municipio[municipio].append(dado)

# Salvar os dados em arquivos JSON separados
for municipio, dados in dados_por_municipio.items():
    filename = f"{municipio}.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=2)

print("Arquivos JSON separados por município foram criados com sucesso!")
