import json

try:
    with open("banco.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    print("Banco de dados carregado com sucesso!")

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")

except json.JSONDecodeError:
    print("Erro: problema no formato do JSON.")



