database = {
    'usuario1':'senha123',
    'usuario2':'senha321',
    'usuario3':'senha456'
}
def login():
    while True:
        nome_usuario = input('Digite o nome de usuário: ')
        senha_usuario = input('Digite a senha do usuário: ')

        #Conferir se o nome do usuário está na lista
        if nome_usuario in database:
            #confirmar se a senha está errada
            if database[nome_usuario] == senha_usuario:
                print('Seja bem-vindo(a)')
                break
            else:
                print('Senha inválida. Tente novamente.')
        else:
            print('Usuário não encontrado. Por favor, tente novamente.')

login()