import sqlite3

# Conectar ao banco (sqlite)
def conectar_db():
    conn = sqlite3.connect('biblioteca.db') # Cria ou abre o banco de dados
    return conn

# Função para criar tabelas no banco
def criar_tabelas():
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Livros (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   autor TEXT NOT NULL,
                   editora TEXT,
                   ano_publicacao INTEGER,
                   disponivel INTEGER DEFAULT 1 
                   )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL,
                   Telefone TEXT,
                   Celular TEXT
                   )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Emprestimos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   id_usuario INTEGER,
                   id_livro INTEGER,
                   data_emprestimo DATE,
                   data_devolucao DATE,
                   multa REAL DEFAULT 0.0,
                   FOREIGN KEY (id_usuario) REFERENCES Usuarios(id),
                   FOREIGN KEY (id_livro) REFERENCES Livros(id)
                   )
''')
    
    conn.commit()
    conn.close()

# Criar Tabelas no banco
if __name__ == "__main__":
    criar_tabelas()
