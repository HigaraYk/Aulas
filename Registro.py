


'''1º o print'''



print('--1--')

#Extrair resultados para o console 


print("Olá")
print('Mundo')



'''2º Adicionando comentários'''



print('--2--')

#Comentários não podem ser executados pelo programa

#Comentário de uma linha é usado == ( # )


print('Sexta')


'''
Comentário longo
é usado == 3 aspas no começo e 3 aspas no final 
'''



'''3º Strings e Numeros'''



print('--3--')

#Data Types 


#   Texto comum é lido como Str (String)  'Texto'
print('texto')

#   Numeros sem fração são numeros inteiros, lido como Int (Integer) 1,2,3...
print(123)

#   Numeros fracionados são lidos como (float) 1.5,2.0,3.3...
print(1.1)

#   Booleano é um tipo de dado primitivo da computação que possui apenas um de dois valores possíveis: Verdadeiro ou Falso
print(True)
print(False)



'''4º Entendendo sobre variáveis'''



print('--4--')
x = 2 
# X,Y e Z são o containers, 2, olá e mundo são dados 
y = 'Olá' 

z = ' Mundo'

print (x + x) 
#== 4 

print(y + z) 
#== olá



'''5º Modificando o tipo de dados'''



print('--5--')
x = str(3) 
y = int(4)
z = float(5)


print(x) 
#X vira texto
print(y) 
#Y vira numero inteiro
print(z) 
#Z vira numero fracionado

print('---')
print(x + x) 
#X == 33 pois ele soma um texto + texto
print(y + y) 
print(z + z) 



'''6º Praticando com Strings e Integers''' 



print('--6--')

# O Guest 1337 tem 9 anos de idade e mora nos EUA. 

nome = 'Guest 1337'
idade = 9
cidade = 'EUA' 

'''
print('O ' + nome + ' tem ' + idade + ' anos de idade e mora nos ' + cidade ) Existem duas formas de resolver esse problema.

Primeira formas : print('O ' + nome + ' tem ' + str(idade) + ' anos de idade e mora nos ' + cidade )

Segunda forma: idade = str(idade) ou idade = str(9)

Essas duas formas transformam a idade de Int(numero inteiro) para str(texto). 
'''

idade = str(idade)

print('O ' + nome + ' tem ' + idade + ' anos de idade e mora nos ' + cidade )



'''7º Adicionando Input'''



print('--7--')

nome = input('Qual é o seu nome?')

idade = str(input('Qual é a sua idade?'))

cidade = input('Onde você mora?')


print('O ' + nome + ' tem ' + idade + ' anos de idade e mora em ' + cidade )



'''8º Calculando idade com input'''



print('--8--')

ano_nascimento = 1985

idade = 2026 - ano_nascimento

print(idade)

'''
ano_nascimento = input('Em que ano você nasceu? ') 
Este código não funciona pois não é possível trabalhar com Int e Str ao mesmo tempo.

ano_nascimento é uma String.
idade é um numero.
'''

print('---')


ano_nascimento = input('Em que ano você nasceu?')

idade = 2026 - int(ano_nascimento)

print(idade)

print(type(ano_nascimento))
print(type(idade))

#type define o tipo de dado, se ele é Str, Int, Float ou Bool.



'''9º Entendendo o Slice'''



print('--9--')



# Slice do inglês é: fatiar

fruta = 'abacate'
#index   0123456

'''
Essa variável armazena o dado 'acabate'. O abacate é armazenado por caracteres, porque é uma string.
Cada caracter ganha uma posição dentro da variável, essa posição é chamada de Index. 
'''

print(fruta)

print(fruta[1])
#O número em [] define a posição do Index. 1 == b 

print('---')

#é possível puxar mais de uma letra. Exemplo: letra 2 ao 5 

print(fruta[2:5])

''' 
Em Python, quando se trabalha com index. Ao determinar um valor inicial
ele sempre irá pegar esse valor inicial. Mas, o final do index ele sempre pega uma letra antes.
Por que aquele index não deve ser mostrado, segundo as regras de Python.
'''


#também é possível utilizar valores negativos.

print(fruta[-1])

print('---')

valor = str(99.75)
#index      01234

print(valor[3:5])



'''10º Utilizando Formated Strings'''



print('--10--')


nome = 'Marcus'
sobrenome = 'Copeland'
profissão = 'Agente do FBI'

texto = 'O ' + nome + ' ' + sobrenome + ' é um excelente ' + profissão

print(texto)

print('---')

#vamos usar uma forma alternativa para melhorar o texto.

texto2 = f'O {nome} {sobrenome} é um excelente [{profissão}].'
#dessa forma, o código fica mais limpo e menor.
print(texto2)



'''11º Metodos para Strings'''



print('--11--')

mensagem = '     Eu adoro comida caseira'

'''
Esse método serve para determinar se o texto terá todas as sua palavras em 
maiúculo ou em minúsculo, também é possível determinar que todas as primeiras 
letras serão em maiúculo.
'''

print(mensagem)

#quando você quer utilizar um método, basta dolocar um (.) depois da variável.

print('---')

print(mensagem.lower())
#lower é tudo em minúsculo.
print(mensagem.upper())
#upper é tudo em maiúsculo.
print(mensagem.capitalize())
#capitalize deixa a primeira letra em maiúscula.
print(mensagem.find('c'))
#find procura o index do caracter, se for a palavra inteira, mostra onde começa.
print(mensagem.replace('a', 'e'))
#replace substitui um valor antigo por um novo. 
print(mensagem.replace('caseira', 'feita em casa'))
#Pode ser usado para letras ou palavras.
print(mensagem.strip())
#strip remove todo o espaço antes do primeiro caracter ou o index 0. 



'''12º Operações matemáticas em Python'''



print('--12--')

# Adição e subtração 
# Multiplicação e divisão    
# Parenteses 
# Exponenciais 

calculo = 2 + 2

print(calculo)

calculo = 2 + 2 * 3
# 2 + (2 * 3)
print(calculo)

#Se existe uma soma e uma multiplicação, a operação priorizada é a multiplicação.

#Se tiver multiplicação e divisão na mesma linha, sempre será executando da esquerda para a direita.

calculo = 2 + 2 * 3 / 2
# 2 + ((2 * 3) / 2)
print(calculo)

calculo = (2 + 2) * 3

print(calculo)

calculo = 2 ** 3 

# (**) significa expoente. 2 ** 3 = 2.2.2 = 8

''' 
Ordem das operações: 
1º Parenteses
2º Exponencial 
3º Multiplicação e divisão
4º Adição e subtração
'''


'''13º Operadores de comparação'''




