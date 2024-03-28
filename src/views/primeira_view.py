def tela_introducao():
    mensagem = '''
        Leitor de NFe.xml

        Selecione alguma opção apertando seu número correspondente:

        [1] - Escolher nome do Arquivo
        [2] - Informar caminho da Base de Dados
        [0] - Sair 
'''
    print(mensagem)
    comando = input('Comando: ')
    
    return comando