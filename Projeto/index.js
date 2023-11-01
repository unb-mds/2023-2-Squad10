// Função para executar a pesquisa
function search() {
    // Obtém o valor de entrada do campo de pesquisa com o id 'search-bar'
    let input = document.getElementById('search-bar').value;

    // Converte o valor de entrada em letras minúsculas para fazer uma comparação sem distinção entre maiúsculas e minúsculas
    input = input.toLowerCase();

    // Obtém uma coleção de elementos com a classe 'nav-link'
    let x = document.getElementsByClassName('nav-link');

    // Loop através dos elementos da coleção
    for (i = 0; i < x.length; i++) {
        // Verifica se o texto do elemento não inclui o valor de entrada em letras minúsculas
        if (!x[i].innerHTML.toLowerCase().includes(input)) {
            // Se não incluir, define o estilo de exibição como 'none' para ocultar o elemento
            x[i].style.display = "none";
        } else {
            // Se incluir, define o estilo de exibição como 'list-item' para exibir o elemento
            x[i].style.display = "list-item";
        }
    }
}
