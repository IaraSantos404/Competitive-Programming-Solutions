# EXPLICAÇÃO DO PROBLEMA"
# Alice tem n balas, onde a i-ésima bala é do tipo candyType[i]. Alice percebeu que começou
# a ganhar peso, então ela foi ao médico.
# O médico aconselhou Alice a comer apenas n / 2 das balas que ela tem (n é sempre par).
# Alice gosta muito das suas balas e quer comer o máximo possível de tipos diferentes de
# balas, ainda assim seguindo o conselho do médico.
# Dada a lista de inteiros candyType de tamanho n, retorne o número máximo de tipos
# diferentes de balas que ela pode comer, se ela comer no máximo n / 2 delas.
# Exemplo 1:
# Entrada: candyType = [1,1,2,2,3,3]
# Saída: 3
# Explicação: Alice pode comer no máximo 6 / 2 = 3 balas. Como há apenas 3 tipos de bala,
# ela pode comer uma de cada tipo.
# Exemplo 2:
# Entrada: candyType = [1,1,2,3]
# Saída: 2
# Explicação: Alice pode comer no máximo 4 / 2 = 2 balas. Não importa se ela come os tipos
# [1,2], [1,3] ou [2,3], ela ainda poderá comer no máximo 2 tipos diferentes.
# Exemplo 3:
# Entrada: candyType = [6,6,6,6]
# Saída: 1
# Explicação: Alice pode comer no máximo 4 / 2 = 2 balas. Mesmo que ela possa comer 2
# balas, há apenas 1 tipo disponível.


#RESOLUÇÃO
vetor = []
difs = []

n = int(input())

for i in range(n):
    num = int(input())
    if num not in difs:
        difs.append(num)
    vetor.append(num)

#tam = quantidade q ela pode comer
# len(difs) = quantidade de doces q tem diferentes
tam = len(vetor)/2
result = tam if tam<=len(difs) else len(difs)

print(int(result))
