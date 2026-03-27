# 🏭 Sistema de Gestão - Py Indústrias

Sistema de gerenciamento de produtos, produção e vendas em Python com interface de linha de comando (CLI).

O projeto utiliza persistência em JSON para manter os dados entre execuções.

## 🚀 Funcionalidades Atuais

O sistema já é capaz de realizar as seguintes operações:

- **Cadastrar Produto**: Registra nome, custo de produção, preço de venda e estoque inicial 0.
- **ID automático**: Ao cadastrar produto novo, o ID é calculado a partir do maior ID existente no banco (ex.: se vai até 100, o próximo é 101).
- **Registrar Produção (Entrada)**: Aumenta o estoque de um produto existente.
- **Registrar Venda (Saída)**: Deduz do estoque, calcula faturamento e registra no histórico.
- **Busca por nome (parcial e sem diferenciar maiúsculas/minúsculas)**: Pesquisa tanto em produtos cadastrados quanto em pecas do banco.
- **Integração com pecas**: Se uma peça for usada em entrada/saída e ainda não estiver em produtos, ela é adicionada automaticamente para movimentação de estoque.
- **Relatório de Vendas**: Exibe histórico de transações e faturamento acumulado.
- **Encerramento amigável**: Se o usuário pressionar `Ctrl + C` no menu, o sistema finaliza sem traceback.

## 💾 Persistência de Dados (JSON)

Os dados são lidos e gravados no arquivo `banco.json`:

- `pecas`: base inicial de peças.
- `produtos`: produtos gerenciados no sistema (incluindo os cadastrados e os importados de peças quando necessário).
- `historico_vendas`: histórico textual de vendas.

Toda alteração relevante (cadastro, entrada e saída) é salva automaticamente.

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3
- **Persistência**: JSON (`banco.json`)
- **Estruturas de Dados**: Listas (arrays), loops (`for`, `while`) e estruturas de decisão (`if/else`).


## 📦 Como Executar

1. Certifique-se de ter o Python instalado.
2. Execute o arquivo principal no terminal:

```bash
python Projeto1EtapaPython.py
```

## 📁 Arquivos Principais

- `Projeto1EtapaPython.py`: aplicação principal (menu, regras e persistência).
- `banco.json`: base de dados JSON.

---
*Desenvolvido como parte do projeto da 1ª Etapa de Python.*
