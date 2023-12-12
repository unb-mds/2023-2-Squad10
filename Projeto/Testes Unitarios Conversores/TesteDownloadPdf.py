import unittest
from unittest.mock import Mock, patch
from datetime import datetime, timedelta
from seu_arquivo import get_pdf_url

class TestGetPdfUrl(unittest.TestCase):

    def test_pdf_url_found(self):
        with patch('seu_arquivo.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.text = '<a class="fileLink" data-href="/pdf-link">PDF Link</a>'
            result = get_pdf_url("01-01-2023")
            self.assertEqual(result, "https://diariooficialdasprefeituras.org/pdf-link")

    def test_pdf_url_not_found(self):
        with patch('seu_arquivo.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.text = '<p>No PDF link found</p>'
            result = get_pdf_url("01-01-2023")
            self.assertIsNone(result)

    def test_redirect_and_pdf_url_found(self):
        with patch('seu_arquivo.requests.get') as mock_get:
            redirect_mock = Mock()
            redirect_mock.status_code = 302
            redirect_mock.headers = {'Location': 'https://diariooficialdasprefeituras.org/redirect-link'}
            mock_get.side_effect = [redirect_mock, Mock(status_code=200, text='<a class="fileLink" data-href="/pdf-link">PDF Link</a>')]

            result = get_pdf_url("01-01-2023")
            self.assertEqual(result, "https://diariooficialdasprefeituras.org/pdf-link")

if __name__ == '__main__':
    unittest.main()
