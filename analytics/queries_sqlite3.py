import sqlite3 as sql
import pandas as pd
from pathlib import Path
import datetime

# Define a raiz do projeto de forma dinâmica baseada na localização do script atual.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Configura o caminho absoluto do banco de dados SQLite garantindo portabilidade entre ambientes.
db_path = PROJECT_ROOT / "data" / "olist.db"

# Delimita o intervalo temporal padrão utilizado como filtro nas análises exploratórias.
min_date = datetime.date(2016, 9, 3)
max_date = datetime.date(2018, 11, 12)

def load_raw_data(data: pd.DataFrame, name: str, map_type: str = None) -> None:
    """
    Grava um DataFrame em uma tabela do banco de dados SQLite.

    Args:
        data (pd.DataFrame): DataFrame contendo os dados a serem persistidos.
        name (str): Nome da tabela de destino no banco de dados.
        map_type (str, optional): Mapeamento opcional de tipos de dados SQL para as colunas.
    """
    # Estabelece conexão com o banco de dados SQLite alvo.
    conn = sql.connect(db_path)

    # Persiste o DataFrame como tabela relacional, aplicando mapeamento de tipos customizado se fornecido.
    if map_type == None:
        data.to_sql(name, conn, if_exists='replace', index=False)
    else:
        data.to_sql(name, conn, if_exists='replace', index=False, dtype=map_type)

    # Encerra a conexão para liberar recursos de E/S do banco de dados.
    conn.close()

def read_data(name: str) -> pd.DataFrame:
    """
    Lê uma tabela completa do banco de dados e retorna um DataFrame.

    Args:
        name (str): Nome da tabela a ser consultada.

    Returns:
        pd.DataFrame: DataFrame contendo todos os registros da tabela.
    """
    # Estabelece conexão com o banco de dados SQLite.
    conn = sql.connect(db_path)

    # Executa consulta para carregar a tabela inteira em memória na forma de DataFrame pandas.
    df = pd.read_sql_query(f"SELECT * FROM {name}", conn)

    # Encerra a conexão com o banco de dados.
    conn.close()

    return df

def create_view_cleaned_data() -> None:
    """
    Criar uma view de pedidos entregues, considerando os critérios estabelecidos na análise 
    exploratória, para realizar a análise de receita. 
    """
    # Estabelece conexão com o banco de dados SQLite.
    conn = sql.connect(db_path)

    # Remove a view pré-existente para garantir idempotência na criação.
    conn.execute("""
        DROP VIEW IF EXISTS orders_cleaned;
    """)

    # Cria a view filtrando apenas pedidos com status de entrega concluído dentro da janela temporal de interesse.
    conn.execute("""
        CREATE VIEW orders_cleaned AS
        SELECT * FROM orders
        WHERE order_purchase_timestamp >= '2016-12-01' AND order_purchase_timestamp < '2018-08-26'
            AND order_status == 'delivered'
    """)  # Esses critérios foram estabelecidos durante a análise exploratória.

    # Encerra a conexão com o banco de dados.
    conn.close()


def get_sales_data(
        start: datetime.date = min_date, 
        end: datetime.date = max_date, 
        step: str = "%Y-%m-%d"
    ) -> pd.DataFrame:
    """
    Calcula o faturamento em um período específico, considerando a soma dos
    valores dos pagamentos das compras aprovadas no intervalo informado.

    Permite agrupar os resultados por dia, mês ou ano, de acordo com o formato
    de data definido no parâmetro 'step'.

    Args:
        start (datetime.date): Data inicial do período.
        end (datetime.date): Data final do período, não incluída no intervalo.
        step (str): Formato de agrupamento das datas. Pode ser '%Y-%m-%d'
                    para agrupar por dia, '%Y-%m' para mês ou '%Y' para ano.

    Returns:
        pd.DataFrame: DataFrame contendo o período, o faturamento total (revenue) e a quantidade
                      de pagamentos (sales_count) em cada intervalo de tempo.
                      Caso não existam resultados, retorna um DataFrame
                      com faturamento e quantidade de pagamentos iguais a zero.
    """
    # Estabelece conexão com o banco de dados SQLite.
    conn = sql.connect(db_path)

    # Executa consulta SQL agregando métricas de receita e contagem de vendas por intervalo temporal formatado.
    query = """
        SELECT
            strftime(?, o.order_approved_at) AS date, 
            SUM(p.payment_value) AS revenue,
            COUNT(DISTINCT p.order_id) AS sales_count
        FROM order_payments p
        INNER JOIN orders_cleaned o ON p.order_id = o.order_id
        WHERE o.order_approved_at >= ? AND o.order_approved_at <?
        Group BY strftime(?, o.order_approved_at)
        ORDER BY date;
    """
    df = pd.read_sql_query(query, conn, params=(step, start, end, step))  # Executa a query injetando parâmetros de segurança para evitar SQL Injection.
    conn.close()   # Encerra a conexão com o banco de dados.

    if df.empty:
        # Retorna um DataFrame estruturado com valores zerados caso o conjunto de resultados venha vazio.
        df = pd.DataFrame([{"date": None, "revenue": 0, "sales_count": 0}])
    else:
        # Trata valores nulos substituindo-os por zero e padronizando os tipos de dados.
        df["revenue"] = df["revenue"].fillna(0).astype(float)
        df["sales_count"] = df["sales_count"].fillna(0).astype(int)

    return df # Retorna o DataFrame agregado com as métricas calculadas por período.

def get_clients_data(
        start: datetime.date = min_date, 
        end: datetime.date = max_date,
    ) -> pd.DataFrame:
    """
    Retorna as datas de aprovação e os identificadores únicos dos clientes.

    Args:
        start (datetime.date): Data inicial do período.
        end (datetime.date): Data final do período, não incluída no intervalo.

    Returns:
        pd.DataFrame: DataFrame contendo a data de aprovação e o identificador único do cliente.
    """
    # Estabelece conexão com o banco de dados SQLite.
    conn = sql.connect(db_path)

    # Realiza junção entre pedidos e dados cadastrais para mapear clientes únicos por data de aprovação do pedido.
    query = """
        SELECT 
            o.order_approved_at AS date,
            c.customer_unique_id as customer_id
        FROM orders_cleaned o
        INNER JOIN customers c ON o.customer_id = c.customer_id
        WHERE o.order_approved_at >= ? AND o.order_approved_at < ?
        ORDER BY date;
    """
    df = pd.read_sql_query(query, conn, params=(start, end))  # Executa a consulta parametrizada.
    conn.close()   # Encerra a conexão com o banco de dados.
    
    if df.empty:
        # Retorna estrutura padrão com valores nulos caso a consulta não retorne registros.
        df = pd.DataFrame([{"date": None, "customer_id": None}])
    
    return df # Retorna o mapeamento temporal de clientes únicos.

def get_sales_by_clients_data(
        start: datetime.date = min_date, 
        end: datetime.date = max_date,
    ) -> pd.DataFrame:
    """
    Retorna o faturamento agregado por cliente único no período informado.

    Args:
        start (datetime.date): Data inicial do período.
        end (datetime.date): Data final do período, não incluída no intervalo.

    Returns:
        pd.DataFrame: DataFrame contendo o identificador do cliente e o faturamento total correspondente.
    """
    # Estabelece conexão com o banco de dados SQLite.
    conn = sql.connect(db_path)

    # Agrega o valor total de pagamentos agrupados por identificador único de cliente.
    query = """
        SELECT
            c.customer_unique_id AS customer_id,
            SUM(p.payment_value) As revenue
        FROM order_payments p
        INNER JOIN orders_cleaned o ON o.order_id = p.order_id
        INNER JOIN customers c ON o.customer_id = c.customer_id
        WHERE o.order_approved_at >= ? AND o.order_approved_at < ?
        Group By c.customer_unique_id;
    """
    df = pd.read_sql_query(query, conn, params=(start, end))  # Executa a consulta agregada com parâmetros seguros.
    conn.close()   # Encerra a conexão com o banco de dados.
    
    if df.empty:
        # Retorna estrutura vazia tratada com valores padrão caso não haja dados no intervalo.
        df = pd.DataFrame([{"customer_id": None, "revenue": 0}])
    else:
        # Trata valores ausentes em identificadores e garante conversão numérica da receita.
        df["customer_id"] = df["customer_id"].fillna('0')
        df["revenue"] = df["revenue"].fillna(0).astype(float)
    
    return df # Retorna o DataFrame com o faturamento agrupado por cliente.