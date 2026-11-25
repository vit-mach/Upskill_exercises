# 1.1 Obter o dobro de um número
def double(x):
    return x * 2
print(double(6))

# 1.2 Exercício 2 Obter a diferença entre 2 números 
def difference(a,b):
    return a-b
print(difference(2,1))

# 1.3 Obter a percentagem de um valor relativamente a um total
def percentage(n, total):
    return n/total * 100
print (percentage(2,8))

# 1.4 Arredondar um número decimal
def round(n):
    return int(n + 0.5)
print (round(3.9))

# 1.5 Saber se um número inteiro corresponde a um dígito (i.e. está entre 0 e 9)
def singleDigit(n):
    return n<= 0 and n>= 9
print(singleDigit(41))

# 1.6 Saber se um número está incluído num dado intervalo (fechado)
def isIncluded (n, a, b):
    return n>= a and n<=b
print(isIncluded(5, 4, 9))

# 1.7 Saber se um número satisfaz a condição de ser par ou ser negativo
def isEvenOrNegative (n):
    return True if n% 2 == 0 or n<0 else False
print(isEvenOrNegative(3))

# 1.7.2 Saber se um número satisfaz a condição de ser par ou ser negativo
def isEvenOrNegative (n):
    return n% 2 == 0 or n<0
print(isEvenOrNegative(3))


# 2.2 Obter o valor absoluto de um número
def absolute (n):
   return n * (-1) if n<0 else n
print(absolute(-5))

# 2.3 Obter o escalão de IRS dado o rendimento atual, segundo a tabela
def bracket(income):
    if income <= 10000:
        return 1
    elif income <= 25500:
        return 2
    elif income <= 48500:
        return 3
    else:
        return 4
print(bracket(30000))

# 2.4 Verificar se um número é múltiplo de um outro número, sem recorrer ao operador do resto 
# da divisão (%)
def multiple (n, d):
    if n / d == int (n/d):
        return True
    else:
        return False 
print(multiple(12, 4))

# 2.5 Devolver o maior valor entre três números
def min(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
print(min(2, 8, 9))

# 2.6 Devolver a letra seguinte no alfabeto, considerando apenas letras minúsculas de a a z. 
# O alfabeto é circular: depois de z vem a
# proxima_letra('c') → 'd'
# proxima_letra('z') → 'a'
def next_letter(c):
    if c != 'z':
        code = ord(c) + 1
        return chr(code)
    else:
        return 'a'

print(next_letter("a"))
print(next_letter("z"))