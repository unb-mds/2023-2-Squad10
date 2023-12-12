import unittest
from unittest.mock import mock_open, patch
from seu_arquivo import ExtratorDeDados

class TestExtratorDeDados(unittest.TestCase):

    def setUp(self):
        self.extrator = ExtratorDeDados()

    def test_extrairNomeMunicipio(self):
        bloco = "Texto contendo nome de município Acauã"
        resultado = self.extrator.extrairNomeMunicipio(bloco)
        self.assertEqual(resultado, "Acauã")

    def test_escritaDatabase(self):
        # Criando um mock do open para simular a leitura do arquivo
        with patch('builtins.open', mock_open()) as m:
            dados = {"nomeMunicipio": "Acauã", "dataPost": "2023-01-01", "numeroLicitacoes": 2}
            self.extrator.escritaDatabase(dados)

        # Verificando se o arquivo foi aberto e escrito corretamente
        m.assert_called_once_with("dados.json", "w", encoding="utf-8")
        m().write.assert_called_once_with('[\n    {\n        "nomeMunicipio": "Acauã",\n        "dataPost": "2023-01-01",\n        "numeroLicitacoes": 2\n    }\n]')

if __name__ == '__main__':
    unittest.main()
