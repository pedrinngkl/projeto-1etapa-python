#Variáveis iniciais
faturamento_total = 0
nomes_produtos = []
custos_producao = []
precos_venda = []
estoque_atual = []
historico_vendas = [] #Lista para armazenar registros de cada venda
opcao_menu = 0

#Loop principal (while)
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
    except ValueError:
        print("Erro: Digite um número inteiro!")
        continue # (continue) Volta para o início do loop

    #Estrutura de Decisão (if/elif/else)
    if opcao_menu == 1:
        print("\n-- Cadastro de Produto --")
        nome = input("Nome do veículo: ")
        
        # Validação com (while e break)
        while True:
            try:
                custo = float(input("Custo de produção: "))
                break # (break) Sai do loop de validação se der certo
            except ValueError:
                print("Valor inválido. Tente novamente.")
        
        while True:
            try:
                preco = float(input("Preço de venda: "))
                break
            except ValueError:
                print("Valor inválido.")

        nomes_produtos.append(nome)
        custos_producao.append(custo) 
        precos_venda.append(preco)
        estoque_atual.append(0) # Inicia com estoque 0
        print(f"Produto {nome} cadastrado com sucesso!")

    elif opcao_menu == 2:
        print("\n-- Registrar Produção --")
        busca_nome = input("Nome do produto para produzir: ")
        encontrado = False
        
        # Iteração (for) com enumerate para pegar índice
        for i, nome in enumerate(nomes_produtos):
            if nome == busca_nome:
                qtd = int(input(f"Quantidade a produzir de {nome}: "))
                estoque_atual[i] += qtd
                print(f"Novo estoque de {nome}: {estoque_atual[i]}")
                encontrado = True
                break # Encerra a busca pois já achou
        
        if not encontrado: # (else implícito da lógica)
            print("Produto não encontrado.")

    elif opcao_menu == 3:
        print("\n-- Registrar Venda --")
        busca_nome = input("Nome do produto vendido: ")
        
        for i in range(len(nomes_produtos)):
            if nomes_produtos[i] == busca_nome:
                qtd = int(input(f"Quantidade vendida de {busca_nome}: "))
                
                if estoque_atual[i] >= qtd:
                    estoque_atual[i] -= qtd
                    valor_venda = qtd * precos_venda[i]
                    faturamento_total += valor_venda
                    historico_vendas.append(f"Venda: {qtd}x {busca_nome} - Total: R${valor_venda:.2f}")
                    print(f"Venda registrada! Faturamento: +R${valor_venda:.2f}")
                else: 
                    print("Estoque insuficiente!")
                break
        else:
            # O 'else' num laço 'for' executa se o loop NÃO for interrompido por break
            print("Produto não encontrado para venda.")

    elif opcao_menu == 4:
        print("\n-- Buscar Produto --")
        termo = input("Digite parte do nome: ")
        print("Resultados:")
        
        # (for) simples
        for nome in nomes_produtos:
            if termo not in nome:
                continue # (continue) Pula para o próximo se não tiver o termo
            print(f"- {nome}")

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
        break # Encerra o loop principal

    else:
        print("Opção inválida! Tente novamente.")