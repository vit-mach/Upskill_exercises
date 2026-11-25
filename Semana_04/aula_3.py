# Aula 3 — Ciclos while e estruturas de dados (listas, tuplas, sets e dicionários)

# ---------------------------------------------------------------------------
# PARTE 1 — ciclos while com números
# ---------------------------------------------------------------------------

# 1.1 Recebe um número e devolve o primeiro algarismo da representação decimal de n.
# Este valor pode ser obtido fazendo sucessivas divisões por 10
# IDEIA: cada divisão inteira por 10 "corta" o último algarismo.
# Repetimos até sobrar só um algarismo, que é o primeiro.
def first_digit(n):
    while n >= 10:      # enquanto o número tiver 2 ou mais algarismos
        n = n // 10     # divisão inteira: 1234 → 123 → 12 → 1
    return n            # sobrou um só algarismo: é o primeiro
print(first_digit(2011))  # 2


# 1.2 Recebe um número natural e devolve a potência 2^n (sem usar multiplicação)
# IDEIA: 2^n = começar no 1 e duplicar n vezes. Duplicar = somar o número a si próprio.
def power_of_two(n):
    result = 1                    # acumulador: começa em 1 (2^0 = 1); se fosse 0, ficava sempre 0
    i = 0                         # contador: quantas duplicações já fizemos
    while i < n:                  # corre exatamente n vezes
        result = result + result  # duplica o acumulador só com + (ex.: 8 + 8 = 16)
        i += 1                    # avança o contador; sem isto, ciclo infinito
    return result                 # no fim, devolve o acumulador
print(power_of_two(4))  # 16


# 1.3 Recebe como argumento um número natural n e devolve a soma dos números naturais até n
# IDEIA: o contador vai passando por cada número e soma-se ao acumulador
def sum_up_to(n):
    result = 0                # acumulador: começa em 0 (somar 0 não estraga a soma)
    i = 1                     # contador: começa no 1 (somar o 0 seria inútil)
    while i <= n:             # <= para o próprio n também entrar na soma
        result = result + i   # o contador é o número a somar nesta volta (1, 2, 3...)
        i += 1                # avança para o próximo número; sem isto, ciclo infinito
    return result             # no fim, devolve o acumulador
print(sum_up_to(5))  # 15


# 1.4 Recebe como argumento dois números naturais n e p e devolve a soma de números naturais
# pares compreendidos entre os dois números (intervalo fechado)
# IDEIA: Soma n + (n+1) + ... + p, mas só se o número for par.
# O contador vai passando por cada número e soma-se ao acumulador se for par.
def sum_even_numbers_between(n, p):
    result = 0                  # acumulador: começa em 0 (somar 0 não estraga a soma)
    i = n                       # contador: começa no n (o primeiro número do intervalo)
    while i <= p:               # <= para o próprio p também entrar na soma
        if i % 2 == 0:          # verifica se o número é par
            result += i         # soma o número par ao acumulador
        i += 1                  # avança para o próximo número; sem isto, o ciclo é infinito
    return result               # devolve o acumulador após as somas
print(sum_even_numbers_between(3, 8))  # 18


# ---------------------------------------------------------------------------
# PARTE 2 — ciclos while com listas
# ---------------------------------------------------------------------------

# 2.1 Calcula a média dos valores de uma lista
# IDEIA: O acumulador vai somando os elementos da lista, e no final divide-se pelo tamanho da lista
def mean(lista):
    total = 0                    # acumulador: soma dos elementos
    i = 0                        # índice: começa na posição 0
    while i < len(lista):        # enquanto o índice for menor que o tamanho da lista
        total = total + lista[i] # soma o elemento da posição i ao acumulador
        i += 1                   # avança para a próxima posição
    return total / len(lista)    # passo final: soma / quantidade
print(mean([13, 14, 16, 15]))  # 14.5


# 2.2 Copia um vetor de inteiros, tendo o novo vetor um tamanho dado como argumento
# IDEIA: Crio uma lista nova vazia. Percorro as posições de 0 até ao tamanho pedido (sem o incluir).
# Em cada posição, se ela for menor que o tamanho da lista original, acrescento
# o elemento da lista original nessa posição; senão, acrescento 0.
# No fim devolvo a nova lista.
def copy(lista, tamanho):
    nova = []                       # a lista nova começa vazia
    i = 0                           # posição atual, começa no 0
    while i < tamanho:              # paro quando a nova tiver o tamanho pedido
        if i < len(lista):          # a posição existe na lista original?
            nova.append(lista[i])   # sim → acrescenta o elemento da original nessa posição
        else:
            nova.append(0)          # não → acrescenta 0
        i += 1                      # passa à posição seguinte
    return nova                     # devolve a lista nova
print(copy([1, 2, 3], 6))  # [1, 2, 3, 0, 0, 0]


# 2.3 Verifica se existe um determinado valor n numa lista
# IDEIA: percorro a lista; assim que encontro o valor devolvo True.
# Se o ciclo acabar sem o encontrar, devolvo False.
def list_contains(lista, n):
    i = 0                           # índice: começa na posição 0
    while i < len(lista):           # percorre todas as posições válidas
        if lista[i] == n:           # encontrei o valor?
            return True             # sim → não preciso de ver o resto
        i += 1                      # passa à posição seguinte
    return False                    # o ciclo acabou e nunca o encontrei
print(list_contains([1, 2, 3], 2))  # True


# 2.4 Permita obter metade de uma lista, incluindo opcionalmente o elemento do meio
# (caso o comprimento da lista seja ímpar)
# IDEIA: Percorro a lista até a metade. Se o comprimento for ímpar e include_middle
# for True, acrescento o elemento do meio.
def first_half(lista, include_middle):
    half = len(lista) // 2                              # metade do tamanho (divisão inteira //)
    new = []                                            # a lista nova começa vazia
    i = 0                                               # índice: começa na posição 0
    while i < half:                                     # só percorre a primeira metade
        new.append(lista[i])                            # acrescenta o elemento da posição i
        i += 1                                          # passa à posição seguinte
    if include_middle and len(lista) % 2 == 1:          # comprimento ímpar e pediram o do meio?
        new.append(lista[half])                         # o do meio está na posição half
    return new                                          # devolve a metade
print(first_half([1, 2, 3, 4, 5], True))   # [1, 2, 3]
print(first_half([1, 2, 3, 4, 5], False))  # [1, 2]


# ---------------------------------------------------------------------------
# PARTE 3 — tuplas, sets e dicionários
# ---------------------------------------------------------------------------

# 3.1 Tuplas
cores = ("vermelho", "verde", "amarelo")

# 3.1.1 Verifica se é possível fazer cores[1] = "azul"
# cores[1] = "azul"   → TypeError: as tuplas são imutáveis, não dá para alterar

# 3.1.2 Obtém uma tupla com "azul" no lugar de "verde", partindo da tupla original
lista_cores = list(cores)          # 1. transforma a tupla numa lista (que é mutável)
lista_cores[1] = "azul"            # 2. altera a posição 1 ("verde") na lista
cores_nova = tuple(lista_cores)    # 3. refaz uma tupla a partir da lista
print(cores_nova)                  # ('vermelho', 'azul', 'amarelo')
print(cores)                       # a original continua igual: ('vermelho', 'verde', 'amarelo')


# 3.2 Tuplas: acesso e métodos
notas = (12, 15, 15, 18, 9)
print(notas[0])               # primeira nota: índice 0 → 12
print(notas[-1])              # última nota: -1 conta a partir do fim → 9
print(notas[len(notas) - 1])  # alternativa: último índice = comprimento - 1 → 9
print(notas.count(15))        # count() conta quantas vezes o valor aparece → 2
print(notas.index(18))        # index() devolve a posição da 1ª ocorrência → 3


# 3.3 Sets
# IDEIA: os sets não guardam duplicados, por isso o "FI" repetido desaparece.
aluno_a = {"FI", "SO", "RC", "FI"}
print(aluno_a)        # {'FI', 'SO', 'RC'} (a ordem pode variar: sets não são ordenados)
print(len(aluno_a))   # 3, e não 4! O "FI" repetido foi eliminado.

# 3.3.1 Comparar sets
# IDEIA: cada pergunta corresponde a uma operação de conjuntos da matemática.
aluno_b = {"FI", "Álgebra", "RC", "IA"}
print(aluno_a.intersection(aluno_b))          # ambos frequentam (interseção) → {'FI', 'RC'}
print(aluno_a.union(aluno_b))                 # todas as disciplinas (união)
print(aluno_a.difference(aluno_b))            # só o A frequenta (diferença A − B) → {'SO'}
print(aluno_a.symmetric_difference(aluno_b))  # só um dos dois (diferença simétrica) → {'SO', 'Álgebra', 'IA'}


# 3.4 Dicionários
# IDEIA: num dicionário acede-se, altera-se e acrescenta-se sempre pela CHAVE, com [ ].
filme = {
    "titulo": "Interstellar",
    "ano": 2013,                     # ano "errado" de propósito, para corrigir a seguir
    "realizador": "Christopher Nolan",
    "duracao_min": 169
}
print(filme["titulo"])                 # imprime o título: acede pela chave
filme["ano"] = 2014                    # corrige o ano: a chave já existe, por isso substitui o valor
filme["genero"] = "Ficção científica"  # adiciona "genero": a chave não existe, por isso é criada
filme.pop("duracao_min")               # remove a chave "duracao_min" (e o seu valor)
print(filme.keys())                    # imprime as chaves


# ---------------------------------------------------------------------------
# PARTE 4 — estruturas aninhadas (turma, contactos, F1)
# ---------------------------------------------------------------------------
# A fazer.
