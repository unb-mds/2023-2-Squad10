from datetime import datetime, timedelta
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def download_pdfs(start_date, end_date):
    # Inicializa o driver do navegador (Chrome neste exemplo)
    driver = webdriver.Chrome()  # ou outro driver de navegador
    
    try:
        current_date = start_date
        # Itera sobre as datas, começando da data inicial até a data final
        while current_date >= end_date:
            formatted_date = current_date.strftime("%d-%m-%Y")
            pdf_url = get_pdf_url(formatted_date)
            
            if pdf_url:
                download_pdf(pdf_url, current_date)

            # Decrementa a data atual
            current_date -= timedelta(days=1)

    finally:
        # Fecha o driver do navegador ao finalizar
        driver.quit()

def get_pdf_url(date):
    # URLs e parâmetros para busca de PDFs
    base_url = "https://diariooficialdasprefeituras.org"
    formatted_date = date if isinstance(date, str) else date.strftime("%d-%m-%Y")
    search_url = f"{base_url}/piaui/buscas/search?utf8=%E2%9C%93&q%5Bnome_or_arquivos_texto_cont%5D=&q%5Barquivos_hashFile_eq%5D=&q%5Bedicao_id_eq%5D=&q%5Bcategoria_id_eq%5D=&q%5Bunidade_entidade_id_eq%5D=&q%5Bunidade_id_eq%5D=&q%5Bedicao_data_gteq%5D={formatted_date}&q%5Bedicao_data_lteq%5D={formatted_date}&q%5Bflag_doc_diario_true%5D=0&q%5Bflag_doc_diario_true%5D=1&q%5Bflag_lrf_true%5D=0&q%5Bppa_true%5D=0&q%5Bflag_loa_true%5D=0&q%5Bflag_ldo_true%5D=0"

    # Envia uma solicitação HTTP GET para a página de busca
    response = requests.get(search_url, allow_redirects=False)
    if response.status_code == 302:
        # Se houver um redirecionamento, segue o redirecionamento
        redirect_url = response.headers['Location']
        response = requests.get(redirect_url)
        
    if response.status_code == 200:
        # Analisa o HTML da página de busca
        soup = BeautifulSoup(response.text, 'html.parser')
        pdf_link = soup.find('a', class_='fileLink')
        if pdf_link:
            # Retorna a URL do PDF se encontrada
            return f"{base_url}{pdf_link['data-href']}"
    
    # Se não encontrar a URL do PDF, imprime o HTML da página para análise
    print(f"HTML da página para {formatted_date}:\n{response.text}\n\n")
    return None

def download_pdf(pdf_url, date):
    # Cria o diretório se não existir
    download_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'downloads')
    os.makedirs(download_folder, exist_ok=True)

    # Obtém o nome do arquivo do URL
    file_name = os.path.join(download_folder, f"diario_{date.strftime('%Y-%m-%d')}.pdf")

    print(f"Baixando para a data: {date}")
    
    # Baixa o PDF diretamente usando a biblioteca requests
    response = requests.get(pdf_url)
    with open(file_name, 'wb') as pdf_file:
        pdf_file.write(response.content)

    print(f"Download concluído para a data: {date}")

# Exemplo de uso
data_inicial = datetime.strptime("31/12/2021", "%d/%m/%Y")  # Substitua pela data desejada
data_final = datetime.strptime("21/06/2021", "%d/%m/%Y")  # Substitua pela data desejada
download_pdfs(data_inicial, data_final)

