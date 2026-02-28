# 🏭 Sistema de Gestão - Py Indústrias

Este é um projeto inicial de um sistema de gerenciamento de produtos, produção e vendas, desenvolvido em Python. O objetivo é criar uma ferramenta de linha de comando (CLI) simples e eficiente para controle industrial.

## 🚀 Funcionalidades Atuais

O sistema já é capaz de realizar as seguintes operações em memória:

- **Cadastrar Produto**: Registra nome, custo de produção e preço de venda.
- **Registrar Produção (Entrada)**: Aumenta o estoque de um produto existente.
- **Registrar Venda (Saída)**: Deduz do estoque e calcula o faturamento, validando se há saldo suficiente.
- **Buscar Produto**: Pesquisa produtos por nome (busca parcial).
- **Relatório de Vendas**: Exibe o hitórico de transações e o faturamento total acumulado.

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3
- **Estruturas de Dados**: Listas (Arrays), Loops (`for`, `while`) e Estruturas de Decisão (`if/else`).

## 🔮 Roadmap (Melhorias Futuras)

Este projeto está em constante evolução. As próximas etapas de desenvolvimento incluem:

- [ ] **Refatoração do Código**: Migrar de múltiplas listas para Dicionários ou Classes (POO) para melhor organização.
- [ ] **Persistência de Dados**: Integração com Banco de Dados **MySQL** para salvar os registros permanentemente.

## 📦 Como Executar

1. Certifique-se de ter o Python instalado.
2. Execute o arquivo principal no terminal:

```bash
python Projeto1EtapaPython.py
```

---
*Desenvolvido como parte do projeto da 1ª Etapa de Python.*
