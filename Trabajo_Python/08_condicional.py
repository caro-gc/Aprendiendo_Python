# Condicional if
adivinar = 42
numero = int(input('Sr usuario, digite un número: '))
if (numero > adivinar):
  print('Bájele el volumen')
elif (numero < adivinar):
  print('Subale el volumen')
else:
  print("VERDADERO")

# IF anidado 2:
if (numero >= adivinar):
  if (numero > adivinar):
    print('Coloque un número menor.')
  else:
    print('Acertado!!!')
else:
  print('Coloque un número mayor')
# Fin del IF.

print('La instrución "IF" terminó. ')
