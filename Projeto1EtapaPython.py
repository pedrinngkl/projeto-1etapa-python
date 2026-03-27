import json
from datetime import datetime

try:
    with open("banco.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
except FileNotFoundError:
    dados = {}
except json.JSONDecodeError:
    print("Erro: problema no formato do JSON.")
    raise SystemExit(1)

if not isinstance(dados, dict):
    dados = {}

dados.setdefault("pecas", [])
dados.setdefault("produtos", [])
dados.setdefault("historico_vendas", [])


def salvar_banco():
    dados["produtos"] = []
    for i in range(len(nomes_produtos)):
        dados["produtos"].append(
            {
                "id": ids_produtos[i],
                "nome": nomes_produtos[i],
                "custo_producao": custos_producao[i],
                "preco_venda": precos_venda[i],
                "estoque_atual": estoque_atual[i],
            }
        )

    dados["historico_vendas"] = historico_vendas

    with open("banco.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)


def proximo_id_produto():
    maior_id = 0

    for peca in dados.get("pecas", []):
        try:
            maior_id = max(maior_id, int(peca.get("id", 0)))
        except (ValueError, TypeError):
            continue

    for id_produto in ids_produtos:
        try:
            maior_id = max(maior_id, int(id_produto))
        except (ValueError, TypeError):
            continue

    return maior_id + 1


def encontrar_indice_produto(nome_busca):
    nome_busca = nome_busca.strip().lower()
    for i, nome in enumerate(nomes_produtos):
        if nome.strip().lower() == nome_busca:
            return i
    return -1


def adicionar_peca_como_produto(nome_busca):
    nome_busca = nome_busca.strip().lower()

    for peca in dados.get("pecas", []):
        nome_peca = str(peca.get("peca", ""))
        if nome_peca.strip().lower() != nome_busca:
            continue

        try:
            id_peca = int(peca.get("id", proximo_id_produto()))
        except (ValueError, TypeError):
            id_peca = proximo_id_produto()

        ids_produtos.append(id_peca)
        nomes_produtos.append(nome_peca)
        custos_producao.append(0.0)
        precos_venda.append(0.0)
        estoque_atual.append(0)
        salvar_banco()
        return len(nomes_produtos) - 1

    return -1


def agora_formatado():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


# Variáveis iniciais (mesma estrutura de listas)
faturamento_total = 0
ids_produtos = []
nomes_produtos = []
custos_producao = []
precos_venda = []
estoque_atual = []
historico_vendas = []
opcao_menu = 0

# Carrega produtos já salvos no JSON para as listas
for produto in dados.get("produtos", []):
    ids_produtos.append(int(produto.get("id", 0)))
    nomes_produtos.append(str(produto.get("nome", "")))
    custos_producao.append(float(produto.get("custo_producao", 0)))
    precos_venda.append(float(produto.get("preco_venda", 0)))
    estoque_atual.append(int(produto.get("estoque_atual", 0)))

for venda in dados.get("historico_vendas", []):
    historico_vendas.append(str(venda))

for venda in historico_vendas:
    try:
        valor = float(venda.split("R$")[-1])
        faturamento_total += valor
    except ValueError:
        continue

# Loop principal (while)
while True:
    print("\n--- MENU PY INDÚSTRIAS ---")
    print("1. Cadastrar Produto")
    print("2. Registrar Produção (Entrada)")
    print("3. Registrar Venda (Saída)")
    print("4. Buscar Produto")
    print("5. Relatório de Vendas")
    print("6. Sair")

    try:
        opcao_menu = int(input("Escolha uma opção: "))
    except KeyboardInterrupt:
        print("\nEncerrando sistema...")
        break
    except ValueError:
        print("Erro: Digite um número inteiro!")
        continue

    # Estrutura de Decisão (if/elif/else)
    if opcao_menu == 1:
        print("\n-- Cadastro de Produto --")
        nome = input("Nome do veículo: ")

        # Validação com (while e break)
        while True:
            try:
                custo = float(input("Custo de produção: "))
                break
            except ValueError:
                print("Valor inválido. Tente novamente.")

        while True:
            try:
                preco = float(input("Preço de venda: "))
                break
            except ValueError:
                print("Valor inválido.")

        novo_id = proximo_id_produto()
        ids_produtos.append(novo_id)
        nomes_produtos.append(nome)
        custos_producao.append(custo)
        precos_venda.append(preco)
        estoque_atual.append(0)
        salvar_banco()
        print(f"Produto {nome} cadastrado com sucesso! ID: {novo_id}")

    elif opcao_menu == 2:
        print("\n-- Registrar Produção --")
        busca_nome = input("Nome do produto para produzir: ")
        i = encontrar_indice_produto(busca_nome)

        if i == -1:
            i = adicionar_peca_como_produto(busca_nome)

        if i == -1:
            print("Produto não encontrado.")
            continue

        try:
            qtd = int(input(f"Quantidade a produzir de {nomes_produtos[i]}: "))
        except ValueError:
            print("Quantidade inválida.")
            continue

        estoque_atual[i] += qtd
        salvar_banco()
        print(f"Novo estoque de {nomes_produtos[i]}: {estoque_atual[i]}")

    elif opcao_menu == 3:
        print("\n-- Registrar Venda --")
        busca_nome = input("Nome do produto vendido: ")
        i = encontrar_indice_produto(busca_nome)

        if i == -1:
            i = adicionar_peca_como_produto(busca_nome)

        if i == -1:
            print("Produto não encontrado para venda.")
            continue

        try:
            qtd = int(input(f"Quantidade vendida de {nomes_produtos[i]}: "))
        except ValueError:
            print("Quantidade inválida.")
            continue

        if estoque_atual[i] >= qtd:
            if precos_venda[i] <= 0:
                while True:
                    try:
                        precos_venda[i] = float(input("Preço de venda não definido. Informe o preço: "))
                        break
                    except ValueError:
                        print("Valor inválido.")

            estoque_atual[i] -= qtd
            valor_venda = qtd * precos_venda[i]
            faturamento_total += valor_venda
            historico_vendas.append(
                f"[{agora_formatado()}] Venda: {qtd}x {nomes_produtos[i]} - Total: R${valor_venda:.2f}"
            )
            salvar_banco()
            print(f"Venda registrada! Faturamento: +R${valor_venda:.2f}")
        else:
            print("Estoque insuficiente!")

    elif opcao_menu == 4:
        print("\n-- Buscar Produto --")
        termo = input("Digite parte do nome: ").strip().lower()
        print("Resultados:")
        encontrou = False

        # (for) simples
        for nome in nomes_produtos:
            if termo not in nome.lower():
                continue
            encontrou = True
            print(f"- {nome}")

        # Também pesquisa as peças que já existem no banco.json
        for peca in dados.get("pecas", []):
            nome_peca = str(peca.get("peca", ""))
            if termo not in nome_peca.lower():
                continue
            encontrou = True
            print(f"- {nome_peca}")

        if not encontrou:
            print("Nenhum item encontrado.")

    elif opcao_menu == 5:
        print("\n-- Relatório de Vendas --")
        if len(historico_vendas) == 0:
            print("Nenhuma venda registrada.")
        else:
            for venda in historico_vendas:
                print(venda)
            print(f"Faturamento Total Acumulado: R${faturamento_total:.2f}")

    elif opcao_menu == 6:
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")