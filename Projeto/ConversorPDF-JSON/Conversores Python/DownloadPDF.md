<!--

S
A
I

D
A
Q
U
I

S
E
U

C
U
R
I
O
S
O

ASS: xGabrielCv 

-->


<!-- Adiciona distintivos (shields) do GitHub -->
![GitHub repo size](https://img.shields.io/github/repo-size/unb-mds/2023-2-Squad10?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/unb-mds/2023-2-Squad10?style=for-the-badge)
![GitHub views](https://komarev.com/ghpvc/?username=unb-mds&repo=2023-2-Squad10&color=blueviolet&style=for-the-badge&label=Views)

<!-- Título centralizado -->
<div align="center">
  <h2>Bem-vindo ao nosso repositório! </h2>
</div> 

<!-- Título centralizado -->
<div align="center">
  <h2>Diario Oficial do Piaui UnB </h2>
</div> 

<!-- Título centralizado -->
<div align="center">
  <h2>🎯 Download PDF </h2>
</div> 

• Este é um script Python para baixar os diários oficiais de prefeituras do Piauí .

<!-- Título centralizado -->
<div align="center">
  <h2>👩🏾‍💻 Funcionalidades </h2>
</div> 

Este script oferece as seguintes funcionalidades:

• O código utiliza Selenium e BeautifulSoup para automatizar o download de Diários Oficiais em formato PDF,
define um intervalo de datas (início e fim) para iterar sobre as páginas de busca do Diário Oficial,
a cada iteração, procura por links para os PDFs dos Diários Oficiais na página correspondente à data.

• Inicializa um driver de navegador (Chrome neste exemplo) utilizando a biblioteca Selenium,
navega entre as páginas de busca do Diário Oficial, manipulando o navegador para encontrar os links dos PDFs.

• Utiliza a biblioteca requests para enviar solicitações HTTP e baixar os PDFs diretamente,
analisa o HTML das páginas de busca usando BeautifulSoup para extrair os links dos PDFs,
cria uma pasta de downloads, se não existir, e salva os PDFs com nomes baseados na data.

• Itera sobre as datas no intervalo especificado, buscando e baixando os Diários Oficiais correspondentes,
a cada iteração, a data é formatada, a URL do PDF é obtida, e o download é realizado se a URL for válida.

<!-- Título centralizado -->
<div align="center">
  <h2>🤞 Como executar o script </h2>
</div> 

### 1. 🔑 Pré-requisitos
Esses são os nossos pré-requisitos:
- [Python3](https://www.python.org/downloads/)
- [Google Chrome](https://www.google.pt/intl/pt-PT/chrome/?brand=JJTC&gclid=CjwKCAiAjfyqBhAsEiwA-UdzJMg9rrK6120NVHWXKNS773PEP1Du65dqiZWcktY_KxHpRkV4SV03XBoCri8QAvD_BwE&gclsrc=aw.ds)
- [ChromeDriver](https://chromedriver.chromium.org/downloads)


<!-- Adiciona a lista de bibliotecas para copiar -->
### 2. 📑 Instalação das bibliotecas do Python
Aqui estão as bibliotecas do Python usadas :


```
pip install requests
```
```
pip install selenium
```
```
pip install BeautifulSoup
```


<!-- Adiciona a funçao de copiar o link do repositorio -->
### 3. 📍 Clonar o Repositório
Vamos começar clonando um repositório do GitHub em um diretório local através do terminal, conforme indicado a seguir:
```
git clone https://github.com/unb-mds/2023-2-Squad10.git
```
  	
  
<div align="center">
  <h2>⚙️ Configurações do script </h2>
</div>

• O script solicitará as datas iniciais e finais para baixar os PDFs correspondentes.


• Certifique-se de ter uma conexão com a internet ativa.


• Os arquivos PDF serão baixados no diretório 'downloads', e o progresso será exibido no console.

<div align="center">
  <h2>👩‍💻 Contribuidores </h2>
</div> 
<!-- Foto dos participantes do grupo -->
<div align="center"> 
 <img src="https://avatars.githubusercontent.com/u/119907827?v=4" width="100"/>
 <img src="https://avatars.githubusercontent.com/u/87997616?v=4" width="100" />
 <img src="https://avatars.githubusercontent.com/u/90454615?v=4" width="100"/>
 <img src="https://avatars.githubusercontent.com/u/124631520?v=4" width="100"/>
 <img src="https://avatars.githubusercontent.com/u/98980548?v=4" width="100"/>
 <img src="https://avatars.githubusercontent.com/u/101183266?v=4" width="100"/>
 <img src="https://avatars.githubusercontent.com/u/109704535?v=4" width="100"/>
</div>

<div align="center">
  <h2>📄 Documentação </h2>
</div>

### • A documentação do projeto pode ser encontrada clicando [AQUI](https://unb-mds.github.io/2023-2-Squad10/).




<div align="center">
  <h2>©️ Licença </h2>
</div>



<!-- Criador e licença -->
### ESTE SOFTWARE ESTÁ SOB LICENÇA: [MIT](https://github.com/nhn/tui.editor/blob/master/LICENSE) ©
### FEITO POR: [xGabrielCv](https://github.com/xGabrielCv)
<!-- Icons das ferramentas e linguagens ultilizadas -->
<p align="left">
    <a href="https://www.python.org" target="_blank" rel="noreferrer">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="30" height="30"/>
    </a>
    <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="30" height="30"/>
    </a>
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="30" height="30"/>
    </a>
    <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer">
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="30" height="30"/>
    </a>
    <a href="https://git-scm.com/" target="_blank" rel="noreferrer">
        <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="30" height="30"/>
    </a>
    <a href="https://www.figma.com/" target="_blank" rel="noreferrer">
        <img src="https://www.vectorlogo.zone/logos/figma/figma-icon.svg" alt="figma" width="30" height="30"/>
    </a>
</p>
