import csv


with open('exercicios.csv', 'r', encoding='utf-8') as arquivo_origem:
    leitor = csv.reader(arquivo_origem)
    dados = list(leitor)


novos_dados = []
cabecalho = dados[0].copy()
cabecalho.append('media')
novos_dados.append(cabecalho)


for i in range(1, len(dados)):
    nome = dados[i][0]
    notas = [float(nota) for nota in dados[i][1:]]
    media = sum(notas) / len(notas)
    
    nova_linha = dados[i].copy()
    nova_linha.append(round(media, 2))
    novos_dados.append(nova_linha)
    
    
    print(f"{nome}: {media:.2f}")


with open('notas_com_media.csv', 'w', encoding='utf-8', newline='') as arquivo_destino:
    escritor = csv.writer(arquivo_destino)
    escritor.writerows(novos_dados)

print("\nArquivo 'notas_com_media.csv' criado com sucesso!")