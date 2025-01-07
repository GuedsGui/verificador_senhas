import string

def senha():
    qtd_caracteres = 8
    
    usuario = input('Usuário: ')
    senha = input('Senha: ')
    
    #funções que verificam se a senha contém letras, números e caracteres especiais
    def alfa(a):
        return any(char.isalpha() for char in a)
    
    def numeros(n):
        return any(char.isdigit() for char in n)
    
    def especiais(e):
        return any(char in string.punctuation for char in e)
    
    while True:
        if alfa(senha) and numeros(senha) and especiais(senha) and len(senha) >= qtd_caracteres and len(usuario) >= qtd_caracteres:
            print('Bem vindo!')
            break
        
        elif len(senha) < qtd_caracteres:
            senha = input('A senha deve conter no mínimo 8 caracteres: ')
        elif len(usuario) < qtd_caracteres:
            usuario = input('O nome de usuário deve conter no mínimo 8 caracteres: ')
        else:
            senha = input('A senha deve conter letras, números e caracteres especiais: ')
            
    print('========== LOGIN ===========')

    #confirmam se o nome de usuário e senha são os mesmos dos cadastrados
    confirma_usuario = input('Nome de usuário: ')
    confirma_senha = input('Informe sua senha: ')
    
    #se for verdadeiro ele loga, se não ele pede para que o usuário informe o nome de usuário ou senha corretamente
    while True:    
        if usuario == confirma_usuario and senha == confirma_senha:
            print('Bem vindo!')
            break
        
        elif usuario == confirma_usuario:
            print('Senha incorreta!')
            confirma_senha = input('Insira sua senha novamente: ')
            
            while True:
                if senha == confirma_senha:
                    break
                break
        
        elif senha == confirma_senha:
            print('Nome de usuário incorreto!')
            confirma_usuario = input('Insira seu nome de usuário novamente: ')
            
            while True:
                if usuario == confirma_usuario:
                    break
                break
        
        else:
            print('Nome de usuário e senha incorretos, por favor, tente novamente!')
            confirma_usuario = input('Insira seu nome de usuário: ')
            confirma_senha = input('Insira sua senha novamente: ')

senha()