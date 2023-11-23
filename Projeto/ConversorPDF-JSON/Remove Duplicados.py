import json
import hashlib

def remover_duplicatas(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r', encoding='utf-8') as file:
        dados = json.load(file)

    # Função para calcular o hash de uma entrada
    def calcular_hash(entrada):
        return hashlib.sha256(json.dumps(entrada, sort_keys=True).encode('utf-8')).hexdigest()

    # Remover duplicatas com base nos hashes
    entradas_unicas = {}
    for entrada in dados:
        hash_entrada = calcular_hash(entrada)
        entradas_unicas[hash_entrada] = entrada

    dados_sem_duplicatas = list(entradas_unicas.values())

    with open(arquivo_saida, 'w', encoding='utf-8') as file:
        json.dump(dados_sem_duplicatas, file, indent=4, ensure_ascii=False)


# Exemplo de uso
remover_duplicatas('C:/Users/Carlin/2023-2-Squad10/Projeto/dados.json', 'saida.json')