#importando o conector do mysql

import mysql.connector

#input para decisao do que fazer

c = int(input('Oque deseja fazer 1 = criar \n 2 = ler \n 3 = atualizar \n 4 excluir \n qualquer outra tecla = desligar o programa\n '))

#acessando o banco de dados
if c == 1 or 2 or 3 or 4:
    def connect_db():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="061005Aa",
            database="mycruddb"
    )

# comando CREATE

if c == 1:
    def create_item(name, description):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("insert into items (name, description) VALUES (%s, %s)", (name, description))
        conn.commit()
        conn.close()

#Comando READ

if c == 2:
    def read_items():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("select * from items")
        result = cursor.fetchall()
        conn.close()
        return  result

#Comando UPDATE

if c == 3:
    def update_item(item_id, name, description):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("update items ser name  = %s, description = %s where id = %s", (name, description, item_id))
        conn.commit()
        conn.close()

#Comando DELETE

if c == 4:
    def delete_item(item_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("delete from items WHERE id = %s", (item_id))
        conn.commit()
        conn.close()

else:
    print('encerrando programa')
