import pandas as pd
from analytics.queries_sqlite3 import load_raw_data, create_view_cleaned_data

datasets = [
    "customers", 
    "order_payments", 
    "orders"
]

if __name__ == "__main__":
    # Carrega cada arquivo CSV e substitui a tabela correspondente no banco SQLite.
    for dataset_name in datasets:
        df = pd.read_csv(f"data/olist_{dataset_name}_dataset.csv")
        load_raw_data(data = df, name = dataset_name)
    
    # Cria a view usada pela análise para considerar pedidos entregues no período definido.
    create_view_cleaned_data()
