
import csv

dados = [
    ['nome','nota'],
    ['roberta', 8.5],
    ['felipe', 0.4],
    ['Cataina', 9.9],

]
with open ('exercicios.csv', 'w',
           encoding='utf-8',
           newline='') as arquivo:
    escritor=csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)


