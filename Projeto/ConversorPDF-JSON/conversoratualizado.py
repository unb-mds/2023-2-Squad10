#AINDA ESTA EM TESTE FEITO POR xGabrielCv
import fitz  # PyMuPDF
import re
import json
import sys  # Importando o módulo sys

# Padrão de expressão regular para encontrar números
pattern_numero = re.compile(r'\d+')

# Caminho do arquivo PDF
pdf_path = 'C:/Users/jgabr/Downloads/TESTE/PDF/TESTE DEFINITIVO 2.pdf' #COLOQUE O DIRETORIO EXTATO DO ARQUIVO 

# Função para extrair texto de um arquivo PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as pdf_document:
            for page_number in range(pdf_document.page_count):
                page = pdf_document[page_number]
                text += page.get_text()
    except Exception as e:
        print(f"Erro ao extrair texto do PDF: {e}")
    return text

# Extrair texto do PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Imprimir o conteúdo do PDF para análise, ignorando caracteres problemáticos
try:
    print(pdf_text.encode(sys.stdout.encoding, errors='ignore').decode(sys.stdout.encoding))
except UnicodeEncodeError:
    print("Conteúdo do PDF contém caracteres que não podem ser impressos na console padrão.")

json_output_path = 'C:/Users/jgabr/Downloads/TESTE/JSON/output.json' #COLOQUE O DIRETORIO EXATO ONDE VOCE QUER A SAIDA COM FINAL OUTPUT.JSON

# Dividir o texto em blocos usando quebras de linha como delimitador
blocos = [bloco.strip() for bloco in pdf_text.split('\n')]

# Inicializar listas para armazenar informações
municipios = []
licitacoes = []

# Iterar pelos blocos
for bloco in blocos:
    # Tentar extrair números de cada bloco
    numeros = pattern_numero.findall(bloco)
    if numeros:
        # Se houver números, verificar se o bloco contém informações sobre municípios ou licitações
        if "Município" in bloco:
            municipios.append({"Nome do Município": bloco, "Número Total de Licitações": int(numeros[0])})
        elif "Licitação" in bloco:
            licitacoes.append(int(numeros[0]))

# Obter totais
total_licitacoes = sum(licitacoes)
total_municipios = len(municipios)

# Criar o dicionário JSON com as informações
json_data = {
    "Total de Licitações": total_licitacoes,
    "Total de Municípios": total_municipios,
    "Municípios": municipios
}

# Salvar o JSON em um arquivo
try:
    with open(json_output_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)
    print(f"JSON salvo em: {json_output_path}")
except Exception as e:
    print(f"Erro ao salvar o JSON: {e}")