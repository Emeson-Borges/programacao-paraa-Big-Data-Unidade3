import psycopg2 as psy

# Conectar ao banco de dados
conn = psy.connect(
    dbname="pmtomeacu_backup",
    user="postgres",
    password="161213",
    host="localhost"
)

# Criar um cursor
cur = conn.cursor()

# Executar uma consulta SQL
cur.execute("SELECT * FROM esocial.s1010 limit 1")

# Recuperar os resultados da consulta
rows = cur.fetchall()

# Iterar sobre os resultados e exibi-los
for row in rows:
    print(row)

# Fechar o cursor e a conexão
cur.close()
conn.close()
