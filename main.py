import sqlite3

conn = sqlite3.connect('biblioteca.db')

# Importa as funções do arquivo funcoes.py
from model import inserir_livro, inserir_usuario, inserir_emprestimo, registrar_devolucao, lista_livros_disponiveis
from model import buscar_livro_titulo, buscar_livro_autor, atualiza_livro, atualiza_usuario, excluir_livro, excluir_usuario

print()
print('========================= M E N U =========================')
def exibir_menu():
    print("Escolha uma opção:")
    print("1 - Inserir Livro")
    print("2 - Inserir Usuário")
    print("3 - Inserir Empréstimo")
    print("4 - Registrar Devolução")
    print("5 - Livros Disponiveís")
    print("6 - Buscar Livro Por Título")
    print("7 - Buscar Livro Por Autor")
    print("8 - Atualizar Um Livro")
    print("9 - Atualizar Um Usuário")
    print("10 - Excluir Um Livro")
    print("11 - Excluir Um Usuário")
    print("0 - Sair")

def main():
    while True:
        exibir_menu()
        print()
        print('===========================================================')
        print()
        escolha = input("Digite o número da opção desejada: ")
        print()

        if escolha == '1':
            print('============ I N S E R I R - U M - L I V R O ============')
            print()
            titulo = input('Digite o título do livro: ')
            autor = input('Digite o nome do autor: ')
            editora = input('Digite o noma da editora: ')
            ano_publicacao = int(input('Digite o ano da publicação ex: 1900: '))
            disponivel = int(input('Digite [0] False ou [1] True: '))
            inserir_livro(titulo, autor, editora, ano_publicacao, disponivel)
            print()
            print('========================= M E N U =========================')
        elif escolha == '2':
            print('========== I N S E R I R - U M - U S U Á R I O ============')
            print()
            nome = input("Digite o nome do usuário: ")
            email = input('Digite o email do usuário: ')
            telefone = input('Digite o telefone [ex: (00)0000-0000]: ')
            celular = input('Digite o celular [ex: (00)90000-0000]: ')
            inserir_usuario(nome, email, telefone, celular)
            print()
            print('========================= M E N U =========================')
        elif escolha == '3':
            print('========= I N S E R I R - U M - E M P R É S T I M O ========')
            print()
            id_usuario = input('Digite o id do usuário: ')
            id_livro = input('Digite o id do livro: ')
            inserir_emprestimo(id_usuario, id_livro)
            print()
            print('========================= M E N U =========================')
        elif escolha == '4':
            print('========= I N S E R I R - U M A - D E V O L U Ç Ã O ========')
            print()
            id_usuario = input('Digite o id do usuário: ')
            id_livro = input('Digite o id do livro: ')
            registrar_devolucao(id_usuario, id_livro)
            print()
            print('========================= M E N U =========================')
        elif escolha == '5':
            lista_livros_disponiveis()
            print()
            print('========================= M E N U =========================')
        elif escolha == '6':
            print('====== B U S C A R - L I V R O - P O R - T Í T U L O =======')
            print()
            titulo = input('Digite o título do livro a ser pesquisado: ')
            buscar_livro_titulo(titulo)
            print()
            print('========================= M E N U =========================')
        elif escolha == '7':
            print('====== B U S C A R - L I V R O - P O R - A U T O R =========')
            print()
            autor = input('Digite o autor do livro a ser pesquisado: ')
            buscar_livro_autor(autor)
            print()
            print('========================= M E N U =========================')
        elif escolha == '8':
            print('========== A T U A L I Z A R - U M - L I V R O =============')
            print()
            id_livro = input('Digite o ID do livro a ser atualizado: ')
            novo_titulo = input('Digite o novo título do livro: ')
            nova_editora = input('Digite o nome da nova Editora: ')
            novo_autor = input('Digite o nome do novo autor: ')
            novo_ano_publicacao = input('Digite o novo ano de publicação: ')
            atualiza_livro(id_livro, novo_titulo, novo_autor, nova_editora, novo_ano_publicacao)
            print()
            print('========================= M E N U =========================')
        elif escolha == '9':
            print('======== A T U A L I Z A R - U M - U S U Á R I O ==========')
            print()
            id_usuario = input('Digite o ID do usuário a ser atualizado: ')
            novo_nome = input('Digite o novo nome do usuário: ')
            novo_email = input('Digite o novo email do usuário: ')
            novo_telefone = input('Digite o novo telefone [ex: (00)0000-0000]: ')
            novo_celular = input('Digite o novo celular [ex: (00)90000-0000]: ')
            atualiza_usuario(id_usuario, novo_nome, novo_email, novo_telefone, novo_celular)
            print()
            print('========================= M E N U =========================')
        elif escolha == '10':
            print('============ E X C L U I R - U M - L I V R O ==============')
            print()
            id_livro = input('Digite o id do livro a ser excluído: ')
            excluir_livro(id_livro)
            print()
            print('========================= M E N U =========================')
        elif escolha == '11':
            print('========== E X C L U I R - U M - U S U Á R I O ============')
            print()
            id_usuario = input('Digite o id do usuário a ser excluído: ')
            excluir_usuario(id_usuario)
            print()
            print('========================= M E N U =========================')
        elif escolha == '0':
            print("Saindo do programa...")
            print()
            conn.close()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
