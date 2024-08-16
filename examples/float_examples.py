# Definindo variáveis de ponto flutuante
a = 5.75
b = 2.5

# Soma
soma = a + b
print("Soma:", soma)  # 8.25

# Subtração
subtracao = a - b
print("Subtração:", subtracao)  # 3.25

# Multiplicação
multiplicacao = a * b
print("Multiplicação:", multiplicacao)  # 14.375

# Divisão
divisao = a / b
print("Divisão:", divisao)  # 2.3

# Divisão por inteiro
divisao_inteira = a // b
print("Divisão inteira:", divisao_inteira)  # 2.0

# Módulo (resto da divisão)
modulo = a % b
print("Módulo:", modulo)  # 0.75

# Converter de inteiro para float
x = 10
x_float = float(x)
print("x como float:", x_float)  # 10.0

# Converter de float para inteiro
y = 3.14
y_int = int(y)
print("y como int:", y_int)  # 3 (perde a parte fracionária)

# Arredondando um número float
z = 3.14159
z_arredondado = round(z, 2)  # Arredonda para 2 casas decimais
print("z arredondado:", z_arredondado)  # 3.14

# Arredondamento para o número inteiro mais próximo
z_arredondado_int = round(z)
print("z arredondado para inteiro:", z_arredondado_int)  # 3

# Formatação de floats para strings
pi = 3.14159265359
print("Pi com 2 casas decimais: {:.2f}".format(pi))  # Pi com 2 casas decimais: 3.14
print("Pi com 4 casas decimais: {:.4f}".format(pi))  # Pi com 4 casas decimais: 3.1416

# Cálculo de média aritmética
notas = [7.5, 8.0, 6.5, 9.0]
media = sum(notas) / len(notas)
print("Média das notas:", media)  # 7.75

