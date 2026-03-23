import csv

dados = [
    ['nome','nota1', 'nota2', 'nota3'],
    ['ana', 8.5, 7.9, 6.9],
    ['beto', 0.4, 0.3, 1.1],
    ['carla', 9.9, 10, 8.9],

]
with open ('exercicios.csv', 'w',
           encoding='utf-8',
           newline='') as arquivo:
    escritor=csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)
        print(linha)