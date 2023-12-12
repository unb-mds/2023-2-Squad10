import unittest
import json
from unittest.mock import mock_open, patch
from seu_arquivo import remover_duplicatas

class TestRemoverDuplicatas(unittest.TestCase):

    def setUp(self):
        # Dados de exemplo para teste
        self.dados_exemplo = [
            {"nome": "João", "idade": 25},
            {"nome": "Maria", "idade": 30},
            {"nome": "João", "idade": 25},
            {"nome": "Carlos", "idade": 40},
            {"nome": "Maria", "idade": 30},
        ]

    def test_remover_duplicatas(self):
        # Mock da função open para simular a leitura do arquivo
        with patch('builtins.open', mock_open(read_data=json.dumps(self.dados_exemplo))):
            # Mock da função json.dump para simular a escrita do arquivo
            with patch('json.dump') as mock_json_dump:
                remover_duplicatas('entrada.json', 'saida.json')

        # Verificar se a função json.dump foi chamada corretamente
        mock_json_dump.assert_called_once()

        # Obter os argumentos que foram passados para json.dump
        _, args, _ = mock_json_dump.mock_calls[0]
        dados_sem_duplicatas = json.loads(args[0])

        # Verificar se as duplicatas foram removidas corretamente
        self.assertEqual(len(dados_sem_duplicatas), 3)

if __name__ == '__main__':
    unittest.main()
