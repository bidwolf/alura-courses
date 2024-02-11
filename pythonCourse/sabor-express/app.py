def betweenBreakLines(str:str):
  for letter in str:
    print(f'{letter}\n')

print('Sabor Express\n')
options = [
  '1. Cadastrar restaurante',
  '2. Listar restaurante',
  '3. Ativar restaurante',
  '4. Sair',
]
betweenBreakLines(options)
opcao_escolhida = input('Escolha uma opção:')
print(f'Você escolheu a opção {opcao_escolhida}\n')

print ('Python na Escola de Programação da Alura\n')

# Usando loop
betweenBreakLines('ALURA')

# Usando Sep
print('A','L','U','R','A',sep='\n')

pi = 3.14159

# Usando Round
print(f'{round(pi, 2)}')
# Usando o método f-string
print(f'{pi:.2f}')
# Usando .format
print('{:.2f}'.format(pi))

nome = 'Henrique de Paula Rodrigues'
idade = 23
