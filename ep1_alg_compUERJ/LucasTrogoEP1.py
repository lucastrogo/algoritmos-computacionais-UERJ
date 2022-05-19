def question_1():
    quant_branco = 0
    quant_vogal = 0
    frase = input('Insira uma frase: ')
    list_frase = [[i for i in str(frase)]]
    for j in range(len(list_frase[0])):
        print(list_frase[0][j])
        if list_frase[0][j] == ' ':
            quant_branco += 1
        elif list_frase[0][j] in ('a', 'e', 'i', 'o', 'u'):
            quant_vogal += 1
    print(f'Quantidade de espaço em branco: {quant_branco} || Quantidade de vogais: {quant_vogal}')


def question_2():
    num_int = int(input('Insira um número inteiro: '))
    num =  0
    list_num = []
    while num < num_int:
        num += 1
        list_num.append(num)
        print(list_num)


def question_3():
    num_int = int(input('Insira um número inteiro: '))
    list_num = [int(i) for i in str(num_int)]
    print(list_num)
    vet = 0
    size = len(list_num) - 1
    for pos in range(size):
        list_num[vet] = list_num[size - pos]
        vet += 1
    print(list_num)

def main():
    question_1()
    question_2()
    question_3()
main()