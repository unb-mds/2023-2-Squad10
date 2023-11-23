import fitz  # PyMuPDF
import re
import json
import os


"""
{
    municipio: nome do munucipio
    data: data do dia de extração
    nomeação: bool indicando se há 
    extração: bool indicando se há
}
"""


class ExtratorDeDados:
    def __init__(self):
        self.nomeDosMunicipios = [
            "Acauã",
            "Agricolândia",
            "Água Branca",
            "Alagoinha do Piauí",
            "Alegrete do Piauí",
            "Alto Longá",
            "Altos",
            "Alvorada do Gurgueia",
            "Amarante",
            "Angical do Piauí",
            "Anísio de Abreu",
            "Antônio Almeida",
            "Aroazes",
            "Aroeiras do Itaim",
            "Arraial",
            "Assunção do Piauí",
            "Avelino Lopes",
            "Baixa Grande do Ribeiro",
            "Barra d'Alcântara",
            "Barras",
            "Barreiras do Piauí",
            "Barro Duro",
            "Batalha",
            "Bela Vista do Piauí",
            "Belém do Piauí",
            "Beneditinos",
            "Bertolínia",
            "Betânia do Piauí",
            "Boa Hora",
            "Bocaina",
            "Bom Jesus",
            "Bom Princípio do Piauí",
            "Bonfim do Piauí",
            "Boqueirão do Piauí",
            "Brasileira",
            "Brejo do Piauí",
            "Buriti dos Lopes",
            "Buriti dos Montes",
            "Cabeceiras do Piauí",
            "Cajazeiras do Piauí",
            "Cajueiro da Praia",
            "Caldeirão Grande do Piauí",
            "Campinas do Piauí",
            "Campo Alegre do Fidalgo",
            "Campo Grande do Piauí",
            "Campo Largo do Piauí",
            "Campo Maior",
            "Canavieira",
            "Canto do Buriti",
            "Capitão de Campos",
            "Capitão Gervásio Oliveira",
            "Caracol",
            "Caraúbas do Piauí",
            "Caridade do Piauí",
            "Castelo do Piauí",
            "Caxingó",
            "Cocal",
            "Cocal de Telha",
            "Cocal dos Alves",
            "Coivaras",
            "Colônia do Gurgueia",
            "Colônia do Piauí",
            "Conceição do Canindé",
            "Coronel José Dias",
            "Corrente",
            "Cristalândia do Piauí",
            "Cristino Castro",
            "Curimatá",
            "Currais",
            "Curral Novo do Piauí",
            "Curralinhos",
            "Demerval Lobão",
            "Dirceu Arcoverde",
            "Dom Expedito Lopes",
            "Dom Inocêncio",
            "Domingos Mourão",
            "Elesbão Veloso",
            "Eliseu Martins",
            "Esperantina",
            "Fartura do Piauí",
            "Flores do Piauí",
            "Floresta do Piauí",
            "Floriano",
            "Francinópolis",
            "Francisco Ayres",
            "Francisco Macedo",
            "Francisco Santos",
            "Fronteiras",
            "Geminiano",
            "Gilbués",
            "Guadalupe",
            "Guaribas",
            "Hugo Napoleão",
            "Ilha Grande",
            "Inhuma",
            "Ipiranga do Piauí",
            "Isaías Coelho",
            "Itainópolis",
            "Itaueira",
            "Jacobina do Piauí",
            "Jaicós",
            "Jardim do Mulato",
            "Jatobá do Piauí",
            "Jerumenha",
            "João Costa",
            "Joaquim Pires",
            "Joca Marques",
            "José de Freitas",
            "Juazeiro do Piauí",
            "Júlio Borges",
            "Jurema",
            "Lagoa Alegre",
            "Lagoa de São Francisco",
            "Lagoa do Barro do Piauí",
            "Lagoa do Piauí",
            "Lagoa do Sítio",
            "Lagoinha do Piauí",
            "Landri Sales",
            "Luís Correia",
            "Luzilândia",
            "Madeiro",
            "Manoel Emídio",
            "Marcolândia",
            "Marcos Parente",
            "Massapê do Piauí",
            "Matias Olímpio",
            "Miguel Alves",
            "Miguel Leão",
            "Milton Brandão",
            "Monsenhor Gil",
            "Monsenhor Hipólito",
            "Monte Alegre do Piauí",
            "Morro Cabeça no Tempo",
            "Morro do Chapéu do Piauí",
            "Murici dos Portelas",
            "Nazaré do Piauí",
            "Nazária",
            "Nossa Senhora de Nazaré",
            "Nossa Senhora dos Remédios",
            "Nova Santa Rita",
            "Novo Oriente do Piauí",
            "Novo Santo Antônio",
            "Oeiras",
            "Olho d'Água do Piauí",
            "Padre Marcos",
            "Paes Landim",
            "Pajeú do Piauí",
            "Palmeira do Piauí",
            "Palmeirais",
            "Paquetá",
            "Parnaguá",
            "Parnaíba",
            "Passagem Franca do Piauí",
            "Patos do Piauí",
            "Pau d'Arco do Piauí",
            "Paulistana",
            "Pavussu",
            "Pedro II",
            "Pedro Laurentino",
            "Picos",
            "Pimenteiras",
            "Pio IX",
            "Piracuruca",
            "Piripiri",
            "Porto",
            "Porto Alegre do Piauí",
            "Prata do Piauí",
            "Queimada Nova",
            "Redenção do Gurgueia",
            "Regeneração",
            "Riacho Frio",
            "Ribeira do Piauí",
            "Ribeiro Gonçalves",
            "Rio Grande do Piauí",
            "Santa Cruz do Piauí",
            "Santa Cruz dos",
        ]

    def extrairNomeMunicipio(self, bloco):
        # Create a regular expression pattern for matching municipality names
        pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, self.nomeDosMunicipios)) + r')\b', re.IGNORECASE)

        # Find all matches in the block of text
        matches = pattern.findall(bloco)

        # If matches are found, return the first one; otherwise, return a default value
        return matches[0] if matches else "Publicado Prefeitura sem Nome"

    def escritaDatabase(self, dados):
        try:
            with open("dados.json", "r", encoding="utf-8") as file:
                dados_escritos = json.load(file)
        except FileNotFoundError:
            dados_escritos = []

        dados_escritos.append(dados)
        with open("dados.json", "w", encoding="utf-8") as file:
            json.dump(dados_escritos, file, indent=4, ensure_ascii=False)

    def extrairDados(self, nomeDoArquivo):
        with open(nomeDoArquivo, "r", encoding="utf-8", errors="ignore") as arquivo:
            texto = arquivo.read()
            padrao = re.compile(r"(LICITAÇÕES|LICITAÇOES )", re.IGNORECASE)

            resultados = padrao.finditer(texto)

            for correspondencia in resultados:
                inicio_contexto = max(correspondencia.start() - 150, 0)
                fim_contexto = min(correspondencia.end() + 250, len(texto))

                contexto = texto[inicio_contexto:fim_contexto]

                nomeDoMunicipio = self.extrairNomeMunicipio(contexto)
                data = arquivo.name
                data = data[:-4]
                data = data[-10:]

                numero_licitacoes = contexto.lower().count("licitaçõ")
                dados_novos = {
                    "nomeMunicipio": nomeDoMunicipio,
                    "dataPost": data,
                    "numeroLicitacoes": numero_licitacoes,
                }
                self.escritaDatabase(dados_novos)

    def extraiGeral(self):
        diretorio_txt = "C:/Users/Carlin/2023-2-Squad10/Projeto/ConversorPDF-JSON/downloads"
        arquivos = os.listdir(diretorio_txt)

        for arq in arquivos:
            arqPath = os.path.join(diretorio_txt, arq)
            self.extrairDados(arqPath)

# Create an instance of ExtratorDeDados
regex = ExtratorDeDados()
regex.extraiGeral()