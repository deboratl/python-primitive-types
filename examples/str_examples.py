# Strings podem ser definidas com aspas simples ou duplas
mensagem = 'Olá, Mundo!'
titulo = "Bem-vindo ao PyCharm"

print(mensagem)
print(titulo)


# Você pode concatenar (juntar) strings usando o operador +
nome = "Maria"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome

print(nome_completo)  # Saída: Maria Silva


# Strings podem ser repetidas usando o operador *
risada = "ha" * 3
print(risada)  # Saída: hahaha


# Você pode acessar caracteres individuais em uma string usando índices
palavra = "Python"

primeira_letra = palavra[0]
ultima_letra = palavra[-1]

print(primeira_letra)  # Saída: P
print(ultima_letra)    # Saída: n

# Fatiamento permite obter substrings
parte = palavra[0:3]
print(parte)  # Saída: Pyt


# Strings têm vários métodos úteis
frase = "   Olá, Mundo!   "

# Remover espaços em branco no início e no fim
frase_limpa = frase.strip()

# Converter para maiúsculas
frase_maiuscula = frase_limpa.upper()

# Substituir partes da string
frase_substituida = frase_limpa.replace("Mundo", "PyCharm")

print(frase_limpa)       # Saída: Olá, Mundo!
print(frase_maiuscula)   # Saída: OLÁ, MUNDO!
print(frase_substituida) # Saída: Olá, PyCharm!


# Você pode verificar se uma substring está presente em uma string
texto = "Programação em Python é divertida!"

tem_python = "Python" in texto
tem_java = "Java" in texto

print(tem_python)  # Saída: True
print(tem_java)    # Saída: False


# Strings podem ser definidas em múltiplas linhas usando três aspas
descricao = """Este é um exemplo
de uma string
multilinha."""

print(descricao)


# Formatação de strings permite inserir valores de variáveis em uma string
nome = "João"
idade = 25

# Usando f-strings (Python 3.6+)
mensagem = f"Meu nome é {nome} e eu tenho {idade} anos."
print(mensagem)  # Saída: Meu nome é João e eu tenho 25 anos.

# Usando o método format (funciona em todas as versões do Python)
mensagem = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(mensagem)  # Saída: Meu nome é João e eu tenho 25 anos.
