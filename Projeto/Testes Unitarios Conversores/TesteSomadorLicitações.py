import unittest
from unittest.mock import mock_open, patch
import json
from seu_arquivo import processar_dados_licitacoes

class TestProcessarDadosLicitacoes(unittest.TestCase):

    def setUp(self):
        # Dados de exemplo para teste
        self.dados_exemplo = [
            {"nomeMunicipio": "Acauã", "dataPost": "2023-01-15", "numeroLicitacoes": 2},
            {"nomeMunicipio": "Bela Vista", "dataPost": "2023-01-15", "numeroLicitacoes": 1},
            {"nomeMunicipio": "Acauã", "dataPost": "2023-02-20", "numeroLicitacoes": 3},
            {"nomeMunicipio": "Bela Vista", "dataPost": "2023-02-20", "numeroLicitacoes": 1},
        ]

    @patch('seu_arquivo.open', new_callable=mock_open, read_data=json.dumps(self.dados_exemplo))
    @patch('seu_arquivo.json.dump')
    def test_processar_dados_licitacoes(self, mock_json_dump, mock_open):
        processar_dados_licitacoes("dados.json")

        # Verificar se a função json.dump foi chamada corretamente
        mock_json_dump.assert_called_once()

        # Obter os argumentos que foram passados para json.dump
        _, args, _ = mock_json_dump.mock_calls[0]
        resultados_salvos = json.loads(args[0])

        # Verificar se os resultados foram processados corretamente
        self.assertEqual(len(resultados_salvos), 2)
        self.assertEqual(resultados_salvos[0]['Municipio'], 'Acauã')
        self.assertEqual(resultados_salvos[0]['Mes'], '01')
        self.assertEqual(resultados_salvos[0]['TotalLicitacoes'], 3)
        self.assertEqual(resultados_salvos[1]['Municipio'], 'Bela Vista')
        self.assertEqual(resultados_salvos[1]['Mes'], '01')
        self.assertEqual(resultados_salvos[1]['TotalLicitacoes'], 1)

if __name__ == '__main__':
    unittest.main()
