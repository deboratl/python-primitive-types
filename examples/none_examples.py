# Atribuindo None a uma variável
x = None
print(x)  # Saída: None


def verifica_valor(valor):
    if valor is None:
        return "Valor não foi definido."
    else:
        return f"Valor definido: {valor}"


# Testando a função
print(verifica_valor(None))  # Saída: Valor não foi definido.
print(verifica_valor(10))    # Saída: Valor definido: 10

def saudacao():
    print("Olá!")


resultado = saudacao()
print(resultado)  # Saída: None

# Comparando uma variável com None
a = None

if a is None:
    print("a é None")  # Saída: a é None

if a is not None:
    print("a não é None")

def configura_sistema(opcao=None):
    if opcao is None:
        opcao = "padrão"
    print(f"Opção configurada: {opcao}")

# Chamando a função sem fornecer o argumento opcional
configura_sistema()  # Saída: Opção configurada: padrão

# Chamando a função com um argumento opcional
configura_sistema(opcao="avançada")  # Saída: Opção configurada: avançado

def busca_elemento(lista, elemento):
    if elemento in lista:
        return elemento
    else:
        return None


resultado = busca_elemento([1, 2, 3], 4)
if resultado is None:
    print("Elemento não encontrado.")  # Saída: Elemento não encontrado.


def soma(a, b):
    if a is None or b is None:
        return "Erro: Um dos valores é None."
    return a + b


print(soma(5, None))  # Saída: Erro: Um dos valores é None.
print(soma(5, 3))     # Saída: 8

# Limpando uma variável
x = 10
x = None
print(x)  # Saída: None
