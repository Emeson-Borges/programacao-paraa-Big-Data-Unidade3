# Exemplo 0: Somar dois números
def soma(a, b):
    resultado = a + b
    return resultado

# Chamando a função
resultado_soma = soma(5, 3)
print("Resultado da soma:", resultado_soma)  # Saída: Resultado da soma: 8

###############################################################################################
# Exemplo 1: Função para Verificar se um Número é Par
def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Chamando a função
numero = 6
if eh_par(numero):
    print(numero, "é um número par.")
else:
    print(numero, "não é um número par.")

###############################################################################################
# Exemplo 2: Função para Calcular o Fatorial de um Número
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Chamando a função
numero = 5
resultado_fatorial = fatorial(numero)
print("O fatorial de", numero, "é", resultado_fatorial)

###############################################################################################
#Exemplo 3: Função para Verificar se uma Palavra é um Palíndromo
def eh_palindromo(palavra):
    palavra = palavra.lower()  # Converter para minúsculas para ser case-insensitive
    return palavra == palavra[::-1]

# Chamando a função
texto = "radar"
if eh_palindromo(texto):
    print(texto, "é um palíndromo.")
else:
    print(texto, "não é um palíndromo.")
