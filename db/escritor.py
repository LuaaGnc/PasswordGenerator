import os.path
import re

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
        password_file = open(PATH, 'r+')
    except FileNotFoundError:
        password_file = open(PATH, 'w+')

    # Leitura de linhas
    leitura_file = password_file.read()
    linhas = leitura_file.split('\n')
    
    for i in linhas:
        if i:
            n_linhas += 1    

    if ler:
        lista_site_pass = list()
        lista_site_pass2 = list()
        # Lê o arquiv 
        while flag_leitura:

            for i in password_file.readline():
                lista_site_pass.append(i)
            
            for item in range(0, len(lista_site_pass)):
                string_site_pass += lista_site_pass[item]
            
            lista_site_pass.clear()
            
            lista_site_pass.append(string_site_pass)
            
            # Remove site:  //   password:  //   \n
            lista_site_pass = [frase.replace('site:', '') for frase in lista_site_pass]
            lista_site_pass = [frase.replace('password: ', '') for frase in lista_site_pass]
            lista_site_pass = [frase.replace('\n', '') for frase in lista_site_pass]
            
            lista_site_pass2.append(lista_site_pass[:])
            
            # Remove todos os itens para depois ler a próxima linha
            lista_site_pass.clear()
            
            if contador == n_linhas:
                flag_leitura = False
            else:
                contador += 1
        
            
        return lista_site_pass2
            
        
            
            
print(filefunc('sth', 'saidsainwlewla', escrever=False, ler=True))