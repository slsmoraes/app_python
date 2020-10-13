# conjunto = {1, 2, 3, 4}
# print(type(conjunto))  # class 'set'
# print(conjunto)
#
# conjuntoA = {1, 2, 3, 4, 2, 4, 5}
# print('conjuntoA: ', conjuntoA) # note que o 2 e o 4 são listados uma unica vez.
# conjuntoA.add(7)
# print('connjuntoA add: ', conjuntoA)
# conjuntoA.discard(2)
# print('cojuntoA discard: ', conjuntoA)

cjA = {1, 2, 3, 4, 5}
cjB = {5, 6, 7, 8}
print('cjA: ', cjA)
print('cjB: ', cjB)

cj_uniao = cjA.union(cjB)
print('união: ', cj_uniao)

cj_interseccao = cjA.intersection(cjB)
print('intersecção: ', cj_interseccao)

cj_diferencaA = cjA.difference(cjB)
print('difereça entre A e B: ', cj_diferencaA)
cj_diferencaB = cjB.difference(cjA)
print('difereça entre B e A: ', cj_diferencaB)

cj_simetrica = cjA.symmetric_difference(cjB)
print('diferença simétrica: {}'.format(cj_simetrica))

cjA = {1, 2, 3}
cjB = {1, 2, 3, 4, 5}
print('A: {}'.format(cjA))
print('B: {}'.format(cjB))

cj_subset = cjA.issubset(cjB)
print('subset entre A e B: {}'.format(cj_subset))
cj_subset = cjB.issubset(cjA)
print('subset entre B e A: {}'.format(cj_subset))

cj_superset = cjB.issuperset(cjA)
print('superset: entre B e A {}'.format(cj_superset))
cj_superset = cjA.issuperset(cjB)
print('superset: entre A e B {}'.format(cj_superset))

# Converter lista pra conjunto
lista = ['cachorro', 'gato', 'gato', 'cachorro', 'elefante']
cj_animais = set(lista)
print('conjunto animais: {}'.format(cj_animais))
lista_animais = list(cj_animais)
print('lista sem duplicidade: {}'.format(lista_animais))