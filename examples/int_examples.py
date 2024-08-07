# Função para somar dois inteiros
def sum_two_integers(a, b):
    """
    Retorna a soma de dois números inteiros.
    """
    return a + b

# Função para calcular o fatorial de um número inteiro
def factorial(n):
    """
    Retorna o fatorial de um número inteiro n.
    Exemplo: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
    """
    if n < 0:
        return "O fatorial não está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Função para verificar se um número é par
def is_even(number):
    """
    Retorna True se o número for par, False caso contrário.
    """
    return number % 2 == 0

# Função para encontrar o maior de três inteiros
def max_of_three(a, b, c):
    """
    Retorna o maior entre três números inteiros.
    """
    return max(a, b, c)

# Função para calcular a soma dos primeiros n inteiros positivos
def sum_of_n_integers(n):
    """
    Retorna a soma dos primeiros n números inteiros positivos.
    Exemplo: sum_of_n_integers(5) = 1 + 2 + 3 + 4 + 5 = 15
    """
    if n < 1:
        return "n deve ser um inteiro positivo."

    soma = 0  # Inicializa a variável que armazenará a soma
    for i in range(1, n + 1):  # Itera de 1 até n (inclusive)
        soma = soma + i  # Adiciona o valor de i à soma

    return soma  # Retorna o valor final da soma

# Testando as funções
print("Sum of 3 and 5:", sum_two_integers(3, 5))
print("Factorial of 5:", factorial(5))
print("Is 4 even?", is_even(4))
print("Maximum of 10, 20, and 15:", max_of_three(10, 20, 15))
print("Sum of the first 10 positive integers:", sum_of_n_integers(10))
