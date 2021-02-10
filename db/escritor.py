import os.path

PATH = 'C:\\Users\\luisg\\OneDrive\\Ambiente de Trabalho\\PasswordGenerator\\db\\passwords.txt'

def filefunc(site, passe, escrever=False, ler=True):
    """Funcionalidades do arquivo FileFunc

    Args:
        *args(string) -> Isto é o que será escrito: Site   --   Password
        escrever (bool, optional): Se irá ser escrito ou não. Defaults to False.
        ler (bool, optional): Se irá ser lido ou não. Defaults to True.
    """
   
    # Criação do Arquivo se não estiver criado
    try:
        passwords_file = open(PATH, 'r+')
    except FileNotFoundError:
        passwords_file = open(PATH, 'w+')

    # Lê o arquivo
    if ler:
        lista_def = passwords_file.readlines()

    # Remove site:  //   password:  //   \n
    lista_def = [frase.replace('site:', '') for frase in lista_def]
    lista_def = [frase.replace('password: ', '') for frase in lista_def]
    lista_def = [frase.replace('\n', '') for frase in lista_def]

    # lista_total recebe frase para cada frase contida em lista_def
    lista_total = [[frase] for frase in lista_def]
    return lista_total

            
print(filefunc('Paypal', '0saAmGsainwl21ewla', escrever=True, ler=True))