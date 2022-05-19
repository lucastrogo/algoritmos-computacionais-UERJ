import random
import string
from os.path import exists



def gerar_users(situation, list_user):
    for _ in range (200):
        nome = ''
        for i in range(0,random.randint(2,7)):
            letra = random.choice(string.ascii_lowercase)
            nome = nome + letra
        senha = ''
        for i in range(0,4):
            senha = senha + str(random.randint(0,9))
        list_user_random = [nome, senha, situation]
        list_user.append(list_user_random)
        generator_list(nome, senha, situation)

def entrar_conta(dados, num_user, situation, list_user):
    if exists('senhas.txt') == True:
        attempts = 0
        with open('senhas.txt', 'r') as arq:
            arq.read()
            nome = input('Informe seu nome: ')
            for j in range(len(list_user)):
                if list_user[j][0] == nome:
                    if list_user[j][2] == 1:
                        print('Sua conta está bloqueada, procure o seu gerente!')
                        main()
                    else:
                        while attempts < 3:
                            senha = int(input('Informe a senha de 4 dígitos: '))
                            if str(list_user[j][1]) == str(senha):
                                    print('Bem vindo a sua conta corrente!')
                                    return main
                            else:
                                attempts += 1
                                print(f'Senha incorreta, você tem mais {3 - attempts}!')
                    if attempts == 3:
                        list_user[j][2] = 1
                        change_situation(list_user)
                        print('Sua conta foi bloqueada, procure o seu gerente!')
    else:
        print("Lista de usuários criada, por favor informe seu nome abaixo.")
        gerar_users(situation, list_user)
        attempts = 0
        with open('senhas.txt', 'r') as arq:
            arq.read()
            nome = input('Informe seu nome: ')
            for j in range(len(list_user)):
                if list_user[j][0] == nome:
                    if list_user[j][2] == 1:
                        print('Sua conta está bloqueada, procure o seu gerente!')
                        main()
                    else:
                        while attempts < 3:
                            senha = int(input('Informe a senha de 4 dígitos: '))
                            if str(list_user[j][1]) == str(senha):
                                    print('Bem vindo a sua conta corrente!')
                                    return main
                            else:
                                attempts += 1
                                print(f'Senha incorreta, você tem mais {3 - attempts} tentativas!')
                    if attempts == 3:
                        list_user[j][2] = 1
                        change_situation(list_user)
                        print('Sua conta foi bloqueada, procure o seu gerente!')


def adiciona_user(dados, num_user, situation, list_user):
    list_senha = []
    nome = input('Informe seu nome: ')
    senha = int(input('Informe a senha de 4 dígitos: '))
    list_senha.append([int(i) for i in str(senha)])
    if len(list_senha[0]) != 4:
        print('Senha diferente de 4 dígitos')
        return adiciona_user(dados, num_user, situation, list_user)
    with open('senhas.txt', 'r') as arq:
        arq.read()
    for j in range(len(list_user)):
        if list_user[j][0] == nome:
            confirmacao = input("Usuário já existente.\nDeseja atualizar seu respectivo nome? (s/n): ")
            while(confirmacao != 's' and confirmacao != 'n'):
                confirmacao = input("Opção inválida.\nDeseja atualizar seu respectivo nome? (s/n): ")
            if(confirmacao == 'n'):
                print("Operação cancelada!\n\n")
                return
        else:
            list_user_especifico = [nome, str(senha), situation]
            list_user.append(list_user_especifico)
            num_user += 1
            generator_list(nome, senha, situation)
            print('Dados adicionado com sucesso!\n\n')
            return


def generator_list(nome, senha, situation):
    with open('senhas.txt', 'a') as arq:
        arq.write('Nome | Senha | Situacao\n')
        arq.write(f'{nome} | {senha} | {situation}\n')
        arq.close()



def change_situation(list_user):
    with open('senhas.txt', 'w') as arq:
        for i in range(len(list_user)):
                with open('senhas.txt', 'a') as arq:
                    arq.write('Nome | Senha | Situacao\n')
                    arq.write(f'{list_user[i][0]} | {list_user[i][1]} | {list_user[i][2]}\n')
        arq.close()

def main():
    opcoes = {
        '1': entrar_conta,
        '2': adiciona_user,
    }
    dados = []
    list_user = []
    num_user = -1
    situation = 0
    while True:
        opcao = input('Informe uma das opcoes abaixo:\n'
                    '1 - Acesso conta corrente\n'
                    '2 - Criar conta corrente\n'
                    'ENTER - Sair do programa\n')
        if opcao == '':
            break
        elif opcao in opcoes.keys():
            opcoes[opcao](dados, num_user, situation, list_user)
        else:
            print('Opcao invalida!')


main()
