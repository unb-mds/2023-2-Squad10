import fitz  # PyMuPDF
import os

def converter_pdf_para_txt(arquivo_pdf, diretorio_saida):
    # Obtém o nome do arquivo PDF sem a extensão
    nome_arquivo = os.path.basename(arquivo_pdf)
    nome_arquivo_sem_extensao = os.path.splitext(nome_arquivo)[0]
    # Define o caminho do arquivo de saída TXT com base no diretório de saída e no nome do arquivo PDF
    arquivo_txt = os.path.join(diretorio_saida, f"{nome_arquivo_sem_extensao}.txt")

    # Abre o arquivo PDF usando PyMuPDF
    doc = fitz.open(arquivo_pdf)
    texto = ""

    # Itera através de todas as páginas do PDF e extrai o texto
    for pagina in doc.pages():
        texto += pagina.get_text()

    # Escreve o texto extraído em um arquivo TXT
    with open(arquivo_txt, "w", encoding="utf-8") as txt_file:
        txt_file.write(texto)

    # Retorna o caminho do arquivo TXT gerado
    return arquivo_txt

# Exemplo de uso
# Define os diretórios de entrada (PDFs) e saída (TXT)
diretorio_pdfs = "C:/Users/Carlin/2023-2-Squad10/Projeto/ConversorPDF-JSON/downloads"
diretorio_txt = "C:/Users/Carlin/2023-2-Squad10/Projeto/ConversorPDF-JSON/downloads"

# Itera sobre os arquivos no diretório de PDFs
for nome_pdf in os.listdir(diretorio_pdfs):
    # Verifica se o arquivo é um PDF
    if nome_pdf.endswith(".pdf"):
        caminho_pdf = os.path.join(diretorio_pdfs, nome_pdf)
        # Chama a função para converter o PDF para TXT
        converter_pdf_para_txt(caminho_pdf, diretorio_txt)