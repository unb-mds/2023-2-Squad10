import unittest
import json
from collections import defaultdict
from unittest.mock import mock_open, patch
from seu_arquivo import organizar_e_salvar_por_municipio

class TestOrganizarESalvarPorMunicipio(unittest.TestCase):

    def setUp(self):
        # Dados de exemplo para teste
        self.dados_exemplo = [
            {"Municipio": "Acauã", "Dado": "Valor1"},
            {"Municipio": "Acauã", "Dado": "Valor2"},
            {"Municipio": "Bela Vista", "Dado": "Valor3"},
        ]

    @patch('seu_arquivo.open', new_callable=mock_open, read_data=json.dumps(self.dados_exemplo))
    @patch('seu_arquivo.json.dump')
    def test_organizar_e_salvar_por_municipio(self, mock_json_dump, mock_open):
        organizar_e_salvar_por_municipio("entrada.json")

        # Verificar se a função json.dump foi chamada corretamente
        mock_json_dump.assert_called_once()

        # Obter os argumentos que foram passados para json.dump
        _, args, _ = mock_json_dump.mock_calls[0]
        dados_salvos = json.loads(args[0])

        # Verificar se os dados foram organizados corretamente
        self.assertEqual(len(dados_salvos), 2)

if __name__ == '__main__':
    unittest.main()
