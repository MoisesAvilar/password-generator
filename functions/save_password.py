def save_password(password, conta):
    with open('arquivo.txt', 'a+') as file:
        file.write(f"Conta/Usuario: {conta} \nSenha: {password}\n")
