import sqlite3
from datetime import datetime

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

def salvar_livro_banco(titulo, autor, editora, ano_publicacao, disponivel):
    cursor.execute('''
    INSERT INTO Livros (titulo, autor, editora, ano_publicacao, disponivel)
    VALUES (?, ?, ?, ?, ?)
    ''', (titulo, autor, editora, ano_publicacao, disponivel))
    conn.commit()

def salvar_usuario_banco(nome, email, telefone, celular):
    cursor.execute('''
    INSERT INTO Usuarios (nome, email, telefone, celular) VALUES (?, ?, ?, ?)
''', (nome, email, telefone, celular))
    conn.commit()

def salvar_emprestimos_banco(id_usuario, id_livro):
    # É necessário verificar se o livro está disponível
    cursor.execute("SELECT disponivel FROM Livros WHERE id = ?", (id_livro))
    livro = cursor.fetchone()
    if livro and livro[0] == 1:
        # Empréstimo pode ser concluído
        data_emprestimo = datetime.now().strftime("%d/%m/%Y")
        cursor.execute('''
        INSERT INTO Emprestimos (id_usuario, id_livro, data_emprestimo) VALUES (?, ?, ?)
    ''', (id_usuario, id_livro, data_emprestimo))
        # Atualizar o livro para não disponível
        cursor.execute('''
        UPDATE Livros SET disponivel = 0 WHERE id = ?
    ''', (id_livro))
        conn.commit()
        print('Emprétimo realizado com sucesso!')
    else:
        print('Livro não disponível para empréstimo!')

def salvar_devolucao_banco(id_usuario, id_livro):
    # Atualizando o empréstimo para devolução
    data_devolucao = datetime.now().strftime("%d/%m/%Y")
    cursor.execute('''
    UPDATE Emprestimos SET data_devolucao = ? WHERE id_usuario = ? AND id_livro = ? AND data_devolucao IS NULL
''', (data_devolucao, id_usuario, id_livro))
    # Agora atualizo o livro para disponível
    cursor.execute('''
    UPDATE Livros SET disponivel = 1 WHERE id = ?
''', (id_livro))
    conn.commit()

def listar_livros_disponiveis():
    cursor.execute("SELECT id, titulo, autor FROM Livros WHERE disponivel = 1")
    livros = cursor.fetchall()
    if livros:
        print('============ L I V R O S  D I S P O N Í V E I S ============')
        print()
        for livro in livros:
            print(f'ID: {livro[0]} Título: {livro[1]} Autor: {livro[2]}')
    else:
        print('Não há livros disponíveis no momento!')

def buscar_livro_por_titulo(titulo):
    cursor.execute("SELECT id, titulo, autor FROM Livros WHERE titulo LIKE ?", ('%' + titulo + '%',))
    livros = cursor.fetchall()
    if livros:
        print('============ L I V R O S  E N C O N T R A D O S ============')
        print()
        for livro in livros:
            print(f'ID: {livro[0]} Título: {livro[1]} Autor: {livro[2]}')
    else:
        print(f'Nenhum livro encontrado com o título {titulo}')

def buscar_livro_por_autor(autor):
    cursor.execute("SELECT id, titulo, autor FROM Livros WHERE autor Like ?", ('%' + autor + '%',))
    livros = cursor.fetchall()
    if livros:
        print('============ L I V R O S  E N C O N T R A D O S ============')
        print()
        for livro in livros:
            print(f'ID: {livro[0]} Título: {livro[1]} Autor: {livro[2]}')
    else:
        print(f'Nenhum livro encontrado com o autor {autor}')

def atualizar_livro(id_livro, novo_titulo=None, novo_autor=None, nova_editora=None, novo_ano_publicacao=None):
    # Primeiro preciso verificar se o livro existe
    cursor.execute("SELECT * FROM Livros WHERE id = ?", (id_livro))
    livro = cursor.fetchone()
    if livro:
        # Cria uma query dinâmica dependendo dos campos fornecidos para atualização
        update_fields = []
        update_values = []

        if novo_titulo:
            update_fields.append("titulo = ?")
            update_values.append(novo_titulo)

        if novo_autor:
            update_fields.append("autor = ?")
            update_values.append(novo_autor)

        if nova_editora:
            update_fields.append("editora = ?")
            update_values.append(nova_editora)

        if novo_ano_publicacao:
            update_fields.append("ano_publicacao = ?")
            update_values.append(novo_ano_publicacao)

        # Verifica se a campos para atualizar
        if update_fields:
            # Adiciona o ID do livro para atualizar especificamente o livro correto
            update_values.append(id_livro)
            query = f"UPDATE Livros SET {', '.join(update_fields)} WHERE id = ?"

            # Executa a atualização
            cursor.execute(query, tuple(update_values))
            conn.commit()
            print('Informações do livro atualizadas com sucesso!')
        else:
            print('Nenhuma informação foi fornecida para atualização!')
    else:
        print('Livro não localizado!')

def atualizar_usuario(id_usuario, novo_nome=None, novo_email=None, novo_telefone=None, novo_celular=None):
    cursor.execute("SELECT * FROM Usuarios WHERE id = ?", (id_usuario))
    usuario = cursor.fetchone()
    if usuario:
        update_fields = []
        update_values = []

        if novo_nome:
            update_fields.append("nome = ?")
            update_values.append(novo_nome)

        if novo_email:
            update_fields.append("email = ?")
            update_values.append(novo_email)

        if novo_telefone:
            update_fields.append("telefone = ?")
            update_values.append(novo_telefone)

        if novo_celular:
            update_fields.append("celular = ?")
            update_values.append(novo_celular)
        
        if update_fields:
            update_values.append(id_usuario)
            query = f"UPDATE Usuarios SET {', '.join(update_fields)} WHERE id = ?"
            cursor.execute(query, tuple(update_values))
            conn.commit()
            print('Informações do Usuário atualizadas com sucesso!')
        else:
            print('Nenhuma informação foi fornecida para atualização!')
    else:
        print('Usuário não localizado!')

def excluir_livro(id_livro):
    # Verifica se o livro existe
    cursor.execute("SELECT * FROM Livros WHERE id = ?", (id_livro))
    livro = cursor.fetchone()
    if livro:
        cursor.execute("DELETE FROM Livros WHERE id = ?", (id_livro))
        conn.commit()
        print(f'Livro com ID: {id_livro} excluído com sucesso!')
    else:
        print(f'Livro com ID: {id_livro} não localizado!')

def excluir_usuario(id_usuario):
    # Verifica se o usuário existe
    cursor.execute("SELECT * FROM Usuarios WHERE id = ?", (id_usuario))
    usuario = cursor.fetchone()
    if usuario:
        cursor.execute("DELETE FROM Usuarios WHERE id = ?", (id_usuario))
        conn.commit()
        print(f'Usuário com ID: {id_usuario} excluído com sucesso!')
    else:
        print(f'Usuário com ID: {id_usuario} não localizado!')

def inserir_livro(titulo, autor, editora, ano_publicacao, disponivel):
    salvar_livro_banco(titulo, autor, editora, ano_publicacao, disponivel)
    print('Livro salvo no banco com sucesso!')

def inserir_usuario(nome, email, telefone, celular):
    salvar_usuario_banco(nome, email, telefone, celular)
    print('Usuário salvo no banco com sucesso!')

def inserir_emprestimo(id_usuario, id_livro):
    salvar_emprestimos_banco(id_usuario, id_livro)

def registrar_devolucao(id_usuario, id_livro):
    salvar_devolucao_banco(id_usuario, id_livro)
    print('Devolução registrada com sucesso!')

def lista_livros_disponiveis():
    listar_livros_disponiveis()

def buscar_livro_titulo(titulo):
    buscar_livro_por_titulo(titulo)

def buscar_livro_autor(autor):
    buscar_livro_por_autor(autor)

def atualiza_livro(id_livro, novo_titulo, novo_autor, nova_editora, novo_ano_publicacao):
    atualizar_livro(id_livro, novo_titulo, novo_autor, nova_editora, novo_ano_publicacao)

def atualiza_usuario(id_usuario, novo_nome, novo_email, novo_telefone, novo_celular):
    atualizar_usuario(id_usuario, novo_nome, novo_email, novo_telefone, novo_celular)

def deletar_livro(id_livro):
    excluir_livro(id_livro)

def deletar_usuario(id_usuario):
    excluir_usuario(id_usuario)