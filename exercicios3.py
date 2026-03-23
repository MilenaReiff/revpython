import csv

dados = [
    ['nome','nota1', 'nota2', 'nota3'],
    ['ana', 8.5, 7.9, 6.9],
    ['beto', 0.4, 0.3, 1.1],
    ['carla', 9.9, 10, 8.9],
]


with open('exercicios.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)

print("\nCálculo das Médias:")
for i in range(1, len(dados)):
    nome = dados[i][0]

    notas = [float(nota) for nota in dados[i][1:]] 
    
    media = sum(notas) / len(notas)
    print(f"{nome}: {media:.2f}")
