# Função para verificar se um número é positivo
def is_positive(number):
    """
    Retorna True se o número for positivo, False caso contrário.
    """
    return number > 0

# Função para verificar se duas strings são iguais
def are_strings_equal(str1, str2):
    """
    Retorna True se as duas strings forem iguais, False caso contrário.
    """
    return str1 == str2

# Função para verificar se um número é par
def is_even(number):
    """
    Retorna True se o número for par, False caso contrário.
    """
    return number % 2 == 0

# Testando as funções booleanas
print("Is 10 positive?", is_positive(10))  # True
print("Is -3 positive?", is_positive(-3))  # False

print("Are 'hello' and 'hello' equal?", are_strings_equal('hello', 'hello'))  # True
print("Are 'hello' and 'world' equal?", are_strings_equal('hello', 'world'))  # False

print("Is 4 even?", is_even(4))  # True
print("Is 7 even?", is_even(7))  # False

# Verificando igualdade
a = 10
b = 20
print("a == b:", a == b)  # False, porque 10 não é igual a 20

# Verificando desigualdade
print("a != b:", a != b)  # True, porque 10 é diferente de 20

# Comparando maior que
print("a > b:", a > b)  # False, porque 10 não é maior que 20

# Comparando menor que
print("a < b:", a < b)  # True, porque 10 é menor que 20

# Comparando maior ou igual
print("a >= 10:", a >= 10)  # True, porque 10 é igual a 10

# Comparando menor ou igual
print("b <= 20:", b <= 20)  # True, porque 20 é igual a 20

# Usando o operador AND (e)
x = True
y = False
print("x and y:", x and y)  # False, porque y é False

# Usando o operador OR (ou)
print("x or y:", x or y)  # True, porque x é True

# Usando o operador NOT (não)
print("not x:", not x)  # False, inverte o valor de x
print("not y:", not y)  # True, inverte o valor de y

# Verificar se uma lista está vazia
my_list = []
print("Is my_list empty?", not my_list)  # True, lista vazia é considerada False

# Verificar se um item está em uma lista
items = [1, 2, 3, 4, 5]
print("Is 3 in items?", 3 in items)  # True, 3 está na lista

# Verificar se um item não está em uma lista
print("Is 6 not in items?", 6 not in items)  # True, 6 não está na lista

# Verificar se uma string contém outra string
phrase = "Python is fun"
print("Does 'Python' in phrase?", 'Python' in phrase)  # True

# Verificar se uma string está vazia
empty_string = ""
print("Is the string empty?", not empty_string)  # True, string vazia é considerada False

# Comparar strings (case-sensitive)
print("Is 'apple' == 'Apple'?", 'apple' == 'Apple')  # False, comparações são sensíveis a maiúsculas/minúsculas

# Verificar se um número é positivo
def is_positive(num):
    return num > 0

print("Is 10 positive?", is_positive(10))  # True
print("Is -5 positive?", is_positive(-5))  # False

# Verificar se um número é negativo
def is_negative(num):
    return num < 0

print("Is -3 negative?", is_negative(-3))  # True
print("Is 7 negative?", is_negative(7))  # False

# Verificar se um número está em um intervalo
def is_in_range(num, start, end):
    return start <= num <= end

print("Is 5 between 1 and 10?", is_in_range(5, 1, 10))  # True
print("Is 15 between 1 and 10?", is_in_range(15, 1, 10))  # False

# Verificar se uma chave existe em um dicionário
person = {'name': 'Alice', 'age': 25}
print("Is 'name' a key in person?", 'name' in person)  # True

# Verificar se um valor existe em um dicionário
print("Is 25 a value in person?", 25 in person.values())  # True

# Verificar se uma chave não existe em um dicionário
print("Is 'address' not a key in person?", 'address' not in person)  # True

# Verificar se uma variável é None
nothing = None
print("Is nothing None?", nothing is None)  # True

# Verificar se uma variável não é None
value = 42
print("Is value not None?", value is not None)  # True

# Exemplo de condicional usando booleano
age = 18
if age >= 18:
    print("You are an adult.")  # Será exibido, porque age >= 18 é True
else:
    print("You are not an adult.")

# Qualquer valor pode ser convertido para um booleano usando a função bool()

# Números: 0 é False, outros são True
    print("bool(0):", bool(0))  # False
    print("bool(42):", bool(42))  # True

    # Strings: String vazia é False, outras são True
    print("bool(''):", bool(''))  # False
    print("bool('Python'):", bool('Python'))  # True

    # Listas: Lista vazia é False, outras são True
    print("bool([]):", bool([]))  # False
    print("bool([1, 2, 3]):", bool([1, 2, 3]))  # True

# Função para verificar se um ano é bissexto
def is_leap_year(year):
    """
    Retorna True se o ano for bissexto, False caso contrário.
    """
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

# Testando a função
print("Is 2024 a leap year?", is_leap_year(2024))  # True
print("Is 1900 a leap year?", is_leap_year(1900))  # False

