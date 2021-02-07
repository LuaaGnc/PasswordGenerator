from random import shuffle, randint

def gerador_password(comprimento):
    """ Generates a password with a certain lenght

    Args:
        comprimento ( [type]--> int ): Lenght of the password
    
    Return:
        password ( [type] --> list): String of password Characters
    """
    password_caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567012345678901234567890123456789'

    password_string = ''
    
    password_list = list(password_caracteres[0:90:])
    shuffle(password_list)
    
    # Apresenta a lista de caracteres da password - Quebra quando a password tiver o mesmo comprimento que o desejado
    while len(password_list) > comprimento:
        password_list.pop(randint(0, len(password_list) - 1))
    
    # Passa de Lista de Strings para String
    for item in range(0, len(password_list)):
        password_string += password_list[item]
    
    return password_string

