// Funçao para adiconar as Barra na Data e bloqueiar Letras
const dataInput = document.getElementById('data');
dataInput.addEventListener('input', (event) => {
    // Remove caracteres não numéricos
    const numericValue = event.target.value.replace(/\D/g, '');

    // Insere as barras automaticamente
    if (numericValue.length >= 2) {
        const formattedValue = `${numericValue.slice(0, 2)}/${numericValue.slice(2, 4)}/${numericValue.slice(4, 8)}`;
        dataInput.value = formattedValue;
    } else {
        dataInput.value = numericValue;
    }
});

//Funçao para Buscar apenas por Numero de Edição
const edicaoInput = document.getElementById('edicao');

edicaoInput.addEventListener('input', () => {
    const edicaoValue = edicaoInput.value;

    // Verifica se o valor contém letras
    if (/[a-zA-Z]/.test(edicaoValue)) {
        // Contém letras, exibe um alerta
        alert('Apenas números são permitidos!');
        edicaoInput.value = ''; // Limpa o campo
    }
});

function verificarNumero() {
    const edicaoValue = edicaoInput.value;

    // Verifica se o valor é um número
    if (/^\d+$/.test(edicaoValue)) {
        // É um número, ação desejada
        console.log('Número válido: ' + edicaoValue);
    } else {
        // Não é um número, exibe um alerta (opcional)
        alert('Apenas números são permitidos!');
        edicaoInput.value = ''; // Limpa o campo (opcional)
    }
}

// Função que faz a busca na tabela

function verificarNumero() {
    // Obtenha os valores digitados nos campos de entrada
    var data = document.getElementById("data").value.trim();
    var edicao = document.getElementById("edicao").value.trim();

    // Selecione a tabela
    var tabela = document.getElementById("tabelaResultados").getElementsByTagName('tbody')[0];
    var linhas = tabela.getElementsByTagName('tr');

    // Loop através das linhas da tabela
    for (var i = 0; i < linhas.length; i++) {
        var colunas = linhas[i].getElementsByTagName('td');
        var numeroEdicao = colunas[0].textContent;
        var dataEdicao = colunas[1].textContent;

        // Verifique se a linha corresponde aos critérios de busca
        if (numeroEdicao === edicao || dataEdicao === data) {
            linhas[i].style.display = '';
        } else {
            linhas[i].style.display = 'none';
        }
    }
}



