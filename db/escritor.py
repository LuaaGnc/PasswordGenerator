import os.path

PATH = 'C:\\Users\\luisg\\OneDrive\\Ambiente de Trabalho\\PasswordGenerator\\db\\passwords.txt'

def filefunc(site, passe, escrever=False, ler=True):
    """Funcionalidades do arquivo FileFunc

    Args:
        *args(string) -> Isto é o que será escrito: Site   --   Password
        escrever (bool, optional): Se irá ser escrito ou não. Defaults to False.
        ler (bool, optional): Se irá ser lido ou não. Defaults to True.
    """
    # Constantes/Variáveis/Flags
    flag_leitura = True
    string_site_pass = ''
    n_linhas, contador = 0, 0
    
    # Criação do Arquivo se não estiver criado
    try:
        passwords_file = open(PATH, 'r+')
    except FileNotFoundError:
        passwords_file = open(PATH, 'w+')

    # Leitura de linhas
    # leitura_file = passwords_file.read()
    # linhas = leitura_file.split('\n')
    
    # for i in linhas:
    #     if i:
    #         n_linhas += 1    

    if ler:
        lista_def = list()
        lista_total = list()
        
        # Lê o arquivo
        while flag_leitura:
            
            # Lê as linhas
            for k in passwords_file.readline():
                string_site_pass += k
            
            # TESTAR ANTES DE USAR -- POSSIVELMENTE NÃO NECESSÁRIO
            # 
            # Passa de Lista de carácteres para uma string
            # for item in range(0, len(lista_def)):
            #     string_site_pass += lista_def[item]
            #     print(string_site_pass)
                
            # lista_def.clear()
            
            lista_def.append(string_site_pass[:])
            
            # Remove site:  //   password:  //   \n
            lista_def = [frase.replace('site:', '') for frase in lista_def]
            lista_def = [frase.replace('password: ', '') for frase in lista_def]
            lista_def = [frase.replace('\n', '') for frase in lista_def]

            lista_total.append(lista_def[::])
            lista_def.clear()
            contador += 1
            
            if contador == 3:
                flag_leitura = False
                
        return lista_total

            
            
print(filefunc('Paypal', '0saAmGsainwl21ewla', escrever=True, ler=True))