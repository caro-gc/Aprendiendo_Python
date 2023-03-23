number = int(input('Digite un número: '))
# OPERACIONES RELACIONALES O DE COMPARACIÓN (RESULTADO BOOLEANO)
# True(1) / False(0)
print(number > 3)  # pregunta si number es mayor que 3
print(number >= 3)  # pregunta si number es mayor o igual a 3
print(number < 3)  # si number es menor a 3
print(number <= 3)  # si number es menor o igual a 3
print(number == 3)  # si number es igual a 3
print(number != 3)  # si number es diferente a 3

# OPERACIONES LÓGICAS
print("Operaciones lógicas.")
# Conjunción (and &)
print("Conjunción:")
print(False and False)
print(False & False)
print(number > 3 and number < 10)

# Disyunción (or, |)
print('Disyunción:')
print(False or True)
print(number <= 3 or number >= 10)
print(not (number <= 3 | number >= 10))

# Negación (not)
print('Negación:')
print(not (True))

# Or exclusiva (^)
print('Or exclusiva:')
print(False ^ False)
print(False ^ True)
print(True ^ False)
print(True ^ True)

# ****OPERACIONES DE PERTENENCIA ****
# in
print('Operador in:')
nombre = 'Cesar Quintero'
print('Q' in nombre)
print('z' in nombre)

