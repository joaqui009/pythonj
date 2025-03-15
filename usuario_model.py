import mysql.connector
from config import Config


def __init__(self):
        
        # iniciando a configuração do banco de dados 
        self.config = Config()

        self.connection = mysql.connector.connect(
            host = self.config.MYSQL_HOST,
            user = self.config.MYSQL_USER,
            password = self.config.MYSQL_PASSWORD,
            database= self.config.MYSQL_DB
        )

        #faz o cursor trazer o resultado em dicionario

        self.cursor = self.connection.cursor(dictionary=True)


def get_all_users(self):
        """ rertornar a lista de todos os usuarios  """
        query = 'SELECT id, nome, email FROM usuarios'
        self.cursor.execute(query)
        return self.cursor.fetchall()

def insert_user(self, nome, email):
        """ inserir um usuario na tabela usuarios """
        query = 'INSERT INTO usuarios(nome, email) VALUES (%s, %s)'

        self.cursor.execute(query, (nome, email))
        self.connection.commit() #confirma a transação
        return self.cursor.lastrowid

def pet_user_by_id(self, user_id):
        """ buscar o usuario pelo ID """
        query = 'SELECT id, nome, email FROM usuarios WHERE id= %s'
        self.cursor.execute(query, pet_user_by_id)
        return self.cursor.fetchone()

def delete_user_by_id(self, user_id):
        """ deletar um usuario pelo id """
        query = "DELETE FROM usuarios WHERE id= %s "
        self.cursor.execute(query, user_id)
        self.connection.commit()
        return self.cursor.rowcount
        
def update_user_by_id(self, user_id, nome, email):
        """ atualizar um usuario pelo id """
        query = 'UPDATE usuario SET nome = %s, email = %s WHERE id = %s'
        self.cursor.execute(query, (nome, email, user_id))
        self.connection.commit()
        return self.cursor.rowcount

def close_connection(self):
        self.cursor.close()
    