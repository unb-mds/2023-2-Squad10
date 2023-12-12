import unittest
import os
import fitz  # PyMuPDF
from seu_modulo import converter_pdf_para_txt

class TestConversorPDF(unittest.TestCase):
    def setUp(self):
        # Crie um diretório temporário para os testes
        self.diretorio_teste = "caminho/do/seu/diretorio/temporario"
        os.makedirs(self.diretorio_teste, exist_ok=True)

    def tearDown(self):
        # Remova o diretório temporário após os testes
        os.rmdir(self.diretorio_teste)

    def test_converte_pdf_para_txt(self):
        # Cria um arquivo PDF de teste no diretório temporário
        caminho_pdf_teste = os.path.join(self.diretorio_teste, "test_file.pdf")
        with open(caminho_pdf_teste, "w", encoding="utf-8") as pdf_file:
            pdf_file.write("Conteúdo do PDF de teste")

        # Chama a função de conversão
        caminho_txt_resultado = converter_pdf_para_txt(caminho_pdf_teste, self.diretorio_teste)

        # Verifica se o arquivo TXT foi criado
        self.assertTrue(os.path.isfile(caminho_txt_resultado))

        # Verifica se o conteúdo do arquivo TXT é o esperado
        with open(caminho_txt_resultado, "r", encoding="utf-8") as txt_file:
            conteudo_txt = txt_file.read()
            self.assertEqual(conteudo_txt, "Conteúdo do PDF de teste")

if __name__ == "__main__":
    unittest.main()
