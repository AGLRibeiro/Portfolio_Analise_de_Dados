# Portfólio de Análise de Dados

<img src="Imagens/Banner_Adilson.jpeg">
Olá! Meu nome é Adilson Gabriel de Lacerda Ribeiro e sou bacharel em Física pela Universidade Federal do Paraná. Tenho experiência em exploração de dados e aplico conhecimentos de matemática, estatística e programação para transformar dados em informações relevantes, identificar padrões e tendências e apoiar a tomada de decisões. Tenho interesse em atuar nas áreas de Análise de Dados e Ciência de Dados.

# Projeto: Diagnóstico financeiro da Olist
## Resumo

**Descrição:** Projeto de análise de dados com Python e SQL, desenvolvido a partir de dados da Olist, uma empresa brasileira de comércio eletrônico. O trabalho inclui exploração e preparação dos dados e um diagnóstico dos mecanismos de crescimento do faturamento.

**Objetivo:** Analisar dados de pedidos, pagamentos e clientes referentes ao período de 2016 a 2018 para investigar a evolução do faturamento e responder a questões relevantes para o negócio.

**Problema de negócio:** A análise exploratória identificou uma tendência de crescimento das vendas. Para avaliar se esse crescimento é saudável, o projeto considera que o faturamento deve ter recorrência e não depender excessivamente de poucos clientes. A análise investiga duas questões:

- O crescimento do faturamento é impulsionado pela conquista de novos clientes, pelo aumento da frequência de compra ou pelo aumento do valor das vendas?
- Como o faturamento se distribui entre os clientes? Há concentração relevante?

**Principais resultados:**
- A receita aumentou devido ao crescimento do número de vendas. O ticket médio permaneceu praticamente estável (+1,53%), enquanto o volume de vendas cresceu 140,19% no mesmo período.
- O número de vendas aumentou em decorrência do crescimento de 147,17% na base de clientes, e não do aumento da frequência de compra, que permaneceu praticamente estável, apresentando uma variação negativa de 0,45%.
- A receita não depende de um único cliente; o maior faturamento individual é de R$ 13.664,08. Ainda assim, há concentração em uma parcela da base de consumidores: 29,28% dos clientes representam 63,9% da receita.

**Recomendações:** 
- Embora a receita não esteja concentrada em um único cliente, uma parcela de aproximadamente 29,28% da base é responsável por 63,9% do faturamento. Isso evidencia a importância desse grupo para os resultados da empresa. Recomenda-se desenvolver estratégias de retenção e fidelização, com programas de fidelidade, benefícios exclusivos e ações de relacionamento, para reduzir o risco de perda de receita. Também se recomenda implementar campanhas de upsell e cross-sell para aumentar o ticket médio dos demais clientes e estimular uma distribuição mais equilibrada do faturamento.

- Criar programas de fidelidade, desenvolver campanhas de recompra, identificar clientes inativos e elaborar campanhas personalizadas com base no histórico de compras, buscando aumentar a frequência de compra dos clientes atuais. A empresa conseguiu conquistar novos clientes, mas ainda não demonstrou crescimento significativo na recorrência de compra.

# O que você encontrará aqui?
A análise foi desenvolvida em Python, utilizando principalmente as bibliotecas pandas para manipulação dos dados e SQLite para consultas e integração das tabelas.

Inicialmente, foi realizada uma exploração dos dados para avaliar sua estrutura, qualidade e consistência. Em seguida, foram aplicados filtros temporais e critérios de seleção dos pedidos, considerando apenas aqueles entregues no período analisado.

Com os dados preparados, foram construídos indicadores de desempenho, como faturamento, volume de vendas, ticket médio, aquisição de clientes, frequência de compra e concentração de receita. Por fim, foram elaborados gráficos para facilitar a visualização dos resultados, identificar tendências e apoiar a interpretação dos indicadores.
- **Preparação e análise exploratória:** inspeção das tabelas, avaliação de valores ausentes e análise da qualidade e do recorte temporal dos registros.
- **SQL com SQLite:** consultas com `SELECT`, `WHERE`, `INNER JOIN`, `GROUP BY` e `ORDER BY`, além das funções de agregação `SUM` e `COUNT(DISTINCT ...)` e da função de data `strftime`.
- **Views:** criação da view `orders_cleaned` com `CREATE VIEW`, após remover uma versão anterior com `DROP VIEW IF EXISTS`. A view restringe a análise a pedidos entregues no intervalo temporal selecionado.
- **Integração entre Python e SQL:** utilização da biblioteca pandas para importar arquivos CSV para tabelas SQLite, executar consultas SQL parametrizadas e carregar os resultados em DataFrames.
- **Manipulação e filtragem de dados:** utilização da biblioteca pandas para selecionar, transformar e filtrar registros, frequentemente por meio de indexação booleana (Boolean Indexing).
- **Análise de negócio:** avaliação do faturamento, do volume de vendas, do ticket médio, da quantidade e frequência de compra dos clientes e da concentração de receita.
- **Visualização e interpretação:** elaboração de gráficos estáticos com Matplotlib e gráficos interativos com Plotly, além da construção de indicadores para identificar tendências, interpretar resultados e comunicar as principais conclusões e recomendações da análise.

## Dados
**Critérios de seleção das tabelas**

O dataset da Olist disponibiliza diversas tabelas com informações sobre pedidos, clientes, vendedores, produtos, pagamentos, avaliações e logística. Inicialmente, analisei a estrutura do dataset e identifiquei quais tabelas continham as informações necessárias para responder às perguntas analíticas propostas. Para este projeto, foram selecionadas três tabelas com base na sua relevância para os objetivos analíticos estabelecidos.

A seleção considerou os seguintes critérios:
- Relevância para o negócio: utilização de dados diretamente relacionados às perguntas que orientaram a análise.
- Necessidade analítica: priorização das informações indispensáveis para a construção dos indicadores e métricas.
- Eficiência do modelo: redução de relacionamentos e complexidade desnecessários, mantendo a consistência das análises.
- Foco nos resultados: concentração nos dados que efetivamente contribuíam para a geração de insights. 
As demais tabelas não foram utilizadas porque estavam fora do escopo definido ou não agregavam informações necessárias aos objetivos desta análise. Essa decisão foi uma escolha metodológica para manter o projeto direcionado, consistente e alinhado às perguntas de negócio propostas.

O projeto utiliza três arquivos CSV com dados de clientes, pedidos e pagamentos, além de um banco SQLite. Os arquivos estão armazenados em [`data/`](data/):

| Arquivo | Conteúdo |
|---|---|
| [`olist_customers_dataset.csv`](data/olist_customers_dataset.csv) | Identificadores dos clientes e informações de localização. |
| [`olist_orders_dataset.csv`](data/olist_orders_dataset.csv) | Identificadores, status e datas dos pedidos. |
| [`olist_order_payments_dataset.csv`](data/olist_order_payments_dataset.csv) | Registros de pagamentos associados aos pedidos. |
| [`olist.db`](data/olist.db) | Banco SQLite com as tabelas `customers`, `orders` e `order_payments`, além da view `orders_cleaned`. |

### Dados de clientes

Este conjunto reúne identificadores e informações de localização dos clientes. A relação com a tabela de pedidos é feita por `customer_id`, que identifica o registro do cliente associado a um pedido. Um consumidor que faz pedidos diferentes pode ter um `customer_id` distinto em cada pedido. Já `customer_unique_id` permite reconhecer o mesmo consumidor entre pedidos diferentes.

| Campo | Descrição |
|---|---|
| `customer_id` | Identificador do registro do cliente relacionado ao pedido. |
| `customer_unique_id` | Identificador que permite reconhecer um cliente em diferentes pedidos. |
| `customer_zip_code_prefix` | Prefixo de cinco dígitos do CEP informado para o cliente. |
| `customer_city` | Cidade do cliente. |
| `customer_state` | Estado do cliente. |

### Dados de pagamentos

Cada registro descreve uma parcela ou transação de pagamento associada a um pedido. Um pedido pode ter mais de um registro quando o pagamento é dividido entre diferentes métodos ou transações.

| Campo | Descrição |
|---|---|
| `order_id` | Identificador do pedido relacionado ao pagamento. |
| `payment_sequential` | Número sequencial do registro de pagamento dentro do pedido. |
| `payment_type` | Método de pagamento utilizado. |
| `payment_installments` | Número de parcelas informado para o pagamento. |
| `payment_value` | Valor registrado para a transação de pagamento. |

### Dados de pedidos

Esta tabela reúne os pedidos e suas principais datas, conectando cada compra ao cliente correspondente. Os registros de data e hora permitem acompanhar etapas que vão da realização da compra à entrega.

| Campo | Descrição |
|---|---|
| `order_id` | Identificador único do pedido. |
| `customer_id` | Identificador do registro do cliente associado ao pedido. |
| `order_status` | Situação do pedido, como entregue ou enviado. |
| `order_purchase_timestamp` | Data e hora em que o pedido foi realizado. |
| `order_approved_at` | Data e hora da aprovação do pagamento. |
| `order_delivered_carrier_date` | Data e hora em que o pedido foi encaminhado ao parceiro logístico. |
| `order_delivered_customer_date` | Data e hora da entrega efetiva ao cliente. |
| `order_estimated_delivery_date` | Data estimada de entrega informada ao cliente no momento da compra. |

**Fonte dos dados:** [Brazilian E-Commerce Public Dataset by Olist — Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

## Etapas da análise

1. **Carga dos dados:** [`main.py`](main.py) lê os três arquivos CSV e grava as tabelas no banco SQLite por meio das funções de [`analytics/queries_sqlite3.py`](analytics/queries_sqlite3.py).
2. **Exploração e preparação:** [`analytics/raw_exploratory_analysis.ipynb`](analytics/raw_exploratory_analysis.ipynb) examina as tabelas, os valores ausentes, os status dos pedidos e a estabilidade dos registros ao longo do tempo.
3. **Seleção dos pedidos:** a função `create_view_cleaned_data()` cria a view `orders_cleaned`, considerando os pedidos entregues com data de compra a partir de 1º de dezembro de 2016 e anterior a 26 de agosto de 2018.
4. **Análise financeira:** [`analytics/analysis.ipynb`](analytics/analysis.ipynb) compara os seguintes indicadores:
   - **Ticket médio:** permite avaliar se os clientes passaram a gastar mais em cada compra, indicando um aumento no valor médio das vendas.
   - **Quantidade de vendas:** permite verificar se houve um aumento no volume de transações, indicando maior atividade comercial. 
   - **Quantidade de clientes:** permite avaliar a evolução da base de clientes, indicando se o crescimento do volume de vendas está associado à conquista de novos consumidores.
   - **Frequência de compra dos clientes:** permite identificar quantas vezes, em média, cada cliente realizou compras em determinado período, indicando se os clientes existentes passaram a comprar com maior frequência.
   - **Faturamento por cliente:** permite identificar quanto cada cliente contribui para a receita total, evidenciando diferenças na participação individual dos consumidores no faturamento.
   - **Concentração da receita por número de clientes:** permite avaliar qual parcela do faturamento está concentrada em diferentes proporções da base de clientes, identificando o grau de dependência em relação aos maiores consumidores.

   Essas métricas foram selecionadas porque a análise conjunta desses indicadores permite identificar os fatores associados ao crescimento do faturamento e compreender como a receita está distribuída entre os clientes. Além disso, os resultados contribuem para identificar oportunidades de melhoria e orientar decisões estratégicas relacionadas ao comportamento dos consumidores.
5. **Visualizações:** os notebooks apresentam gráficos temporais, gráficos de distribuição e indicadores resumidos para facilitar a interpretação dos resultados.

## Principais resultados

### Evolução do faturamento
![Evolução do faturamento da Olist](Imagens/Evolução_do_faturamento_olist.png)

O faturamento passou de **R$ 3,46 milhões em 2017 para R$ 8,44 milhões em 2018**, considerando o período comparável, representando um crescimento de **143,87%**. No mesmo intervalo, o número de vendas aumentou **140,19%**, enquanto o ticket médio apresentou uma variação de apenas **1,53%**.

![Evolução de clientes e faturamento da Olist](Imagens/Evolução_de_clientes_e_faturamento_Olist.png)

A evolução do faturamento foi acompanhada pela expansão da base de clientes, que passou de aproximadamente **22,6 mil para 50,8 mil**, um crescimento de **147,17%**. Entretanto, a frequência média de compra apresentou uma leve retração de **0,45%**.

### Distribuição do faturamento por cliente

![Distribuição do faturamento por cliente](Imagens/Distribuição_do_faturamento_por_cliente.png)

O maior faturamento individual por cliente foi de **R$ 13.664,08**. A análise também revelou uma concentração de receita: aproximadamente **29,28% dos clientes** foram responsáveis por **63,9% do faturamento**, equivalente a **R$ 9,81 milhões**.


## Como executar

1. Baixe do Kaggle os três arquivos CSV listados na tabela acima e coloque-os na pasta `data/`.
2. Instale as dependências listadas em [`requirements.txt`](requirements.txt).
3. Para recriar as tabelas e a view a partir dos CSVs, execute na raiz do projeto:

   ```bash
   python main.py
   ```

4. Abra os notebooks em `analytics/`. Para que o import `queries_sqlite3` seja resolvido como no projeto, configure `analytics/` como diretório de trabalho do kernel.

## Considerações e limitações

**Conclusão:** De acordo com o critério adotado, o faturamento cresceu principalmente junto com a expansão da base de clientes, sem aumento relevante da frequência de compra. A receita não depende de um único consumidor, mas uma parcela expressiva do faturamento está concentrada em parte da base, o que torna importantes as ações de retenção e fidelização.

**Limitações:** Para realizar uma análise mais completa da sustentabilidade do crescimento, seria necessário avaliar a retenção de clientes, a recorrência da receita, a evolução das margens e a concentração das vendas por vendedor ou região. Essas análises, no entanto, não foram contempladas neste trabalho, que se limita a apresentar um diagnóstico geral dos mecanismos de crescimento da receita. Além disso, os dados de 2018 estão incompletos devido ao truncamento da série histórica ao final do período. Portanto, as comparações devem considerar esse recorte, uma vez que os resultados não representam um ano completo.

## Em desenvolvimento
**Power BI:** em processo de aprendizado e desenvolvimento de habilidades em análise e visualização de dados.