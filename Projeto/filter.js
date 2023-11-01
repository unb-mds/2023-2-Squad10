$(document).ready(function () {
    // Função para filtrar a tabela
    function filterTable() {
        var palavraChave = $('#palavraChave').val().toLowerCase();
        var numEdicao = $('#numEdicao').val().toLowerCase();
        var periodoPublicacao = $('#periodoPublicacao').val().toLowerCase();

        $('table tbody tr').each(function () {
            var row = $(this);
            var documento = row.find('td:eq(1)').text().toLowerCase(); // Suponhamos que o título do documento está na segunda coluna.

            var showRow = true;

            if (palavraChave && documento.indexOf(palavraChave) === -1) {
                showRow = false;
            }
            if (numEdicao && row.find('td:eq(0)').text().toLowerCase() !== numEdicao) { // A primeira coluna contém o Nº da Edição.
                showRow = false;
            }
            if (periodoPublicacao && documento.indexOf(periodoPublicacao) === -1) {
                showRow = false;
            }

            row.toggle(showRow);
        });
    }

    // Chamar a função de filtro ao enviar o formulário
    $('form').submit(function (e) {
        e.preventDefault();
        filterTable();
    });
});
