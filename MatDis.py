#DICIONARIOS

pessoas = [
    {"PessoaID": 1, "Nome": "João", "Amigos": [3], "Colegas": [4], "Parentes": [2]},
    {"PessoaID": 2, "Nome": "Maria", "Amigos": [3, 4], "Parentes": [1]},
    {"PessoaID": 3, "Nome": "José", "Colegas": [4], "Amigos": [1, 2]},
    {"PessoaID": 4, "Nome": "Joana", "Amigos": [3], "Colegas": [1, 3]}
]


def amigos_em_comum(pessoa1, pessoa2):
    amigos1 = set(pessoa1["Amigos"])
    amigos2 = set(pessoa2["Amigos"])
    amigos_em_comum = amigos1.intersection(amigos2)
    return amigos_em_comum


joao = pessoas[0]
maria = pessoas[1]
jose = pessoas[2]
joana = pessoas[3]

print("1. Amigos do João:", joao["Amigos"])
print("2. Parentes da Maria:", maria.get("Parentes", "Nenhum"))
print("3. Colegas do Jose:", jose.get("Colegas", "Nenhum"))
print("4. Colegas da Joana:", joana.get("Colegas", "Nenhum"))
print("5. Amigos em comum da Maria e da Joana:", amigos_em_comum(maria, joana))
print("6. Colegas em comum do João e do José:", set(joao["Colegas"]).intersection(set(jose.get("Colegas", []))),)
