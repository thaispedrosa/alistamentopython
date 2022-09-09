from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano de nascimento?'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade< 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, ainda faltam {} anos para o alistamento.'.format(saldo))
elif idade > 18:
    saldo_2 = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo_2))
