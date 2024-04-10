import streamlit as st
import pandas as pd
import psycopg2 as psy

# Função para executar consulta SQL
def execute_query(query):
    # Conectar ao banco de dados
    conn = psy.connect(
        dbname="pmtomeacu_backup",
        user="postgres",
        password="161213",
        host="localhost"
    )

    # Criar um cursor
    cur = conn.cursor()

    # Executar a consulta SQL fornecida
    cur.execute(query)

    # Recuperar os nomes das colunas
    columns = [desc[0] for desc in cur.description]

    # Recuperar os resultados da consulta
    rows = cur.fetchall()

    # Fechar o cursor e a conexão
    cur.close()
    conn.close()

    return columns, rows

# Título da página
st.title('Consulta SQL')

# Entrada de texto para a consulta SQL
query = st.text_area('Insira sua consulta SQL aqui')

# Botão para executar a consulta
if st.button('Executar'):
    # Verificar se a consulta não está vazia
    if query.strip() != '':
        try:
            # Executar a consulta e obter os resultados
            columns, result = execute_query(query)
            
            # Exibir os resultados em uma tabela
            if len(result) > 0:
                st.write('Resultado:')
                df = pd.DataFrame(result, columns=columns)
                st.dataframe(df)
            else:
                st.write('Nenhum resultado encontrado.')
        except Exception as e:
            st.error(f'Ocorreu um erro ao executar a consulta: {str(e)}')
    else:
        st.warning('Por favor, insira uma consulta SQL válida.')
