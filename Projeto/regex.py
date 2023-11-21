# Abra o arquivo txt e leia o conteúdo
with open('doficial.txt', 'r', encoding='utf-8') as f:
    texto = f.read()

# Encontre o índice inicial da parte que você deseja extrair
inicio = texto.find('LICITAÇÕES')

# Encontre o índice final (você pode precisar ajustar isso dependendo de onde termina a parte que você deseja)
fim = texto.find('PORTARIAS')

# Extraia a parte desejada
parte_desejada = texto[inicio:fim]

# Caminho para o novo arquivo
path = 'C:/Users/f1l1p/Desktop/TOP SECRET/MDS/2023-2-Squad10/Projeto/txt/dodfextraido.txt'

# Escreva a parte extraída no novo arquivo
with open(path, 'w', encoding='utf-8') as arquivo:
    arquivo.write(parte_desejada)

print(f"Parte desejada salva em {path}")
