import os.path

PATH = 'YOUR\\PATH\\TO\\HERE\\PasswordGenerator\\db\\passwords.txt'

def filefunc(escrever=False, ler=False):

    """Funcionalidades gerais para o arquivo passwords.txt

    Returns:
        Leitura dos Sites e Passwords OR Se foi escrito com sucesso no arquivo
    """
    # Criação do Arquivo se não estiver criado
    try:
        passwords_file = open(PATH, 'r+')
        passwords_file.close()
    except FileNotFoundError:
        passwords_file = open(PATH, 'w+')
        passwords_file.close()

    # Lê o arquivo
    if ler: 
        passwords_file = open(PATH, 'r')    
        lista_def = passwords_file.readlines()

        # Remove site:  //   password:  //   \n
        lista_def = [frase.replace('site: ', '') for frase in lista_def]
        lista_def = [frase.replace('password: ', '') for frase in lista_def]
        lista_def = [frase.replace('\n', '') for frase in lista_def]

        # lista_total recebe frase para cada frase contida em lista_def
        lista_total = [[frase] for frase in lista_def]
        passwords_file.close()
        
        for i in lista_total:
            print(i)
    # Escreve no arquivo
    if escrever:
        # Abrir o arquivo no modo de "acrescento"
        passwords_file = open(PATH, 'a+')
        
        site = str(input('Digite o -> nome do site <- para cadastrar sua password: ')).strip()
        password = str(input('Digite a sua -> password <- : ')).strip()
        
        # Tenta escrever, Senão imprime um erro
        try:
            passwords_file.write(f'site: {site} password: {password}\n')
            passwords_file.close()
            print('CADASTRADO COM SUCESSO!')
        except:
            print('OCORREU UM ERRO NO SEU CADASTRO, TENTE NOVAMENTE!')
        

print(filefunc(escrever=True, ler=True))
