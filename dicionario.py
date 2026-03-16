#Dicionário
#aluno=  {
    #'nome': 'Fulano',
    #'matricula': '12346',
    #'turma': '1E',
    #'notas': [7.5, 8, 5] #pode ter uma lista dentro do dicionário
#}
#print(aluno) #mostra o dicionáio inteiro
#print(aluno['nome']) #mostra apenas a chave/posição nome
#print(aluno['matricula'])
#print('notas', aluno ['notas'])
#aluno['nome':] = 'ciclano' #altera o valor detro do dicionário
#print(aluno['nome'])
#11)
#contato = {
    #'nome': 'Fulano',
    #'tel': '32998374539',
    #'email': 'fulano123@mail.com',
    #'cidade': 'riodejaneiro'
#}
#print(contato.items())
#contato['instagram'] = 'fulano_ofc'
#print(contato['instagram'])
#if 'email' in contato:
    #print("A chave email existe!")
#del contato ['tel']
#removido = contato.pop('tel')
#print(contato.items())
#12)
#frase = 'o rato roeu a roupa do rei de roma'
#palavras = frase.split()
#contagem = {}

#for p in palavras:
    #if p in contagem:
        # já existe no dic 
        # se sim soma +1
        #contagem[p] = contagem[p] + 1
    #else:
        # n existe
        # mantenha o valor
        #contagem[p] = 1

#for chave, valor in contagem.items():
    #print(f'{chave}: {valor}')
#13)
#turma = {
        #'tiaguinho': [7.6, 7.9, 5.9],
        #'isabela': [9.6, 7.2, 9.9],
        #'aniger': [10, 3.2, 5.0],
        #'milena': [10, 10, 9.9],
#}

#for chave, valor in turma.items():     # itera por pares
    #print(f'{chave}: {valor}')
    #media = sum(valor) / len(valor)

    #if #media >= 6:
        #print("Aprovado")
        #situacao = "aprovado"
    #else:
        #print ("Reprovado")
        #situacao = "reprovado"
#14)
info1 = {
    'nome': 'Notebook', 
    'preco': '400000'
}
info2 = {
    'marca': 'positivo', 
    'estoque': '10000000000000000000000000000000000000000'
}
resultado = info1 | info2  
info1['preco'] = 3200.00 
print (resultado)






