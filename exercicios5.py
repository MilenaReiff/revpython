import csv

dados = [
    ['nome', 'nota1', 'nota2'],
    ['ana', '8.5', '7.8'],
    ['beto', '7', '8.9'],
    ['carlos', '5.5', '4.5'],
    ['diana', '3', '6.5']
]

with open('turma.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)

with open('turma.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    
    aprovados = []
    reprovados = []
    
    for linha in leitor:
        nome = linha[0]
        nota1 = (linha[1])