eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {
    'one' : 'uno',
    'two': 'dos',
    'three': 'tres'}

print(eng2sp)
print(eng2sp['one'])

# OPERADOS IN
print('dos' in eng2sp)

#VERIFICAR OS VALORES DO DICIONÁRIO
valores = eng2sp.values()
print('uno' in valores)

# CONTADOR DE LETRAS
def count_letters(s):
    d = dict () # dicionário vazio
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
dict_contagem = count_letters("Paralelepipedo")
print(dict_contagem)