from src.main.constructors.processo_introducao import processo_introducao

def start() -> None:
    while True:
        comando = processo_introducao()

        if comando == '1': print('Comando 1 foi acionado!')
        elif comando == '2': print('Comando 2 foi acionado!')
        elif comando == '0': exit()
        else: print('Comando não encontrado...\n\n')