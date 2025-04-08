def volumeFeijoada():
    while True:
        try:
            volumeF = int(input("Digite o volume em ml da Feijoada:\n "))
            if (volumeF >= 300) and (volumeF <= 5000):
                return volumeF*0.08
            else:
                print("Não aceitamos porções menos que 300ml ou maiores que 5l. ")
                continue
        except ValueError:
            print("Você não digitou uma opção válida.")



def opcaoFeijoada():
    print("b - Básica (Feijão + paiol + costelinha) ")
    print("p - Premium (Feijão + paiol + costelinha + partes de porco)")
    print("s - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)")
    while True:
        opcaoF = input("Digite a opção de Feijoada: ")
        if opcaoF == 'b':
            return 1
        elif opcaoF == 'p':
            return 1.25
        elif opcaoF == 's':
            return 1.50
        else:
            print('Você não digitou uma opção válida.')
            continue


def acompanhamentoFeijoada():
    acumulador = 0
    print("0- Não desejo mais acompanhamentos (encerrar pedido)")
    print("1- 200g de arroz")
    print("2- 150g de farofa especial")
    print("3- 100g de couve cozida")
    print("4- 1 laranja descascada")
    while True:
        acompanhamentoF = int(input("Deseja mais algum acompanhamento: \n"))
        if acompanhamentoF == 1:
            acumulador += 5
            continue
        elif acompanhamentoF == 2:
            acumulador += 6
            continue
        elif acompanhamentoF == 3:
            acumulador += 7
            continue
        elif acompanhamentoF == 4:
            acumulador += 3
            continue
        elif acompanhamentoF == 0:
            return acumulador
            break
        else:
            print("Opção Inválida")
            continue


print('Bem vindo ao Programa de Feijoada do Adriano Rocha ')
volume = volumeFeijoada()
opcao = opcaoFeijoada()
ac = acompanhamentoFeijoada()


print("{:.2f}" .format(volume))
print("{:.2f}" .format(opcao))

acompanhamento = acompanhamentoFeijoada()
print("{:.2f}" .format(acompanhamento))
total = volume * opcao + ac
print("O valor total a ser pago é de {} R$, (volume = {}, * opcao = {} + acompanhamento = {}" .format(total, volume, opcao, ac))
