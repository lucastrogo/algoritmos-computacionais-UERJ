def deposito(cedulas, history_depos_saque, conta_value_real):
    conta_value = float(input("Por favor, insira o valor a ser depositado: "))
    conta_value_real[0] += conta_value
    history_depos_saque.append(conta_value)
    cedula_value = int(input("Insira a cédula a ser inserida na máquina. Nota de 100, 50, 20, 10, 2 ou 1: "))
    num_cedula = int(input("Insira o número da respectiva cédula a serem inseridos: "))
    if cedula_value == 100:
        cedulas["Cem"] += num_cedula
    elif cedula_value == 50:
        cedulas["Cinquenta"] += num_cedula
    elif cedula_value == 20:
        cedulas["Vinte"] += num_cedula
    elif cedula_value == 10:
        cedulas["Dez"] += num_cedula
    elif cedula_value == 2:
        cedulas["Dois"] += num_cedula
    elif cedula_value == 1:
        cedulas["Um"] += num_cedula
    print("O valor depositado foi de R$", conta_value)

def saque(cedulas, history_depos_saque, conta_value_real):
    saque_value = float(input(f"Por favor, insira o valor a ser sacado. Valor atual em conta R${conta_value_real[0]}: "))
    print(f"Número de cédulas: {cedulas}")
    if saque_value <= conta_value_real[0]:
        conta_value_real[0] -= saque_value
        history_depos_saque.append(saque_value * (-1))
        if saque_value // 100 == 0:
            cedulas["Cem"] -= (saque_value / 100)
        elif saque_value // 50 == 0:
            cedulas["Cinquenta"] -= (saque_value / 50)
        elif saque_value // 20 == 0:
            cedulas["Vinte"] -= (saque_value / 20)
        elif saque_value // 10 == 0:
            cedulas["Dez"] -= (saque_value / 10)
        elif saque_value //2 == 0:
            cedulas["Dois"] -= (saque_value / 2)
        elif saque_value //1 ==0:
            cedulas["Um"] -= (saque_value / 1)
    else:
        print("Valor de saque maior que em conta, por favor informe um valor menor ou igual ao que está na conta.")
        return saque(cedulas, history_depos_saque, conta_value_real)

def saque_depos_history(cedulas, history_depos_saque, conta_value_real):
    print(history_depos_saque)

def saldo(cedulas, history_depos_saque, conta_value_real):
    print(f"O seu saldo é de R${conta_value_real[0]}")

def main():
    opcoes = {
        '1': deposito,
        '2': saque,
        '3': saque_depos_history,
        '4': saldo
    }
    history_depos_saque = []
    cedulas = {"Cem": 100, "Cinquenta": 100, "Vinte": 100, "Dez": 100, "Dois": 100, "Um": 100}
    conta_value_real = [0]
    while True:
        opcao = input('Informe uma das opcoes abaixo:\n'
                    '1 - Operação de depósito\n'
                    '2 - Operação de saque\n'
                    '3 - Histórico de depósito e saque\n'
                    '4 - Saldo em conta\n'
                    'ENTER - Sair do programa\n')
        if opcao == '':
            break
        elif opcao in opcoes.keys():
            opcoes[opcao](cedulas, history_depos_saque, conta_value_real)
        else:
            print('Opcao invalida!')

main()
