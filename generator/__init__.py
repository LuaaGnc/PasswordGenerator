from random import shuffle, randint

def gerador(comprimento):
    """ Generates a password with a certain lenght

    Args:
        comprimento ( [type]--> int ): Lenght of the password
    
    Return:
        password ( [type] --> list): List with password characters
    """
    password_caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567012345678901234567890123456789'
    password_list = list(password_caracteres[0:90:])
    shuffle(password_list)
    
    # Quebra quando a password tiver o mesmo comprimento que o desejado
    while len(password_list) > comprimento:
        password_list.pop(randint(0, len(password_list) - 1))
        
    return password_list

a = gerador(20)
print(a)