import fitz  # PyMuPDF
import os

def converter_pdf_para_txt(arquivo_pdf, diretorio_saida):
    nome_arquivo = os.path.basename(arquivo_pdf)
    nome_arquivo_sem_extensao = os.path.splitext(nome_arquivo)[0]
    arquivo_txt = os.path.join(diretorio_saida, f"{nome_arquivo_sem_extensao}.txt")

    doc = fitz.open(arquivo_pdf)
    texto = ""

    for pagina in doc.pages():
        texto += pagina.get_text()

    with open(arquivo_txt, "w", encoding="utf-8") as txt_file:
        txt_file.write(texto)

    return arquivo_txt

# Exemplo de uso
diretorio_pdfs = "C:/Users/Carlin/2023-2-Squad10/Projeto/ConversorPDF-JSON/downloads"
diretorio_txt = "C:/Users/Carlin/2023-2-Squad10/Projeto/ConversorPDF-JSON/downloads"

for nome_pdf in os.listdir(diretorio_pdfs):
    if nome_pdf.endswith(".pdf"):
        caminho_pdf = os.path.join(diretorio_pdfs, nome_pdf)
        converter_pdf_para_txt(caminho_pdf, diretorio_txt)