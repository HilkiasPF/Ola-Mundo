def separador(x):
    return print('=' * x)

def cor(x):
    return print(f'\033[31m{x}\033[m')

def errou(x):
    while True:
        try:
            x = float(input(f'{x}'))
            break
        except ValueError:
            cor('Inválido')
    return x

separador(30)
cor('IMC'.center(30))
separador(30)

nome = input('Nome:')

sexo = ''
while sexo != 'm' and sexo != 'f':
    sexo = input('Sexo[m/f]:')

idade = errou('Idade:')
peso = errou('Peso:')
altura = errou('Altura:')
imc = peso / (altura ** 2)
separador(30)
print(f'IMC = {imc:.2f}kg/m²')

if imc < 19:
    print(f'Baixo peso, seu peso ideal é {altura**2 * 21.9:.2f}kg, {nome}.')
elif 25 > imc > 19:
    print(f'Peso ideal, {nome}.')
elif imc > 25:
    print(f'Acima do peso, seu peso ideal é {altura ** 2 * 21.9:.2f}kg, {nome}.')


