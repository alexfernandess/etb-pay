import pandas as pd
import random

# Carrega o arquivo
df = pd.read_csv('log_transacoes_300_utf8.csv')

# Listas para gerar nomes
nomes = ["João", "Maria", "Carlos", "Ana", "Marcos", "Fernanda", "Pedro", "Juliana", "Lucas", "Mariana", "Rafael", "Camila", "Rodrigo", "Letícia", "Marcelo", "Beatriz", "Felipe", "Amanda", "Gustavo", "Carolina"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Costa", "Ribeiro", "Martins", "Carvalho", "Almeida", "Lopes", "Soares", "Fernandes"]

# Mapeia os clientes únicos
clientes_unicos = df['Remetente'].unique()
nomes_ficticios = set()

while len(nomes_ficticios) < len(clientes_unicos):
    nomes_ficticios.add(f"{random.choice(nomes)} {random.choice(sobrenomes)}")

nomes_ficticios = list(nomes_ficticios)
mapa_nomes = dict(zip(clientes_unicos, nomes_ficticios))

# Aplica a substituição
df['Remetente'] = df['Remetente'].map(mapa_nomes)

# Salva o novo arquivo
df.to_csv('log_transacoes_300_ficticios.csv', index=False, encoding='utf-8')
print("Arquivo log_transacoes_300_ficticios.csv gerado com sucesso!")