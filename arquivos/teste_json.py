import json
import os

caminho = "dados_restaurantes.json"

# Verifica se o arquivo já existe
if os.path.exists(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
else:
    dados = []

ultimo_id = max(r["id"] for r in dados)
novo_id = ultimo_id + 1

# Novo restaurante que será adicionado
novo_restaurante = {
    "nome_restaurante": "Pizzaria da Vó",
    "cnpj": "12345678901234",
    "email": "vo@pizza.com",
    "senha": "segredo123",
    "id": novo_id
}

novo_restaurante2 = {
    "nome_restaurante": "oioi",
    "cnpj": "12341235151",
    "email": "voaaa@pizza.com",
    "senha": "segredo1232",
    "id": novo_id
}

novo_restaurante3 = {
    "nome_restaurante": "oioi",
    "cnpj": "12341235151",
    "email": "voaaa@pizza.com",
    "senha": "segredo1232",
    "id": novo_id
}

# Adiciona o novo restaurante à lista
dados.append(novo_restaurante2)
dados.append(novo_restaurante3)

print(novo_id)



# Salva a lista atualizada no arquivo JSON
with open(caminho, "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
