def tela_introducao():
    mensagem = '''
        Leitor de NFe.xml

        Este programa lê uma pasta buscando arquivos.xml no padrão das NFe's 
        e gera um arquivo.xlsx contendo todas as informações da Nota e dos Produtos
        dentro dela, de acordo com lógica e parâmetros previamente definidos.
        
        Selecione alguma opção apertando seu número correspondente:

        [1] - Escolher nome do Arquivo.
        [2] - Informar caminho da Base de Dados.
        [0] - Sair.
'''
    print(mensagem)
    comando = input('Comando: ')
    
    return comando