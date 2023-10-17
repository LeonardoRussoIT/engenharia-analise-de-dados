import pandas as pd
import mysql.connector

df = pd.read_csv('dados/final_vendas.csv')

conexao = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="vendas")

cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        id INT NOT NULL,
        produto VARCHAR(255),
        categoria VARCHAR(255),
        preco DOUBLE,
        frete DOUBLE,
        data_compra DATETIME,
        vendedor VARCHAR(255),
        local_compra VARCHAR(255),
        avaliacao INT,
        tipo_pagamento VARCHAR(255),
        parcelas INT
    )
""")

# Inserir os dados do DataFrame no banco de dados MySQL
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO vendas (id, produto, categoria, preco, frete, data_compra, vendedor, local_compra, avaliacao, tipo_pagamento, parcelas) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (row['id'], row['produto'], row['categoria'], row['preco'], row['frete'], row['data_compra'], row['vendedor'], row['local_compra'], row['avaliacao'], row['tipo_pagamento'], row['parcelas']))

conexao.commit()
conexao.close()
